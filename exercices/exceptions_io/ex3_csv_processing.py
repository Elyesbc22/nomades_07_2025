"""
Exercice 3 : Traitement de fichiers CSV
=======================================

Objectifs :
- Lire et écrire des fichiers CSV
- Gérer différents délimiteurs et dialectes
- Traiter et analyser des données CSV
- Gérer les erreurs de format et de données

Instructions :
Complétez les fonctions ci-dessous pour manipuler des fichiers CSV.
"""

import csv
import os
from datetime import datetime


def detecter_delimiteur(chemin_fichier, echantillon_lignes=5):
    """
    Détecte automatiquement le délimiteur d'un fichier CSV.
    
    Args:
        chemin_fichier (str): Chemin vers le fichier CSV
        echantillon_lignes (int): Nombre de lignes à analyser
    
    Returns:
        tuple: (succès: bool, délimiteur: str ou message d'erreur: str)
        
    Délimiteurs à tester : ',', ';', '|', '\t'
    
    Exceptions à gérer :
    - FileNotFoundError
    - UnicodeDecodeError
    - PermissionError
    """
    delimiteurs_possibles = [',', ';', '|', '\t']
    
    # TODO: Implémentez la détection automatique du délimiteur
    pass


def lire_csv_robuste(chemin_fichier, delimiteur=None):
    """
    Lit un fichier CSV de manière robuste avec détection automatique.
    
    Args:
        chemin_fichier (str): Chemin vers le fichier CSV
        delimiteur (str, optional): Délimiteur spécifique ou None pour auto-détection
    
    Returns:
        tuple: (succès: bool, données: list[dict] ou message d'erreur: str)
        
    La fonction doit :
    1. Détecter le délimiteur si non spécifié
    2. Lire toutes les lignes
    3. Gérer les lignes malformées
    4. Retourner une liste de dictionnaires
    
    Exceptions à gérer :
    - Toutes les exceptions de fichier
    - csv.Error pour les erreurs de format CSV
    """
    # TODO: Implémentez cette fonction
    pass


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
        
    Créez le dossier parent si nécessaire.
    Gérez les erreurs d'écriture et d'encodage.
    """
    # TODO: Implémentez cette fonction
    pass


def analyser_donnees_csv(donnees):
    """
    Analyse des données CSV et génère des statistiques.
    
    Args:
        donnees (list[dict]): Données CSV sous forme de liste de dictionnaires
    
    Returns:
        dict: Statistiques détaillées
        {
            'nombre_lignes': int,
            'colonnes': list[str],
            'types_colonnes': dict,  # {colonne: type_detecte}
            'valeurs_manquantes': dict,  # {colonne: nombre}
            'statistiques_numeriques': dict  # pour les colonnes numériques
        }
    
    Détectez automatiquement les types de données (int, float, date, str).
    """
    # TODO: Implémentez cette fonction
    pass


def filtrer_donnees_csv(donnees, criteres):
    """
    Filtre des données CSV selon des critères.
    
    Args:
        donnees (list[dict]): Données à filtrer
        criteres (dict): Critères de filtrage
            Exemples :
            - {'age': ('>', 30)} : âge > 30
            - {'ville': ('==', 'Paris')} : ville == 'Paris'
            - {'salaire': ('between', 3000, 4000)} : salaire entre 3000 et 4000
            - {'nom': ('contains', 'Martin')} : nom contient 'Martin'
    
    Returns:
        list[dict]: Données filtrées
        
    Opérateurs supportés : '==', '!=', '>', '<', '>=', '<=', 'between', 'contains', 'in'
    """
    # TODO: Implémentez cette fonction
    pass


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
        
    Stats retournées :
    - nombre_lignes_traitees
    - nombre_erreurs
    - taille_fichier_source
    - taille_fichier_destination
    """
    # TODO: Implémentez cette fonction
    pass


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
        
    La fonction doit :
    1. Vérifier que tous les fichiers ont les mêmes colonnes
    2. Fusionner les données
    3. Optionnellement ajouter une colonne 'source_file'
    4. Gérer les conflits de format
    
    Rapport retourné :
    - fichiers_traites: list[str]
    - lignes_par_fichier: dict
    - total_lignes: int
    - erreurs: list[str]
    """
    # TODO: Implémentez cette fonction
    pass


def generateur_rapport_csv(chemin_fichier):
    """
    Génère un rapport complet sur un fichier CSV.
    
    Args:
        chemin_fichier (str): Chemin vers le fichier CSV
    
    Returns:
        str: Rapport formaté en texte
        
    Le rapport doit inclure :
    - Informations générales (taille, nombre de lignes, délimiteur)
    - Liste des colonnes avec types détectés
    - Statistiques pour chaque colonne
    - Détection d'anomalies (valeurs manquantes, doublons, etc.)
    - Aperçu des premières lignes
    
    Sauvegardez aussi le rapport dans un fichier texte.
    """
    # TODO: Implémentez cette fonction
    pass


def interface_csv_interactif():
    """
    Interface interactive pour manipuler des fichiers CSV.
    
    Options :
    1. Analyser un fichier CSV
    2. Convertir le format d'un CSV
    3. Filtrer des données CSV
    4. Fusionner des fichiers CSV
    5. Générer un rapport
    6. Quitter
    
    Gérez toutes les exceptions et guidez l'utilisateur.
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
                # TODO: Implémentez l'analyse
                pass
            elif choix == '2':
                # TODO: Implémentez la conversion
                pass
            elif choix == '3':
                # TODO: Implémentez le filtrage
                pass
            elif choix == '4':
                # TODO: Implémentez la fusion
                pass
            elif choix == '5':
                # TODO: Implémentez la génération de rapport
                pass
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
    print("=== Tests Exercice 3 ===")
    
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
    
    # Décommentez pour tester interactivement
    # interface_csv_interactif()
