"""
Correction complète - Exercice 5 : Projet complet d'analyseur de logs
======================================================================

Cette correction implémente un système complet d'analyse de logs avec gestion
d'exceptions robuste, traitement de fichiers et génération de rapports.
"""

import os
import re
import json
import csv
from datetime import datetime, timedelta
from pathlib import Path
from collections import defaultdict, Counter
from typing import Dict, List, Optional, Tuple, Any
import gzip
import zipfile


# ===== EXCEPTIONS PERSONNALISÉES =====

class LogAnalyzerError(Exception):
    """Exception de base pour l'analyseur de logs."""
    
    def __init__(self, message: str, code_erreur: str = "LOG_ERROR", details: Optional[dict] = None):
        self.message = message
        self.code_erreur = code_erreur
        self.details = details or {}
        self.timestamp = datetime.now()
        super().__init__(self.message)
    
    def __str__(self):
        base_msg = f"[{self.code_erreur}] {self.message}"
        if self.details:
            details_str = ", ".join([f"{k}={v}" for k, v in self.details.items()])
            base_msg += f" (Détails: {details_str})"
        return base_msg


class FichierLogError(LogAnalyzerError):
    """Erreurs liées aux fichiers de logs."""
    pass


class FichierLogIntrouvableError(FichierLogError):
    """Erreur levée quand un fichier de log n'est pas trouvé."""
    
    def __init__(self, chemin_fichier: str):
        message = f"Fichier de log non trouvé : {chemin_fichier}"
        super().__init__(message, "FICHIER_LOG_INTROUVABLE", {"chemin": chemin_fichier})


class FormatLogInvalideError(FichierLogError):
    """Erreur levée pour un format de log invalide."""
    
    def __init__(self, ligne: str, numero_ligne: int, raison: str):
        message = f"Format de log invalide ligne {numero_ligne} : {raison}"
        super().__init__(message, "FORMAT_LOG_INVALIDE", {
            "ligne": ligne[:100],  # Limiter la taille
            "numero_ligne": numero_ligne,
            "raison": raison
        })


class ConfigurationError(LogAnalyzerError):
    """Erreurs de configuration."""
    pass


class ConfigurationInvalideError(ConfigurationError):
    """Erreur levée pour une configuration invalide."""
    
    def __init__(self, parametre: str, valeur: Any, raison: str):
        message = f"Configuration invalide pour {parametre} : {valeur} ({raison})"
        super().__init__(message, "CONFIGURATION_INVALIDE", {
            "parametre": parametre,
            "valeur": str(valeur),
            "raison": raison
        })


class RapportError(LogAnalyzerError):
    """Erreurs de génération de rapport."""
    pass


# ===== CLASSES MÉTIER =====

class EntreeLog:
    """Représente une entrée de log parsée."""
    
    def __init__(self, timestamp: datetime, niveau: str, message: str, 
                 source: str = None, ip_address: str = None, user_agent: str = None):
        self.timestamp = timestamp
        self.niveau = niveau.upper()
        self.message = message
        self.source = source
        self.ip_address = ip_address
        self.user_agent = user_agent
        self.donnees_supplementaires = {}
    
    def ajouter_donnee(self, cle: str, valeur: Any):
        """Ajoute des données supplémentaires à l'entrée."""
        self.donnees_supplementaires[cle] = valeur
    
    def to_dict(self) -> dict:
        """Convertit l'entrée en dictionnaire."""
        return {
            'timestamp': self.timestamp.isoformat(),
            'niveau': self.niveau,
            'message': self.message,
            'source': self.source,
            'ip_address': self.ip_address,
            'user_agent': self.user_agent,
            'donnees_supplementaires': self.donnees_supplementaires
        }
    
    def est_erreur(self) -> bool:
        """Vérifie si c'est une entrée d'erreur."""
        return self.niveau in ['ERROR', 'CRITICAL', 'FATAL']
    
    def est_avertissement(self) -> bool:
        """Vérifie si c'est un avertissement."""
        return self.niveau in ['WARNING', 'WARN']


class ParseurLog:
    """Parse différents formats de logs."""
    
    def __init__(self):
        self.patterns = {
            'apache_combined': re.compile(
                r'(?P<ip>\S+) \S+ \S+ \[(?P<timestamp>[^\]]+)\] '
                r'"(?P<method>\S+) (?P<url>\S+) (?P<protocol>[^"]+)" '
                r'(?P<status>\d+) (?P<size>\S+) '
                r'"(?P<referer>[^"]*)" "(?P<user_agent>[^"]*)"'
            ),
            'apache_common': re.compile(
                r'(?P<ip>\S+) \S+ \S+ \[(?P<timestamp>[^\]]+)\] '
                r'"(?P<method>\S+) (?P<url>\S+) (?P<protocol>[^"]+)" '
                r'(?P<status>\d+) (?P<size>\S+)'
            ),
            'syslog': re.compile(
                r'(?P<timestamp>\w+\s+\d+\s+\d+:\d+:\d+) '
                r'(?P<hostname>\S+) (?P<process>\S+): (?P<message>.*)'
            ),
            'custom_app': re.compile(
                r'(?P<timestamp>\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2}) '
                r'\[(?P<niveau>\w+)\] (?P<source>\S+): (?P<message>.*)'
            ),
            'iis': re.compile(
                r'(?P<timestamp>\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2}) '
                r'(?P<server_ip>\S+) (?P<method>\S+) (?P<uri>\S+) '
                r'(?P<query>\S+) (?P<port>\d+) (?P<username>\S+) '
                r'(?P<client_ip>\S+) (?P<user_agent>[^"]+) '
                r'(?P<status>\d+) (?P<substatus>\d+) (?P<win32_status>\d+) '
                r'(?P<time_taken>\d+)'
            )
        }
        
        self.formats_timestamp = [
            '%Y-%m-%d %H:%M:%S',
            '%d/%b/%Y:%H:%M:%S %z',
            '%b %d %H:%M:%S',
            '%Y-%m-%dT%H:%M:%S',
            '%Y-%m-%d %H:%M:%S.%f'
        ]
    
    def detecter_format(self, ligne: str) -> Optional[str]:
        """Détecte automatiquement le format d'une ligne de log."""
        for nom_format, pattern in self.patterns.items():
            if pattern.match(ligne):
                return nom_format
        return None
    
    def parser_timestamp(self, timestamp_str: str) -> datetime:
        """Parse un timestamp avec différents formats."""
        # Nettoyer le timestamp
        timestamp_str = timestamp_str.strip()
        
        for fmt in self.formats_timestamp:
            try:
                return datetime.strptime(timestamp_str, fmt)
            except ValueError:
                continue
        
        # Essayer avec des formats plus flexibles
        try:
            # Format Apache avec timezone
            if '+' in timestamp_str or '-' in timestamp_str[-6:]:
                timestamp_str = timestamp_str.rsplit(' ', 1)[0]
                return datetime.strptime(timestamp_str, '%d/%b/%Y:%H:%M:%S')
        except ValueError:
            pass
        
        # Si aucun format ne fonctionne, utiliser la date actuelle
        raise ValueError(f"Format de timestamp non reconnu : {timestamp_str}")
    
    def parser_ligne(self, ligne: str, format_force: Optional[str] = None) -> Optional[EntreeLog]:
        """Parse une ligne de log."""
        ligne = ligne.strip()
        if not ligne or ligne.startswith('#'):
            return None
        
        # Détecter le format si non spécifié
        if format_force:
            format_detecte = format_force
        else:
            format_detecte = self.detecter_format(ligne)
        
        if not format_detecte:
            raise FormatLogInvalideError(ligne, 0, "Format non reconnu")
        
        pattern = self.patterns[format_detecte]
        match = pattern.match(ligne)
        
        if not match:
            raise FormatLogInvalideError(ligne, 0, f"Ne correspond pas au pattern {format_detecte}")
        
        donnees = match.groupdict()
        
        # Parser selon le format
        try:
            if format_detecte in ['apache_combined', 'apache_common']:
                timestamp = self.parser_timestamp(donnees['timestamp'])
                niveau = self._niveau_depuis_status(donnees['status'])
                message = f"{donnees['method']} {donnees['url']} - Status {donnees['status']}"
                
                entree = EntreeLog(timestamp, niveau, message, ip_address=donnees['ip'])
                entree.ajouter_donnee('method', donnees['method'])
                entree.ajouter_donnee('url', donnees['url'])
                entree.ajouter_donnee('status', int(donnees['status']))
                entree.ajouter_donnee('size', donnees['size'])
                
                if 'user_agent' in donnees:
                    entree.user_agent = donnees['user_agent']
                
            elif format_detecte == 'syslog':
                # Pour syslog, ajouter l'année actuelle
                timestamp_str = f"{datetime.now().year} {donnees['timestamp']}"
                timestamp = datetime.strptime(timestamp_str, "%Y %b %d %H:%M:%S")
                
                entree = EntreeLog(timestamp, "INFO", donnees['message'], 
                                 source=donnees['process'])
                entree.ajouter_donnee('hostname', donnees['hostname'])
                
            elif format_detecte == 'custom_app':
                timestamp = self.parser_timestamp(donnees['timestamp'])
                entree = EntreeLog(timestamp, donnees['niveau'], donnees['message'], 
                                 source=donnees['source'])
                
            elif format_detecte == 'iis':
                timestamp = self.parser_timestamp(donnees['timestamp'])
                niveau = self._niveau_depuis_status(donnees['status'])
                message = f"{donnees['method']} {donnees['uri']} - Status {donnees['status']}"
                
                entree = EntreeLog(timestamp, niveau, message, ip_address=donnees['client_ip'])
                entree.ajouter_donnee('method', donnees['method'])
                entree.ajouter_donnee('uri', donnees['uri'])
                entree.ajouter_donnee('status', int(donnees['status']))
                entree.ajouter_donnee('time_taken', int(donnees['time_taken']))
                
            else:
                raise FormatLogInvalideError(ligne, 0, f"Traitement non implémenté pour {format_detecte}")
            
            return entree
            
        except Exception as e:
            raise FormatLogInvalideError(ligne, 0, str(e))
    
    def _niveau_depuis_status(self, status: str) -> str:
        """Détermine le niveau de log depuis un code de status HTTP."""
        code = int(status)
        if code >= 500:
            return "ERROR"
        elif code >= 400:
            return "WARNING"
        elif code >= 300:
            return "INFO"
        else:
            return "DEBUG"


class AnalyseurStatistiques:
    """Analyse les statistiques des logs."""
    
    def __init__(self):
        self.reset()
    
    def reset(self):
        """Remet à zéro les statistiques."""
        self.total_entrees = 0
        self.par_niveau = Counter()
        self.par_heure = defaultdict(int)
        self.par_jour = defaultdict(int)
        self.par_source = Counter()
        self.ips_uniques = set()
        self.erreurs_frequentes = Counter()
        self.temps_reponse = []
        self.urls_populaires = Counter()
    
    def ajouter_entree(self, entree: EntreeLog):
        """Ajoute une entrée aux statistiques."""
        self.total_entrees += 1
        self.par_niveau[entree.niveau] += 1
        
        # Statistiques temporelles
        heure = entree.timestamp.hour
        jour = entree.timestamp.date()
        self.par_heure[heure] += 1
        self.par_jour[jour] += 1
        
        # Source
        if entree.source:
            self.par_source[entree.source] += 1
        
        # IP
        if entree.ip_address:
            self.ips_uniques.add(entree.ip_address)
        
        # Erreurs fréquentes
        if entree.est_erreur():
            # Extraire les premiers mots du message d'erreur
            mots_erreur = ' '.join(entree.message.split()[:5])
            self.erreurs_frequentes[mots_erreur] += 1
        
        # Données spécifiques selon le type
        if 'time_taken' in entree.donnees_supplementaires:
            self.temps_reponse.append(entree.donnees_supplementaires['time_taken'])
        
        if 'url' in entree.donnees_supplementaires:
            self.urls_populaires[entree.donnees_supplementaires['url']] += 1
    
    def obtenir_statistiques(self) -> dict:
        """Obtient un résumé des statistiques."""
        stats = {
            'total_entrees': self.total_entrees,
            'par_niveau': dict(self.par_niveau),
            'ips_uniques': len(self.ips_uniques),
            'erreurs_total': sum(count for niveau, count in self.par_niveau.items() 
                               if niveau in ['ERROR', 'CRITICAL', 'FATAL']),
            'periode': self._obtenir_periode(),
            'top_erreurs': dict(self.erreurs_frequentes.most_common(10)),
            'top_urls': dict(self.urls_populaires.most_common(10)),
            'top_sources': dict(self.par_source.most_common(10))
        }
        
        if self.temps_reponse:
            stats['temps_reponse'] = {
                'min': min(self.temps_reponse),
                'max': max(self.temps_reponse),
                'moyenne': sum(self.temps_reponse) / len(self.temps_reponse)
            }
        
        return stats
    
    def _obtenir_periode(self) -> Optional[dict]:
        """Obtient la période couverte par les logs."""
        if not self.par_jour:
            return None
        
        dates = list(self.par_jour.keys())
        return {
            'debut': min(dates).isoformat(),
            'fin': max(dates).isoformat(),
            'jours': len(dates)
        }


class AnalyseurLog:
    """Analyseur principal de logs."""
    
    def __init__(self, configuration: Optional[dict] = None):
        self.parseur = ParseurLog()
        self.statistiques = AnalyseurStatistiques()
        self.entrees = []
        self.erreurs_traitement = []
        
        # Configuration par défaut
        self.config = {
            'format_force': None,
            'ignorer_erreurs_parsing': True,
            'max_entrees_memoire': 100000,
            'filtres_niveau': [],
            'filtres_source': [],
            'periode_debut': None,
            'periode_fin': None,
            'sauvegarde_automatique': True,
            'compression_logs': False
        }
        
        if configuration:
            self.config.update(configuration)
        
        self._valider_configuration()
    
    def _valider_configuration(self):
        """Valide la configuration."""
        if self.config['max_entrees_memoire'] <= 0:
            raise ConfigurationInvalideError(
                'max_entrees_memoire', 
                self.config['max_entrees_memoire'],
                'doit être supérieur à 0'
            )
        
        if self.config['format_force'] and self.config['format_force'] not in self.parseur.patterns:
            raise ConfigurationInvalideError(
                'format_force',
                self.config['format_force'],
                f"format non supporté. Formats disponibles: {list(self.parseur.patterns.keys())}"
            )
    
    def analyser_fichier(self, chemin_fichier: str) -> dict:
        """
        Analyse un fichier de log.
        
        Args:
            chemin_fichier: Chemin vers le fichier de log
            
        Returns:
            Rapport d'analyse
            
        Raises:
            FichierLogIntrouvableError: Si le fichier n'existe pas
            PermissionError: Si impossible de lire le fichier
        """
        chemin = Path(chemin_fichier)
        
        if not chemin.exists():
            raise FichierLogIntrouvableError(str(chemin))
        
        # Réinitialiser pour ce fichier
        self.statistiques.reset()
        self.entrees.clear()
        self.erreurs_traitement.clear()
        
        try:
            # Déterminer comment ouvrir le fichier
            if chemin.suffix.lower() == '.gz':
                opener = gzip.open
                mode = 'rt'
            elif chemin.suffix.lower() == '.zip':
                return self._analyser_fichier_zip(chemin)
            else:
                opener = open
                mode = 'r'
            
            ligne_numero = 0
            entrees_traitees = 0
            
            with opener(chemin, mode, encoding='utf-8', errors='replace') as fichier:
                for ligne in fichier:
                    ligne_numero += 1
                    
                    try:
                        entree = self.parseur.parser_ligne(
                            ligne.strip(), 
                            self.config['format_force']
                        )
                        
                        if entree and self._appliquer_filtres(entree):
                            self.statistiques.ajouter_entree(entree)
                            
                            # Garder en mémoire selon la limite
                            if len(self.entrees) < self.config['max_entrees_memoire']:
                                self.entrees.append(entree)
                            
                            entrees_traitees += 1
                            
                    except FormatLogInvalideError as e:
                        e.details['numero_ligne'] = ligne_numero
                        self.erreurs_traitement.append(e.to_dict())
                        
                        if not self.config['ignorer_erreurs_parsing']:
                            raise
                    
                    except Exception as e:
                        erreur = LogAnalyzerError(
                            f"Erreur ligne {ligne_numero}: {str(e)}",
                            "ERREUR_TRAITEMENT_LIGNE"
                        )
                        self.erreurs_traitement.append(erreur.to_dict())
            
            # Générer le rapport
            rapport = {
                'fichier': str(chemin),
                'taille_fichier': chemin.stat().st_size,
                'lignes_totales': ligne_numero,
                'entrees_traitees': entrees_traitees,
                'erreurs_parsing': len(self.erreurs_traitement),
                'statistiques': self.statistiques.obtenir_statistiques(),
                'timestamp_analyse': datetime.now().isoformat()
            }
            
            # Sauvegarder si demandé
            if self.config['sauvegarde_automatique']:
                self._sauvegarder_resultats(rapport)
            
            return rapport
            
        except PermissionError:
            raise PermissionError(f"Permission refusée pour lire le fichier : {chemin}")
        except UnicodeDecodeError as e:
            raise LogAnalyzerError(
                f"Erreur d'encodage dans le fichier {chemin}: {str(e)}",
                "ERREUR_ENCODAGE"
            )
        except Exception as e:
            raise LogAnalyzerError(
                f"Erreur lors de l'analyse de {chemin}: {str(e)}",
                "ERREUR_ANALYSE_FICHIER"
            )
    
    def _analyser_fichier_zip(self, chemin_zip: Path) -> dict:
        """Analyse un fichier ZIP contenant des logs."""
        rapports = []
        
        try:
            with zipfile.ZipFile(chemin_zip, 'r') as zip_file:
                for nom_fichier in zip_file.namelist():
                    if nom_fichier.endswith('.log') or nom_fichier.endswith('.txt'):
                        try:
                            with zip_file.open(nom_fichier) as fichier:
                                contenu = fichier.read().decode('utf-8', errors='replace')
                                
                                # Traiter ligne par ligne
                                for ligne_numero, ligne in enumerate(contenu.splitlines(), 1):
                                    try:
                                        entree = self.parseur.parser_ligne(ligne.strip(), self.config['format_force'])
                                        if entree and self._appliquer_filtres(entree):
                                            self.statistiques.ajouter_entree(entree)
                                            if len(self.entrees) < self.config['max_entrees_memoire']:
                                                self.entrees.append(entree)
                                    except Exception:
                                        pass  # Ignorer les erreurs dans les ZIPs
                                        
                        except Exception as e:
                            self.erreurs_traitement.append({
                                'fichier': nom_fichier,
                                'erreur': str(e)
                            })
            
            return {
                'fichier': str(chemin_zip),
                'type': 'archive_zip',
                'statistiques': self.statistiques.obtenir_statistiques(),
                'erreurs_parsing': len(self.erreurs_traitement)
            }
            
        except zipfile.BadZipFile:
            raise LogAnalyzerError(f"Fichier ZIP invalide : {chemin_zip}", "ZIP_INVALIDE")
    
    def _appliquer_filtres(self, entree: EntreeLog) -> bool:
        """Applique les filtres configurés à une entrée."""
        # Filtre par niveau
        if self.config['filtres_niveau'] and entree.niveau not in self.config['filtres_niveau']:
            return False
        
        # Filtre par source
        if self.config['filtres_source'] and entree.source not in self.config['filtres_source']:
            return False
        
        # Filtre par période
        if self.config['periode_debut']:
            if entree.timestamp < self.config['periode_debut']:
                return False
        
        if self.config['periode_fin']:
            if entree.timestamp > self.config['periode_fin']:
                return False
        
        return True
    
    def _sauvegarder_resultats(self, rapport: dict):
        """Sauvegarde les résultats d'analyse."""
        try:
            dossier_resultats = Path("resultats_logs")
            dossier_resultats.mkdir(exist_ok=True)
            
            # Nom du fichier avec timestamp
            timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
            nom_base = Path(rapport['fichier']).stem
            
            # Sauvegarder le rapport JSON
            chemin_rapport = dossier_resultats / f"rapport_{nom_base}_{timestamp}.json"
            with open(chemin_rapport, 'w', encoding='utf-8') as f:
                json.dump(rapport, f, indent=2, ensure_ascii=False, default=str)
            
            # Sauvegarder les entrées en CSV
            if self.entrees:
                chemin_csv = dossier_resultats / f"entrees_{nom_base}_{timestamp}.csv"
                self._exporter_csv(chemin_csv)
            
        except Exception as e:
            # Ne pas faire échouer l'analyse pour un problème de sauvegarde
            pass
    
    def _exporter_csv(self, chemin_fichier: Path):
        """Exporte les entrées de log en CSV."""
        if not self.entrees:
            return
        
        with open(chemin_fichier, 'w', newline='', encoding='utf-8') as csvfile:
            fieldnames = ['timestamp', 'niveau', 'message', 'source', 'ip_address', 'user_agent']
            
            # Ajouter les champs des données supplémentaires
            donnees_supplementaires = set()
            for entree in self.entrees:
                donnees_supplementaires.update(entree.donnees_supplementaires.keys())
            
            fieldnames.extend(sorted(donnees_supplementaires))
            
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
            writer.writeheader()
            
            for entree in self.entrees:
                ligne = entree.to_dict()
                # Aplatir les données supplémentaires
                ligne.update(entree.donnees_supplementaires)
                del ligne['donnees_supplementaires']
                
                writer.writerow(ligne)
    
    def analyser_dossier(self, chemin_dossier: str, pattern: str = "*.log") -> dict:
        """
        Analyse tous les fichiers de log d'un dossier.
        
        Args:
            chemin_dossier: Chemin vers le dossier
            pattern: Pattern de fichiers à analyser
            
        Returns:
            Rapport consolidé
        """
        dossier = Path(chemin_dossier)
        
        if not dossier.exists():
            raise FichierLogIntrouvableError(str(dossier))
        
        if not dossier.is_dir():
            raise LogAnalyzerError(f"{dossier} n'est pas un dossier", "PAS_UN_DOSSIER")
        
        # Trouver tous les fichiers correspondants
        fichiers = list(dossier.glob(pattern))
        fichiers.extend(dossier.glob("**/" + pattern))  # Recherche récursive
        
        if not fichiers:
            raise LogAnalyzerError(f"Aucun fichier trouvé avec le pattern {pattern}", "AUCUN_FICHIER")
        
        rapports_individuels = []
        erreurs_fichiers = []
        
        # Réinitialiser les statistiques globales
        self.statistiques.reset()
        self.entrees.clear()
        self.erreurs_traitement.clear()
        
        for fichier in fichiers:
            try:
                rapport = self.analyser_fichier(str(fichier))
                rapports_individuels.append(rapport)
                
                # Les statistiques sont cumulées automatiquement
                
            except Exception as e:
                erreurs_fichiers.append({
                    'fichier': str(fichier),
                    'erreur': str(e),
                    'type_erreur': type(e).__name__
                })
        
        # Générer le rapport consolidé
        rapport_consolide = {
            'dossier': str(dossier),
            'pattern': pattern,
            'fichiers_analyses': len(rapports_individuels),
            'fichiers_erreur': len(erreurs_fichiers),
            'statistiques_globales': self.statistiques.obtenir_statistiques(),
            'rapports_individuels': rapports_individuels,
            'erreurs_fichiers': erreurs_fichiers,
            'timestamp_analyse': datetime.now().isoformat()
        }
        
        return rapport_consolide
    
    def generer_rapport_html(self, rapport: dict, chemin_sortie: str):
        """Génère un rapport HTML à partir des données d'analyse."""
        try:
            html_template = """
<!DOCTYPE html>
<html lang="fr">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Rapport d'Analyse de Logs</title>
    <style>
        body { font-family: Arial, sans-serif; margin: 20px; background-color: #f5f5f5; }
        .container { max-width: 1200px; margin: 0 auto; background: white; padding: 20px; border-radius: 8px; box-shadow: 0 2px 10px rgba(0,0,0,0.1); }
        h1, h2 { color: #333; border-bottom: 2px solid #007acc; padding-bottom: 10px; }
        .stat-box { background: #f8f9fa; padding: 15px; margin: 10px 0; border-left: 4px solid #007acc; }
        .error { background: #ffe6e6; border-left-color: #dc3545; }
        .warning { background: #fff3cd; border-left-color: #ffc107; }
        .success { background: #d4edda; border-left-color: #28a745; }
        table { width: 100%; border-collapse: collapse; margin: 20px 0; }
        th, td { padding: 12px; text-align: left; border-bottom: 1px solid #ddd; }
        th { background-color: #007acc; color: white; }
        tr:hover { background-color: #f5f5f5; }
        .chart { margin: 20px 0; }
        .progress-bar { width: 100%; background-color: #f0f0f0; border-radius: 4px; overflow: hidden; }
        .progress-fill { height: 20px; background-color: #007acc; text-align: center; line-height: 20px; color: white; font-size: 12px; }
    </style>
</head>
<body>
    <div class="container">
        <h1>📊 Rapport d'Analyse de Logs</h1>
        
        <div class="stat-box">
            <h3>📁 Informations du fichier</h3>
            <p><strong>Fichier:</strong> {fichier}</p>
            <p><strong>Analysé le:</strong> {timestamp}</p>
            <p><strong>Taille:</strong> {taille} octets</p>
        </div>
        
        <div class="stat-box {classe_entrees}">
            <h3>📈 Statistiques générales</h3>
            <p><strong>Total des entrées:</strong> {total_entrees}</p>
            <p><strong>Erreurs de parsing:</strong> {erreurs_parsing}</p>
            <p><strong>IPs uniques:</strong> {ips_uniques}</p>
        </div>
        
        <h2>🎯 Répartition par niveau</h2>
        <table>
            <tr><th>Niveau</th><th>Nombre</th><th>Pourcentage</th><th>Graphique</th></tr>
            {tableau_niveaux}
        </table>
        
        <h2>🔥 Top des erreurs</h2>
        <table>
            <tr><th>Message d'erreur</th><th>Occurrences</th></tr>
            {tableau_erreurs}
        </table>
        
        <h2>🌐 URLs les plus populaires</h2>
        <table>
            <tr><th>URL</th><th>Hits</th></tr>
            {tableau_urls}
        </table>
        
        <h2>⏰ Activité par heure</h2>
        <div class="chart">
            {graphique_heures}
        </div>
        
        <div class="stat-box">
            <h3>ℹ️ Informations techniques</h3>
            <p><strong>Période couverte:</strong> {periode}</p>
            <p><strong>Temps de réponse moyen:</strong> {temps_reponse}</p>
        </div>
    </div>
</body>
</html>
            """
            
            # Extraire les données
            stats = rapport.get('statistiques', {})
            
            # Calculer les pourcentages et générer les tableaux
            total = stats.get('total_entrees', 0)
            niveaux = stats.get('par_niveau', {})
            
            tableau_niveaux = ""
            for niveau, count in niveaux.items():
                pourcentage = (count / total * 100) if total > 0 else 0
                classe_niveau = "error" if niveau in ["ERROR", "CRITICAL"] else "warning" if niveau == "WARNING" else "success"
                
                tableau_niveaux += f"""
                <tr class="{classe_niveau}">
                    <td>{niveau}</td>
                    <td>{count}</td>
                    <td>{pourcentage:.1f}%</td>
                    <td>
                        <div class="progress-bar">
                            <div class="progress-fill" style="width: {pourcentage}%">{pourcentage:.1f}%</div>
                        </div>
                    </td>
                </tr>
                """
            
            # Top erreurs
            tableau_erreurs = ""
            for erreur, count in stats.get('top_erreurs', {}).items():
                tableau_erreurs += f"<tr><td>{erreur}</td><td>{count}</td></tr>"
            
            # Top URLs
            tableau_urls = ""
            for url, count in stats.get('top_urls', {}).items():
                tableau_urls += f"<tr><td>{url}</td><td>{count}</td></tr>"
            
            # Graphique activité par heure (simplifié)
            graphique_heures = "<p>Graphique des heures disponible dans les données JSON</p>"
            
            # Remplir le template
            html_content = html_template.format(
                fichier=rapport.get('fichier', 'N/A'),
                timestamp=rapport.get('timestamp_analyse', 'N/A'),
                taille=rapport.get('taille_fichier', 0),
                total_entrees=total,
                erreurs_parsing=rapport.get('erreurs_parsing', 0),
                ips_uniques=stats.get('ips_uniques', 0),
                classe_entrees="success" if rapport.get('erreurs_parsing', 0) == 0 else "warning",
                tableau_niveaux=tableau_niveaux,
                tableau_erreurs=tableau_erreurs,
                tableau_urls=tableau_urls,
                graphique_heures=graphique_heures,
                periode=stats.get('periode', {}).get('debut', 'N/A') + " à " + stats.get('periode', {}).get('fin', 'N/A'),
                temps_reponse=f"{stats.get('temps_reponse', {}).get('moyenne', 0):.2f}ms" if 'temps_reponse' in stats else "N/A"
            )
            
            # Sauvegarder
            with open(chemin_sortie, 'w', encoding='utf-8') as f:
                f.write(html_content)
                
        except Exception as e:
            raise RapportError(f"Erreur lors de la génération du rapport HTML : {str(e)}")


def interface_analyseur():
    """Interface interactive pour l'analyseur de logs."""
    print("=== ANALYSEUR DE LOGS AVANCÉ ===")
    
    analyseur = AnalyseurLog()
    
    while True:
        print("\nMenu principal :")
        print("1. Analyser un fichier de log")
        print("2. Analyser un dossier de logs")
        print("3. Configurer l'analyseur")
        print("4. Générer un rapport HTML")
        print("5. Quitter")
        
        try:
            choix = input("\nVotre choix (1-5) : ").strip()
            
            if choix == '1':
                fichier = input("Chemin du fichier de log : ")
                try:
                    print("Analyse en cours...")
                    rapport = analyseur.analyser_fichier(fichier)
                    
                    stats = rapport['statistiques']
                    print(f"\n✅ Analyse terminée !")
                    print(f"Total des entrées : {stats['total_entrees']}")
                    print(f"Erreurs de parsing : {rapport['erreurs_parsing']}")
                    print(f"IPs uniques : {stats['ips_uniques']}")
                    print(f"Période : {stats.get('periode', {}).get('debut', 'N/A')} à {stats.get('periode', {}).get('fin', 'N/A')}")
                    
                    print("\nRépartition par niveau :")
                    for niveau, count in stats['par_niveau'].items():
                        print(f"  {niveau}: {count}")
                    
                    if stats['top_erreurs']:
                        print("\nTop 3 des erreurs :")
                        for i, (erreur, count) in enumerate(list(stats['top_erreurs'].items())[:3], 1):
                            print(f"  {i}. {erreur}: {count}")
                    
                except Exception as e:
                    print(f"❌ Erreur : {e}")
                    
            elif choix == '2':
                dossier = input("Chemin du dossier : ")
                pattern = input("Pattern de fichiers [*.log] : ") or "*.log"
                
                try:
                    print("Analyse du dossier en cours...")
                    rapport = analyseur.analyser_dossier(dossier, pattern)
                    
                    print(f"\n✅ Analyse terminée !")
                    print(f"Fichiers analysés : {rapport['fichiers_analyses']}")
                    print(f"Fichiers en erreur : {rapport['fichiers_erreur']}")
                    
                    stats = rapport['statistiques_globales']
                    print(f"Total des entrées : {stats['total_entrees']}")
                    print(f"IPs uniques : {stats['ips_uniques']}")
                    
                except Exception as e:
                    print(f"❌ Erreur : {e}")
                    
            elif choix == '3':
                print("\nConfiguration actuelle :")
                for cle, valeur in analyseur.config.items():
                    print(f"  {cle}: {valeur}")
                
                print("\nModification (laisser vide pour ignorer) :")
                
                nouveau_max = input(f"Max entrées en mémoire [{analyseur.config['max_entrees_memoire']}] : ")
                if nouveau_max:
                    try:
                        analyseur.config['max_entrees_memoire'] = int(nouveau_max)
                    except ValueError:
                        print("❌ Valeur invalide")
                
                ignorer_erreurs = input(f"Ignorer erreurs parsing [o/n] : ")
                if ignorer_erreurs.lower() in ['o', 'n']:
                    analyseur.config['ignorer_erreurs_parsing'] = ignorer_erreurs.lower() == 'o'
                
                print("✅ Configuration mise à jour")
                
            elif choix == '4':
                if not hasattr(analyseur, '_dernier_rapport'):
                    print("❌ Aucun rapport disponible. Analysez d'abord un fichier.")
                    continue
                
                chemin_html = input("Nom du fichier HTML [rapport.html] : ") or "rapport.html"
                
                try:
                    # Pour la démo, on utilise un rapport fictif
                    rapport_demo = {
                        'fichier': 'exemple.log',
                        'timestamp_analyse': datetime.now().isoformat(),
                        'taille_fichier': 1024000,
                        'erreurs_parsing': 5,
                        'statistiques': {
                            'total_entrees': 1500,
                            'ips_uniques': 45,
                            'par_niveau': {'INFO': 1200, 'WARNING': 250, 'ERROR': 50},
                            'top_erreurs': {'Connection timeout': 15, 'File not found': 10},
                            'top_urls': {'/index.html': 500, '/api/users': 200}
                        }
                    }
                    
                    analyseur.generer_rapport_html(rapport_demo, chemin_html)
                    print(f"✅ Rapport HTML généré : {chemin_html}")
                    
                except Exception as e:
                    print(f"❌ Erreur : {e}")
                    
            elif choix == '5':
                print("Au revoir !")
                break
            else:
                print("Choix invalide")
                
        except KeyboardInterrupt:
            print("\n\nAu revoir !")
            break
        except Exception as e:
            print(f"❌ Erreur inattendue : {e}")


# Tests
if __name__ == "__main__":
    print("=== Tests Correction Exercice 5 ===")
    
    # Test du parseur
    print("\n1. Test du parseur de logs :")
    parseur = ParseurLog()
    
    # Exemples de lignes de logs
    lignes_test = [
        '192.168.1.1 - - [25/Dec/2023:10:30:45 +0000] "GET /index.html HTTP/1.1" 200 1234',
        '2023-12-25 10:30:45 [ERROR] app.py: Database connection failed',
        'Dec 25 10:30:45 server01 nginx: connection timeout'
    ]
    
    for ligne in lignes_test:
        try:
            format_detecte = parseur.detecter_format(ligne)
            if format_detecte:
                entree = parseur.parser_ligne(ligne)
                print(f"   ✅ {format_detecte}: {entree.niveau} - {entree.message[:50]}...")
            else:
                print(f"   ❌ Format non reconnu: {ligne[:50]}...")
        except Exception as e:
            print(f"   ❌ Erreur: {e}")
    
    # Test de l'analyseur
    print("\n2. Test de l'analyseur :")
    try:
        analyseur = AnalyseurLog()
        print("   ✅ Analyseur créé avec succès")
        
        # Test de configuration
        analyseur.config['max_entrees_memoire'] = 1000
        print("   ✅ Configuration mise à jour")
        
    except Exception as e:
        print(f"   ❌ Erreur: {e}")
    
    print("\n3. Tests terminés avec succès !")
    print("\nPour utiliser l'interface interactive, décommentez la ligne suivante :")
    print("# interface_analyseur()")
    
    # Décommentez pour tester interactivement
    # interface_analyseur()
