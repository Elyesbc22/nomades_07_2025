"""
Exercice 2 : Opérations sur les fichiers
========================================

Objectifs :
- Lire et écrire des fichiers texte
- Gérer les exceptions liées aux fichiers
- Utiliser la syntaxe with...open
- Manipuler le contenu des fichiers

Instructions :
Complétez les fonctions ci-dessous en gérant les erreurs de fichiers.
"""

import os
from pathlib import Path


def lire_fichier_securise(chemin_fichier):
    """
    Lit le contenu d'un fichier de manière sécurisée.
    
    Args:
        chemin_fichier (str): Le chemin vers le fichier
    
    Returns:
        tuple: (succès: bool, contenu: str ou message d'erreur: str)
        
    Exceptions à gérer :
    - FileNotFoundError
    - PermissionError
    - UnicodeDecodeError
    
    Exemple :
        >>> lire_fichier_securise("data/test.txt")
        (True, "Contenu du fichier...")
        >>> lire_fichier_securise("inexistant.txt")
        (False, "Fichier non trouvé")
    """
    # TODO: Implémentez cette fonction
    pass


def ecrire_fichier_securise(chemin_fichier, contenu, mode='w'):
    """
    Écrit du contenu dans un fichier de manière sécurisée.
    
    Args:
        chemin_fichier (str): Le chemin vers le fichier
        contenu (str): Le contenu à écrire
        mode (str): Le mode d'écriture ('w' ou 'a')
    
    Returns:
        tuple: (succès: bool, message: str)
        
    Exceptions à gérer :
    - PermissionError
    - OSError
    - UnicodeEncodeError
    
    Si le dossier parent n'existe pas, créez-le.
    """
    # TODO: Implémentez cette fonction
    pass


def copier_fichier_avec_verification(source, destination):
    """
    Copie un fichier avec vérifications et gestion d'erreurs.
    
    Args:
        source (str): Chemin du fichier source
        destination (str): Chemin du fichier destination
    
    Returns:
        tuple: (succès: bool, message: str)
        
    Vérifications :
    1. Le fichier source existe
    2. Le fichier destination n'existe pas (demander confirmation sinon)
    3. Permissions suffisantes
    
    Affichez la progression (nombre d'octets copiés).
    """
    # TODO: Implémentez cette fonction
    pass


def analyser_fichier_texte(chemin_fichier):
    """
    Analyse un fichier texte et retourne des statistiques.
    
    Args:
        chemin_fichier (str): Le chemin vers le fichier
    
    Returns:
        dict: Statistiques du fichier ou None si erreur
        {
            'taille_octets': int,
            'nombre_lignes': int,
            'nombre_mots': int,
            'nombre_caracteres': int,
            'ligne_plus_longue': str
        }
    
    Gérez toutes les exceptions et affichez des messages informatifs.
    """
    # TODO: Implémentez cette fonction
    pass


def journal_erreurs(nom_fichier_log="data/erreurs.log"):
    """
    Crée un système de journalisation des erreurs.
    
    Cette fonction retourne une fonction de logging qui :
    1. Écrit les erreurs dans un fichier de log avec timestamp
    2. Gère les erreurs d'écriture du log lui-même
    3. Affiche aussi l'erreur sur la console
    
    Returns:
        function: Fonction de logging
        
    Exemple d'utilisation :
        log_error = journal_erreurs()
        log_error("Une erreur s'est produite", "TypeError")
    """
    from datetime import datetime
    
    def log_error(message, type_erreur="Erreur"):
        # TODO: Implémentez la fonction de logging
        pass
    
    return log_error


def gestionnaire_fichiers_interactif():
    """
    Interface interactive pour gérer des fichiers.
    
    Options disponibles :
    1. Lire un fichier
    2. Écrire dans un fichier
    3. Copier un fichier
    4. Analyser un fichier
    5. Lister les fichiers d'un dossier
    6. Quitter
    
    Gérez toutes les exceptions et proposez des actions de récupération.
    """
    log_error = journal_erreurs()
    
    while True:
        print("\n=== Gestionnaire de Fichiers ===")
        print("1. Lire un fichier")
        print("2. Écrire dans un fichier")
        print("3. Copier un fichier")
        print("4. Analyser un fichier")
        print("5. Lister les fichiers d'un dossier")
        print("6. Quitter")
        
        try:
            choix = input("\nVotre choix (1-6) : ").strip()
            
            if choix == '1':
                # TODO: Implémentez la lecture de fichier
                pass
            elif choix == '2':
                # TODO: Implémentez l'écriture de fichier
                pass
            elif choix == '3':
                # TODO: Implémentez la copie de fichier
                pass
            elif choix == '4':
                # TODO: Implémentez l'analyse de fichier
                pass
            elif choix == '5':
                # TODO: Implémentez le listage de dossier
                pass
            elif choix == '6':
                print("Au revoir !")
                break
            else:
                print("Choix invalide. Veuillez choisir entre 1 et 6.")
                
        except KeyboardInterrupt:
            print("\n\nArrêt demandé par l'utilisateur.")
            break
        except Exception as e:
            log_error(f"Erreur inattendue : {str(e)}", type(e).__name__)


# Tests et données de test
def creer_fichiers_test():
    """Crée des fichiers de test pour les exercices."""
    # Créer le dossier data s'il n'existe pas
    os.makedirs("data", exist_ok=True)
    
    # Fichier de test simple
    with open("data/test.txt", "w", encoding="utf-8") as f:
        f.write("Bonjour le monde !\nCeci est un fichier de test.\nIl contient plusieurs lignes.\n")
    
    # Fichier avec du contenu plus complexe
    with open("data/poeme.txt", "w", encoding="utf-8") as f:
        f.write("""L'informatique est un art,
Le code une poésie.
Chaque ligne écrite avec soin,
Révèle une symphonie.

Les exceptions sont nos garde-fous,
Les fichiers nos mémoires.
Python nous guide vers le but,
Dans cette belle histoire.""")
    
    print("Fichiers de test créés dans le dossier 'data/'")


if __name__ == "__main__":
    print("=== Tests Exercice 2 ===")
    
    # Créer les fichiers de test
    creer_fichiers_test()
    
    # Test lire_fichier_securise
    print("\n1. Test lire_fichier_securise :")
    succes, contenu = lire_fichier_securise("data/test.txt")
    if succes:
        print(f"   Contenu lu : {repr(contenu[:50])}...")
    else:
        print(f"   Erreur : {contenu}")
    
    # Test fichier inexistant
    succes, contenu = lire_fichier_securise("inexistant.txt")
    print(f"   Fichier inexistant : {contenu}")
    
    # Test ecrire_fichier_securise
    print("\n2. Test ecrire_fichier_securise :")
    succes, message = ecrire_fichier_securise("results/test_ecriture.txt", "Test d'écriture\n")
    print(f"   Écriture : {message}")
    
    # Test analyser_fichier_texte
    print("\n3. Test analyser_fichier_texte :")
    stats = analyser_fichier_texte("data/poeme.txt")
    if stats:
        print(f"   Statistiques : {stats}")
    
    # Décommentez pour tester interactivement
    # gestionnaire_fichiers_interactif()
