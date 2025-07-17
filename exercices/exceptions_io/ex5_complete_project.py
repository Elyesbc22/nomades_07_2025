"""
Exercice 5 : Projet complet - Gestionnaire de fichiers de logs
==============================================================

Objectifs :
- Intégrer toutes les notions vues
- Créer un système complet avec exceptions et file I/O
- Manipuler des données complexes
- Générer des rapports et visualisations

Description du projet :
Vous devez créer un système d'analyse de fichiers de logs d'un serveur web.
Le système doit pouvoir lire différents formats de logs, les analyser,
détecter des anomalies et générer des rapports.

Structure attendue :
- Gestion robuste des erreurs
- Lecture de fichiers de logs volumineux
- Analyse statistique des données
- Détection d'attaques potentielles
- Génération de rapports CSV et graphiques
"""

import re
import csv
import json
import os
from datetime import datetime, timedelta
from pathlib import Path
from collections import defaultdict, Counter

try:
    import matplotlib.pyplot as plt
except ImportError:
    plt = None


# ========================
# EXCEPTIONS PERSONNALISÉES
# ========================

class LogAnalyzerError(Exception):
    """Exception de base pour l'analyseur de logs."""
    pass


class LogFormatError(LogAnalyzerError):
    """Erreur de format de log."""
    pass


class LogFileError(LogAnalyzerError):
    """Erreur de fichier de log."""
    pass


class ConfigurationError(LogAnalyzerError):
    """Erreur de configuration."""
    pass


# ========================
# CLASSES PRINCIPALES
# ========================

class LogEntry:
    """Représente une entrée de log."""
    
    def __init__(self, timestamp, ip, method, url, status_code, size, user_agent=""):
        # TODO: Validez et assignez les attributs
        # Contraintes :
        # - timestamp : datetime valide
        # - ip : format IP valide (xxx.xxx.xxx.xxx)
        # - method : GET, POST, PUT, DELETE, etc.
        # - status_code : entier entre 100 et 599
        # - size : entier >= 0
        pass
    
    def is_error(self):
        """Vérifie si l'entrée représente une erreur (status >= 400)."""
        # TODO: Implémentez cette méthode
        pass
    
    def is_suspicious(self):
        """Détecte des patterns suspects dans la requête."""
        # TODO: Implémentez la détection de patterns suspects :
        # - SQL injection (SELECT, UNION, DROP, etc.)
        # - XSS (<script>, javascript:, etc.)
        # - Path traversal (../, etc.)
        # - Tentatives de force brute (login, admin, etc.)
        pass
    
    def to_dict(self):
        """Convertit l'entrée en dictionnaire."""
        # TODO: Implémentez cette méthode
        pass


class LogParser:
    """Parse différents formats de logs."""
    
    # Formats de logs supportés
    FORMATS = {
        'apache_common': r'(\S+) \S+ \S+ \[(.*?)\] "(\S+) (\S+) \S+" (\d+) (\d+|-)',
        'nginx': r'(\S+) - - \[(.*?)\] "(\S+) (\S+) \S+" (\d+) (\d+) "(.*?)" "(.*?)"',
        'custom': r'(\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2}) - (\S+) - (\S+) (\S+) - (\d+) - (\d+)'
    }
    
    def __init__(self, log_format='apache_common'):
        if log_format not in self.FORMATS:
            raise ConfigurationError(f"Format '{log_format}' non supporté")
        
        self.format = log_format
        self.pattern = re.compile(self.FORMATS[log_format])
    
    def parse_line(self, line):
        """
        Parse une ligne de log.
        
        Args:
            line (str): Ligne de log à parser
        
        Returns:
            LogEntry: Entrée de log parsée
        
        Raises:
            LogFormatError: Si le format est invalide
        """
        # TODO: Implémentez le parsing
        # Gérez les différents formats de date
        # Convertissez les types appropriés
        pass
    
    def detect_format(self, sample_lines):
        """
        Détecte automatiquement le format d'un échantillon de lignes.
        
        Args:
            sample_lines (list[str]): Échantillon de lignes
        
        Returns:
            str: Format détecté
        
        Raises:
            LogFormatError: Si aucun format n'est reconnu
        """
        # TODO: Implémentez la détection automatique
        pass


class LogAnalyzer:
    """Analyseur principal de logs."""
    
    def __init__(self, config_file="config/analyzer_config.json"):
        self.config = self.load_config(config_file)
        self.entries = []
        self.statistics = {}
        self.anomalies = []
    
    def load_config(self, config_file):
        """
        Charge la configuration depuis un fichier JSON.
        
        Configuration attendue :
        {
            "max_file_size_mb": 100,
            "suspicious_patterns": [...],
            "alert_thresholds": {
                "error_rate": 0.05,
                "unique_ips_per_minute": 100
            },
            "output_formats": ["csv", "json", "html"]
        }
        """
        default_config = {
            "max_file_size_mb": 100,
            "suspicious_patterns": [
                "SELECT.*FROM", "UNION.*SELECT", "DROP.*TABLE",
                "<script", "javascript:", "../"
            ],
            "alert_thresholds": {
                "error_rate": 0.05,
                "unique_ips_per_minute": 100
            },
            "output_formats": ["csv", "json"]
        }
        
        try:
            # TODO: Chargez la config depuis le fichier ou utilisez la config par défaut
            # Créez le fichier de config par défaut s'il n'existe pas
            pass
        except Exception as e:
            raise ConfigurationError(f"Erreur de configuration : {e}")
    
    def analyze_file(self, file_path, log_format=None):
        """
        Analyse un fichier de log complet.
        
        Args:
            file_path (str): Chemin vers le fichier de log
            log_format (str): Format des logs ou None pour auto-détection
        
        Raises:
            LogFileError: En cas d'erreur de fichier
            LogFormatError: En cas d'erreur de format
        """
        # TODO: Implémentez l'analyse complète
        # 1. Vérifiez la taille du fichier
        # 2. Détectez le format si nécessaire
        # 3. Parsez toutes les lignes
        # 4. Calculez les statistiques
        # 5. Détectez les anomalies
        pass
    
    def calculate_statistics(self):
        """
        Calcule des statistiques détaillées sur les logs.
        
        Statistiques à calculer :
        - Nombre total de requêtes
        - Répartition par code de statut
        - Top 10 des IPs
        - Top 10 des URLs
        - Répartition par méthode HTTP
        - Trafic par heure/jour
        - Taille moyenne des réponses
        - Taux d'erreur
        """
        # TODO: Implémentez le calcul des statistiques
        pass
    
    def detect_anomalies(self):
        """
        Détecte des anomalies dans les logs.
        
        Anomalies à détecter :
        - Pics de trafic inhabituels
        - Taux d'erreur élevé
        - Activité suspecte (patterns d'attaque)
        - IPs avec trop de requêtes
        - Tentatives de force brute
        """
        # TODO: Implémentez la détection d'anomalies
        pass
    
    def generate_report(self, output_dir="results"):
        """
        Génère des rapports dans différents formats.
        
        Args:
            output_dir (str): Dossier de sortie
        
        Rapports générés :
        - Rapport texte détaillé
        - Fichier CSV avec toutes les entrées
        - Fichier JSON avec les statistiques
        - Graphiques (si matplotlib disponible)
        """
        Path(output_dir).mkdir(parents=True, exist_ok=True)
        
        try:
            # TODO: Générez les différents rapports
            # 1. Rapport texte
            # 2. Export CSV
            # 3. Export JSON
            # 4. Graphiques
            pass
        except Exception as e:
            raise LogAnalyzerError(f"Erreur lors de la génération du rapport : {e}")
    
    def generate_graphs(self, output_dir):
        """
        Génère des graphiques d'analyse.
        
        Graphiques à générer :
        - Évolution du trafic dans le temps
        - Répartition des codes de statut
        - Top 10 des IPs
        - Répartition par méthode HTTP
        """
        try:
            # TODO: Implémentez la génération de graphiques
            # Utilisez matplotlib pour créer des visualisations
            pass
        except ImportError:
            print("Matplotlib non disponible, génération de graphiques ignorée")
        except Exception as e:
            print(f"Erreur lors de la génération des graphiques : {e}")


class LogMonitor:
    """Monitore des fichiers de logs en temps réel."""
    
    def __init__(self, log_analyzer):
        self.analyzer = log_analyzer
        self.watched_files = {}
        
    def watch_file(self, file_path, callback=None):
        """
        Surveille un fichier de log pour les nouvelles entrées.
        
        Args:
            file_path (str): Fichier à surveiller
            callback (function): Fonction appelée pour chaque nouvelle entrée
        """
        # TODO: Implémentez la surveillance de fichier
        # Utilisez la position du fichier pour détecter les nouvelles lignes
        pass
    
    def start_monitoring(self, interval=5):
        """
        Démarre la surveillance en continu.
        
        Args:
            interval (int): Intervalle de vérification en secondes
        """
        # TODO: Implémentez la boucle de surveillance
        pass


# ========================
# INTERFACE UTILISATEUR
# ========================

def create_sample_logs():
    """Crée des fichiers de logs d'exemple pour les tests."""
    sample_data = [
        '192.168.1.100 - - [25/Dec/2023:10:00:00 +0000] "GET /index.html HTTP/1.1" 200 1234',
        '10.0.0.50 - - [25/Dec/2023:10:00:01 +0000] "POST /login HTTP/1.1" 401 567',
        '192.168.1.100 - - [25/Dec/2023:10:00:02 +0000] "GET /admin HTTP/1.1" 403 890',
        '203.0.113.0 - - [25/Dec/2023:10:00:03 +0000] "GET /index.php?id=1\' OR 1=1-- HTTP/1.1" 200 2345',
        '192.168.1.200 - - [25/Dec/2023:10:00:04 +0000] "GET /images/logo.png HTTP/1.1" 200 5678',
    ]
    
    os.makedirs("data", exist_ok=True)
    with open("data/sample_access.log", "w") as f:
        f.write("\n".join(sample_data))
    
    print("Fichiers de logs d'exemple créés dans data/")


def interface_log_analyzer():
    """Interface interactive pour l'analyseur de logs."""
    print("=== Analyseur de Logs ===")
    
    try:
        analyzer = LogAnalyzer()
        monitor = LogMonitor(analyzer)
        
        while True:
            print("\nOptions disponibles :")
            print("1. Analyser un fichier de log")
            print("2. Créer des logs d'exemple")
            print("3. Générer un rapport")
            print("4. Surveiller un fichier en temps réel")
            print("5. Configurer l'analyseur")
            print("6. Quitter")
            
            choix = input("\nVotre choix (1-6) : ").strip()
            
            if choix == '1':
                # TODO: Implémentez l'analyse de fichier
                pass
            elif choix == '2':
                create_sample_logs()
            elif choix == '3':
                # TODO: Implémentez la génération de rapport
                pass
            elif choix == '4':
                # TODO: Implémentez la surveillance
                pass
            elif choix == '5':
                # TODO: Implémentez la configuration
                pass
            elif choix == '6':
                print("Au revoir !")
                break
            else:
                print("Choix invalide.")
                
    except Exception as e:
        print(f"Erreur : {e}")


# Tests
if __name__ == "__main__":
    print("=== Tests Exercice 5 ===")
    
    try:
        # Test création des logs d'exemple
        create_sample_logs()
        
        # Test parser
        print("\n1. Test du parser :")
        parser = LogParser('apache_common')
        test_line = '192.168.1.100 - - [25/Dec/2023:10:00:00 +0000] "GET /index.html HTTP/1.1" 200 1234'
        
        try:
            entry = parser.parse_line(test_line)
            if entry:
                print(f"   Ligne parsée : IP={entry.ip}, URL={entry.url}")
        except Exception as e:
            print(f"   Erreur de parsing : {e}")
        
        # Test analyzer
        print("\n2. Test de l'analyzeur :")
        analyzer = LogAnalyzer()
        
        # Analyser le fichier d'exemple
        try:
            analyzer.analyze_file("data/sample_access.log")
            print(f"   Nombre d'entrées analysées : {len(analyzer.entries)}")
        except Exception as e:
            print(f"   Erreur d'analyse : {e}")
        
        print("\n3. Tests terminés !")
        
    except Exception as e:
        print(f"Erreur lors des tests : {e}")
    
    # Décommentez pour tester interactivement
    # interface_log_analyzer()
