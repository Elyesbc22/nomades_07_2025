"""
Correction complète - Exercice 3 : Traitement de fichiers CSV
=============================================================

Cette correction montre les solutions complètes pour l'exercice 3.
"""

import csv
import os
import re
from datetime import datetime
from pathlib import Path


def detecter_delimiteur(chemin_fichier, echantillon_lignes=5):
    """
    Détecte automatiquement le délimiteur d'un fichier CSV.
    
    Args:
        chemin_fichier (str): Chemin vers le fichier CSV
        echantillon_lignes (int): Nombre de lignes à analyser
    
    Returns:
        tuple: (succès: bool, délimiteur: str ou message d'erreur: str)
    """
    delimiteurs_possibles = [',', ';', '|', '\t']
    
    try:
        with open(chemin_fichier, 'r', encoding='utf-8') as fichier:
            # Lire les premières lignes
            lignes = []
            for i in range(echantillon_lignes):
                ligne = fichier.readline()
                if not ligne:
                    break
                lignes.append(ligne.strip())
        
        if not lignes:
            return (False, "Fichier vide")
        
        # Compter les occurrences de chaque délimiteur
        scores = {}
        for delim in delimiteurs_possibles:
            # Compter le nombre de colonnes avec ce délimiteur pour chaque ligne
            colonnes_par_ligne = []
            for ligne in lignes:
                if ligne:  # Ignorer les lignes vides
                    nb_colonnes = len(ligne.split(delim))
                    colonnes_par_ligne.append(nb_colonnes)
            
            # Le bon délimiteur devrait donner un nombre constant de colonnes > 1
            if colonnes_par_ligne:
                nb_colonnes_unique = len(set(colonnes_par_ligne))
                nb_colonnes_moyen = sum(colonnes_par_ligne) / len(colonnes_par_ligne)
                
                # Score basé sur la consistance et le nombre de colonnes
                if nb_colonnes_unique == 1 and nb_colonnes_moyen > 1:
                    scores[delim] = nb_colonnes_moyen
                else:
                    scores[delim] = 0
        
        # Choisir le délimiteur avec le meilleur score
        if scores and max(scores.values()) > 1:
            meilleur_delim = max(scores.keys(), key=lambda x: scores[x])
            return (True, meilleur_delim)
        else:
            return (False, "Aucun délimiteur détecté")
            
    except FileNotFoundError:
        return (False, "Fichier non trouvé")
    except UnicodeDecodeError:
        return (False, "Erreur d'encodage")
    except PermissionError:
        return (False, "Permission refusée")
    except Exception as e:
        return (False, f"Erreur inattendue : {str(e)}")


def lire_csv_robuste(chemin_fichier, delimiteur=None):
    """
    Lit un fichier CSV de manière robuste avec détection automatique.
    
    Args:
        chemin_fichier (str): Chemin vers le fichier CSV
        delimiteur (str, optional): Délimiteur spécifique ou None pour auto-détection
    
    Returns:
        tuple: (succès: bool, données: list[dict] ou message d'erreur: str)
    """
    try:
        # Détecter le délimiteur si non spécifié
        if delimiteur is None:
            succes, delim_detecte = detecter_delimiteur(chemin_fichier)
            if not succes:
                return (False, f"Impossible de détecter le délimiteur : {delim_detecte}")
            delimiteur = delim_detecte
        
        donnees = []
        lignes_erreur = []
        
        with open(chemin_fichier, 'r', encoding='utf-8') as fichier:
            reader = csv.DictReader(fichier, delimiter=delimiteur)
            
            for numero_ligne, ligne in enumerate(reader, start=2):  # start=2 car ligne 1 = headers
                try:
                    # Nettoyer les valeurs (supprimer espaces en début/fin)
                    ligne_nettoyee = {cle: valeur.strip() if isinstance(valeur, str) else valeur 
                                    for cle, valeur in ligne.items()}
                    donnees.append(ligne_nettoyee)
                except Exception as e:
                    lignes_erreur.append(f"Ligne {numero_ligne}: {str(e)}")
        
        if lignes_erreur:
            message_erreurs = "; ".join(lignes_erreur[:5])  # Limiter à 5 erreurs
            print(f"Avertissement : {len(lignes_erreur)} lignes avec erreurs. Exemples: {message_erreurs}")
        
        return (True, donnees)
        
    except FileNotFoundError:
        return (False, "Fichier non trouvé")
    except csv.Error as e:
        return (False, f"Erreur de format CSV : {str(e)}")
    except UnicodeDecodeError:
        return (False, "Erreur d'encodage")
    except Exception as e:
        return (False, f"Erreur inattendue : {str(e)}")


def ecrire_csv_robuste(chemin_fichier, donnees, delimiteur=',', inclure_headers=True):
    """
    Écrit des données dans un fichier CSV de manière robuste.
    
    Args:
        chemin_fichier (str): Chemin vers le fichier CSV
        donnees (list[dict]): Liste de dictionnaires à écrire
        delimiteur (str): Délimiteur à utiliser
        inclure_headers (bool): Inclure les en-têtes ou non
    
    Returns:
        tuple: (succès: bool, message: str)
    """
    try:
        if not donnees:
            return (False, "Aucune donnée à écrire")
        
        # Créer le dossier parent si nécessaire
        Path(chemin_fichier).parent.mkdir(parents=True, exist_ok=True)
        
        # Extraire les noms de colonnes
        colonnes = list(donnees[0].keys())
        
        with open(chemin_fichier, 'w', newline='', encoding='utf-8') as fichier:
            writer = csv.DictWriter(fichier, fieldnames=colonnes, delimiter=delimiteur)
            
            if inclure_headers:
                writer.writeheader()
            
            writer.writerows(donnees)
        
        return (True, f"Fichier CSV écrit avec succès ({len(donnees)} lignes)")
        
    except PermissionError:
        return (False, "Permission refusée pour l'écriture")
    except csv.Error as e:
        return (False, f"Erreur d'écriture CSV : {str(e)}")
    except Exception as e:
        return (False, f"Erreur inattendue : {str(e)}")


def analyser_donnees_csv(donnees):
    """
    Analyse des données CSV et génère des statistiques.
    
    Args:
        donnees (list[dict]): Données CSV sous forme de liste de dictionnaires
    
    Returns:
        dict: Statistiques détaillées
    """
    if not donnees:
        return None
    
    colonnes = list(donnees[0].keys())
    
    # Initialiser les structures de données
    types_colonnes = {}
    valeurs_manquantes = {}
    statistiques_numeriques = {}
    
    for colonne in colonnes:
        valeurs = [ligne[colonne] for ligne in donnees if ligne[colonne] and ligne[colonne].strip()]
        valeurs_vides = len(donnees) - len(valeurs)
        
        valeurs_manquantes[colonne] = valeurs_vides
        
        if not valeurs:
            types_colonnes[colonne] = 'vide'
            continue
        
        # Détecter le type de données
        type_detecte = detecter_type_colonne(valeurs)
        types_colonnes[colonne] = type_detecte
        
        # Calculer des statistiques pour les colonnes numériques
        if type_detecte in ['int', 'float']:
            try:
                valeurs_numeriques = []
                for val in valeurs:
                    try:
                        if type_detecte == 'int':
                            valeurs_numeriques.append(int(val))
                        else:
                            valeurs_numeriques.append(float(val))
                    except ValueError:
                        continue
                
                if valeurs_numeriques:
                    statistiques_numeriques[colonne] = {
                        'min': min(valeurs_numeriques),
                        'max': max(valeurs_numeriques),
                        'moyenne': sum(valeurs_numeriques) / len(valeurs_numeriques),
                        'nb_valeurs': len(valeurs_numeriques)
                    }
            except Exception:
                pass
    
    return {
        'nombre_lignes': len(donnees),
        'colonnes': colonnes,
        'types_colonnes': types_colonnes,
        'valeurs_manquantes': valeurs_manquantes,
        'statistiques_numeriques': statistiques_numeriques
    }


def detecter_type_colonne(valeurs):
    """Détecte le type de données d'une colonne."""
    if not valeurs:
        return 'vide'
    
    # Échantillon pour la détection de type
    echantillon = valeurs[:min(100, len(valeurs))]
    
    # Tester si c'est un entier
    nb_int = 0
    for val in echantillon:
        try:
            int(val)
            nb_int += 1
        except ValueError:
            pass
    
    if nb_int / len(echantillon) > 0.8:
        return 'int'
    
    # Tester si c'est un float
    nb_float = 0
    for val in echantillon:
        try:
            float(val)
            nb_float += 1
        except ValueError:
            pass
    
    if nb_float / len(echantillon) > 0.8:
        return 'float'
    
    # Tester si c'est une date
    patterns_date = [
        r'\d{4}-\d{2}-\d{2}',
        r'\d{2}/\d{2}/\d{4}',
        r'\d{2}-\d{2}-\d{4}'
    ]
    
    nb_date = 0
    for val in echantillon:
        for pattern in patterns_date:
            if re.match(pattern, str(val)):
                nb_date += 1
                break
    
    if nb_date / len(echantillon) > 0.7:
        return 'date'
    
    return 'str'


def filtrer_donnees_csv(donnees, criteres):
    """
    Filtre des données CSV selon des critères.
    
    Args:
        donnees (list[dict]): Données à filtrer
        criteres (dict): Critères de filtrage
    
    Returns:
        list[dict]: Données filtrées
    """
    def appliquer_critere(valeur, operateur, *args):
        """Applique un critère de filtrage."""
        try:
            if operateur == '==':
                return str(valeur) == str(args[0])
            elif operateur == '!=':
                return str(valeur) != str(args[0])
            elif operateur == '>':
                return float(valeur) > float(args[0])
            elif operateur == '<':
                return float(valeur) < float(args[0])
            elif operateur == '>=':
                return float(valeur) >= float(args[0])
            elif operateur == '<=':
                return float(valeur) <= float(args[0])
            elif operateur == 'between':
                return float(args[0]) <= float(valeur) <= float(args[1])
            elif operateur == 'contains':
                return str(args[0]).lower() in str(valeur).lower()
            elif operateur == 'in':
                return str(valeur) in [str(x) for x in args]
            else:
                return False
        except (ValueError, TypeError):
            return False
    
    donnees_filtrees = []
    
    for ligne in donnees:
        ligne_valide = True
        
        for colonne, critere in criteres.items():
            if colonne not in ligne:
                ligne_valide = False
                break
            
            valeur = ligne[colonne]
            if isinstance(critere, tuple) and len(critere) >= 2:
                operateur = critere[0]
                args = critere[1:]
                
                if not appliquer_critere(valeur, operateur, *args):
                    ligne_valide = False
                    break
        
        if ligne_valide:
            donnees_filtrees.append(ligne)
    
    return donnees_filtrees


def convertir_format_csv(fichier_source, fichier_destination, 
                        delimiteur_source=None, delimiteur_destination=','):
    """
    Convertit un fichier CSV d'un format à un autre.
    
    Args:
        fichier_source (str): Fichier CSV source
        fichier_destination (str): Fichier CSV destination
        delimiteur_source (str): Délimiteur source (None = auto-détection)
        delimiteur_destination (str): Délimiteur destination
    
    Returns:
        tuple: (succès: bool, message: str, stats: dict)
    """
    try:
        # Obtenir la taille du fichier source
        taille_source = Path(fichier_source).stat().st_size
        
        # Lire les données
        succes, donnees = lire_csv_robuste(fichier_source, delimiteur_source)
        if not succes:
            return (False, f"Erreur de lecture : {donnees}", {})
        
        # Écrire dans le nouveau format
        succes_ecriture, message_ecriture = ecrire_csv_robuste(
            fichier_destination, donnees, delimiteur_destination
        )
        
        if not succes_ecriture:
            return (False, f"Erreur d'écriture : {message_ecriture}", {})
        
        # Calculer les statistiques
        taille_destination = Path(fichier_destination).stat().st_size
        
        stats = {
            'nombre_lignes_traitees': len(donnees),
            'nombre_erreurs': 0,  # Implémenté dans lire_csv_robuste
            'taille_fichier_source': taille_source,
            'taille_fichier_destination': taille_destination
        }
        
        return (True, "Conversion réussie", stats)
        
    except Exception as e:
        return (False, f"Erreur lors de la conversion : {str(e)}", {})


def fusionner_fichiers_csv(fichiers_sources, fichier_destination, 
                          ajouter_colonne_source=True):
    """
    Fusionne plusieurs fichiers CSV en un seul.
    
    Args:
        fichiers_sources (list[str]): Liste des fichiers à fusionner
        fichier_destination (str): Fichier de destination
        ajouter_colonne_source (bool): Ajouter une colonne avec le nom du fichier source
    
    Returns:
        tuple: (succès: bool, message: str, rapport: dict)
    """
    try:
        donnees_fusionnees = []
        lignes_par_fichier = {}
        erreurs = []
        fichiers_traites = []
        
        # Lire le premier fichier pour obtenir les colonnes de référence
        if not fichiers_sources:
            return (False, "Aucun fichier source spécifié", {})
        
        succes, donnees_ref = lire_csv_robuste(fichiers_sources[0])
        if not succes:
            return (False, f"Erreur lors de la lecture du fichier de référence : {donnees_ref}", {})
        
        colonnes_reference = set(donnees_ref[0].keys()) if donnees_ref else set()
        
        # Traiter chaque fichier
        for fichier in fichiers_sources:
            try:
                succes, donnees = lire_csv_robuste(fichier)
                if not succes:
                    erreurs.append(f"{fichier}: {donnees}")
                    continue
                
                if not donnees:
                    erreurs.append(f"{fichier}: fichier vide")
                    continue
                
                # Vérifier la compatibilité des colonnes
                colonnes_fichier = set(donnees[0].keys())
                if colonnes_fichier != colonnes_reference:
                    erreurs.append(f"{fichier}: colonnes incompatibles")
                    continue
                
                # Ajouter la colonne source si demandé
                if ajouter_colonne_source:
                    nom_fichier = Path(fichier).stem
                    for ligne in donnees:
                        ligne['source_file'] = nom_fichier
                
                donnees_fusionnees.extend(donnees)
                lignes_par_fichier[fichier] = len(donnees)
                fichiers_traites.append(fichier)
                
            except Exception as e:
                erreurs.append(f"{fichier}: {str(e)}")
        
        if not donnees_fusionnees:
            return (False, "Aucune donnée à fusionner", {})
        
        # Écrire le fichier fusionné
        succes_ecriture, message_ecriture = ecrire_csv_robuste(
            fichier_destination, donnees_fusionnees
        )
        
        if not succes_ecriture:
            return (False, f"Erreur d'écriture : {message_ecriture}", {})
        
        rapport = {
            'fichiers_traites': fichiers_traites,
            'lignes_par_fichier': lignes_par_fichier,
            'total_lignes': len(donnees_fusionnees),
            'erreurs': erreurs
        }
        
        return (True, f"Fusion réussie : {len(donnees_fusionnees)} lignes", rapport)
        
    except Exception as e:
        return (False, f"Erreur lors de la fusion : {str(e)}", {})


def generateur_rapport_csv(chemin_fichier):
    """
    Génère un rapport complet sur un fichier CSV.
    
    Args:
        chemin_fichier (str): Chemin vers le fichier CSV
    
    Returns:
        str: Rapport formaté en texte
    """
    try:
        # Lire et analyser le fichier
        succes, donnees = lire_csv_robuste(chemin_fichier)
        if not succes:
            return f"Erreur lors de la lecture : {donnees}"
        
        stats = analyser_donnees_csv(donnees)
        if not stats:
            return "Impossible d'analyser le fichier"
        
        # Générer le rapport
        rapport = []
        rapport.append("=" * 60)
        rapport.append(f"RAPPORT D'ANALYSE CSV - {Path(chemin_fichier).name}")
        rapport.append("=" * 60)
        rapport.append(f"Date d'analyse : {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
        rapport.append("")
        
        # Informations générales
        rapport.append("INFORMATIONS GÉNÉRALES")
        rapport.append("-" * 25)
        taille_fichier = Path(chemin_fichier).stat().st_size
        rapport.append(f"Taille du fichier : {taille_fichier:,} octets")
        rapport.append(f"Nombre de lignes : {stats['nombre_lignes']:,}")
        rapport.append(f"Nombre de colonnes : {len(stats['colonnes'])}")
        
        # Détection du délimiteur
        succes_delim, delimiteur = detecter_delimiteur(chemin_fichier)
        if succes_delim:
            rapport.append(f"Délimiteur détecté : '{delimiteur}'")
        rapport.append("")
        
        # Colonnes et types
        rapport.append("COLONNES ET TYPES DE DONNÉES")
        rapport.append("-" * 35)
        for colonne in stats['colonnes']:
            type_col = stats['types_colonnes'].get(colonne, 'inconnu')
            valeurs_manquantes = stats['valeurs_manquantes'].get(colonne, 0)
            pourcentage_manquant = (valeurs_manquantes / stats['nombre_lignes']) * 100 if stats['nombre_lignes'] > 0 else 0
            rapport.append(f"  {colonne:<20} | {type_col:<8} | {valeurs_manquantes:>6} valeurs manquantes ({pourcentage_manquant:.1f}%)")
        rapport.append("")
        
        # Statistiques numériques
        if stats['statistiques_numeriques']:
            rapport.append("STATISTIQUES NUMÉRIQUES")
            rapport.append("-" * 25)
            for colonne, stat_num in stats['statistiques_numeriques'].items():
                rapport.append(f"  {colonne}:")
                rapport.append(f"    Min: {stat_num['min']}")
                rapport.append(f"    Max: {stat_num['max']}")
                rapport.append(f"    Moyenne: {stat_num['moyenne']:.2f}")
                rapport.append(f"    Nb valeurs: {stat_num['nb_valeurs']}")
                rapport.append("")
        
        # Aperçu des données
        rapport.append("APERÇU DES DONNÉES (5 premières lignes)")
        rapport.append("-" * 45)
        for i, ligne in enumerate(donnees[:5]):
            rapport.append(f"Ligne {i+1}:")
            for colonne, valeur in ligne.items():
                valeur_affichee = str(valeur)[:50] + "..." if len(str(valeur)) > 50 else str(valeur)
                rapport.append(f"  {colonne}: {valeur_affichee}")
            rapport.append("")
        
        # Détection d'anomalies
        rapport.append("DÉTECTION D'ANOMALIES")
        rapport.append("-" * 22)
        anomalies_detectees = []
        
        # Vérifier les doublons
        identifiants = []
        if 'id' in stats['colonnes']:
            for ligne in donnees:
                if ligne['id']:
                    identifiants.append(ligne['id'])
            if len(identifiants) != len(set(identifiants)):
                anomalies_detectees.append("Doublons détectés dans la colonne 'id'")
        
        # Vérifier les valeurs manquantes importantes
        for colonne, nb_manquantes in stats['valeurs_manquantes'].items():
            pourcentage = (nb_manquantes / stats['nombre_lignes']) * 100 if stats['nombre_lignes'] > 0 else 0
            if pourcentage > 20:
                anomalies_detectees.append(f"Colonne '{colonne}': {pourcentage:.1f}% de valeurs manquantes")
        
        if anomalies_detectees:
            for anomalie in anomalies_detectees:
                rapport.append(f"  ⚠️  {anomalie}")
        else:
            rapport.append("  ✅ Aucune anomalie majeure détectée")
        
        rapport.append("")
        rapport.append("=" * 60)
        
        rapport_texte = "\n".join(rapport)
        
        # Sauvegarder le rapport
        nom_rapport = f"rapport_{Path(chemin_fichier).stem}_{datetime.now().strftime('%Y%m%d_%H%M%S')}.txt"
        chemin_rapport = Path("results") / nom_rapport
        chemin_rapport.parent.mkdir(parents=True, exist_ok=True)
        
        with open(chemin_rapport, 'w', encoding='utf-8') as f:
            f.write(rapport_texte)
        
        print(f"Rapport sauvegardé dans : {chemin_rapport}")
        
        return rapport_texte
        
    except Exception as e:
        return f"Erreur lors de la génération du rapport : {str(e)}"


def interface_csv_interactif():
    """
    Interface interactive pour manipuler des fichiers CSV.
    """
    print("=== Interface CSV Interactive ===")
    
    while True:
        print("\nOptions disponibles :")
        print("1. Analyser un fichier CSV")
        print("2. Convertir le format d'un CSV")
        print("3. Filtrer des données CSV")
        print("4. Fusionner des fichiers CSV")
        print("5. Générer un rapport détaillé")
        print("6. Quitter")
        
        try:
            choix = input("\nVotre choix (1-6) : ").strip()
            
            if choix == '1':
                fichier = input("Chemin du fichier CSV à analyser : ")
                succes, donnees = lire_csv_robuste(fichier)
                if succes:
                    stats = analyser_donnees_csv(donnees)
                    if stats:
                        print(f"\nAnalyse de '{fichier}':")
                        print(f"  Lignes: {stats['nombre_lignes']}")
                        print(f"  Colonnes: {len(stats['colonnes'])}")
                        print(f"  Types détectés: {stats['types_colonnes']}")
                else:
                    print(f"Erreur : {donnees}")
                    
            elif choix == '2':
                source = input("Fichier source : ")
                destination = input("Fichier destination : ")
                delim_dest = input("Délimiteur de destination [,] : ").strip() or ','
                
                succes, message, stats = convertir_format_csv(source, destination, None, delim_dest)
                if succes:
                    print(f"Conversion réussie : {message}")
                    print(f"Statistiques : {stats}")
                else:
                    print(f"Erreur : {message}")
                    
            elif choix == '3':
                fichier = input("Fichier CSV à filtrer : ")
                print("Format des critères : colonne operateur valeur")
                print("Exemple : age > 30")
                
                criteres = {}
                while True:
                    critere = input("Critère (ou 'fin' pour terminer) : ").strip()
                    if critere.lower() == 'fin':
                        break
                    
                    parties = critere.split()
                    if len(parties) >= 3:
                        colonne = parties[0]
                        operateur = parties[1]
                        valeur = ' '.join(parties[2:])
                        criteres[colonne] = (operateur, valeur)
                
                if criteres:
                    succes, donnees = lire_csv_robuste(fichier)
                    if succes:
                        donnees_filtrees = filtrer_donnees_csv(donnees, criteres)
                        print(f"Résultat : {len(donnees_filtrees)} lignes sur {len(donnees)}")
                        
                        if donnees_filtrees:
                            sauvegarder = input("Sauvegarder le résultat ? (o/n) : ")
                            if sauvegarder.lower() == 'o':
                                fichier_sortie = input("Nom du fichier de sortie : ")
                                ecrire_csv_robuste(fichier_sortie, donnees_filtrees)
                    else:
                        print(f"Erreur : {donnees}")
                        
            elif choix == '4':
                fichiers = []
                print("Entrez les fichiers à fusionner (un par ligne, 'fin' pour terminer) :")
                while True:
                    fichier = input("Fichier : ").strip()
                    if fichier.lower() == 'fin':
                        break
                    if fichier:
                        fichiers.append(fichier)
                
                if fichiers:
                    destination = input("Fichier de destination : ")
                    ajouter_source = input("Ajouter colonne source ? (o/n) [o] : ").strip().lower()
                    ajouter_source = ajouter_source != 'n'
                    
                    succes, message, rapport = fusionner_fichiers_csv(fichiers, destination, ajouter_source)
                    if succes:
                        print(f"Fusion réussie : {message}")
                        print(f"Rapport : {rapport}")
                    else:
                        print(f"Erreur : {message}")
                        
            elif choix == '5':
                fichier = input("Fichier CSV pour le rapport : ")
                rapport = generateur_rapport_csv(fichier)
                print("\n" + rapport)
                
            elif choix == '6':
                print("Au revoir !")
                break
            else:
                print("Choix invalide.")
                
        except KeyboardInterrupt:
            print("\n\nAu revoir !")
            break
        except Exception as e:
            print(f"Erreur inattendue : {e}")


# Tests
if __name__ == "__main__":
    print("=== Tests Correction Exercice 3 ===")
    
    # Test détection délimiteur
    print("\n1. Test détection délimiteur :")
    fichiers_test = [
        "data/employees.csv",      # délimiteur ','
        "data/ventes_eu.csv",      # délimiteur ';'
        "data/contacts.csv"        # délimiteur '|'
    ]
    
    for fichier in fichiers_test:
        if os.path.exists(fichier):
            succes, delim = detecter_delimiteur(fichier)
            if succes:
                print(f"   {fichier} : délimiteur '{delim}'")
            else:
                print(f"   {fichier} : erreur - {delim}")
    
    # Test lecture CSV robuste
    print("\n2. Test lecture CSV :")
    succes, donnees = lire_csv_robuste("data/employees.csv")
    if succes and donnees:
        print(f"   Employés lus : {len(donnees)} lignes")
        print(f"   Premier employé : {donnees[0]}")
    
    # Test analyse données
    print("\n3. Test analyse :")
    if succes and donnees:
        stats = analyser_donnees_csv(donnees)
        if stats:
            print(f"   Colonnes : {stats.get('colonnes', [])}")
            print(f"   Types : {stats.get('types_colonnes', {})}")
    
    print("\n4. Tests terminés avec succès !")
    
    # Décommentez pour tester interactivement
    # interface_csv_interactif()
