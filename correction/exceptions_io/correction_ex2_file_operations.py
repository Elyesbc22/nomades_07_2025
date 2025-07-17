"""
Correction complète - Exercice 2 : Opérations sur les fichiers
==============================================================

Cette correction montre les solutions complètes pour l'exercice 2.
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
    """
    try:
        with open(chemin_fichier, 'r', encoding='utf-8') as fichier:
            contenu = fichier.read()
        return (True, contenu)
    except FileNotFoundError:
        return (False, "Fichier non trouvé")
    except PermissionError:
        return (False, "Permission refusée")
    except UnicodeDecodeError:
        return (False, "Erreur d'encodage")
    except Exception as e:
        return (False, f"Erreur inattendue : {str(e)}")


def ecrire_fichier_securise(chemin_fichier, contenu, mode='w'):
    """
    Écrit du contenu dans un fichier de manière sécurisée.
    
    Args:
        chemin_fichier (str): Le chemin vers le fichier
        contenu (str): Le contenu à écrire
        mode (str): Le mode d'écriture ('w' ou 'a')
    
    Returns:
        tuple: (succès: bool, message: str)
    """
    try:
        # Créer le dossier parent si nécessaire
        dossier_parent = Path(chemin_fichier).parent
        dossier_parent.mkdir(parents=True, exist_ok=True)
        
        with open(chemin_fichier, mode, encoding='utf-8') as fichier:
            fichier.write(contenu)
        return (True, "Fichier écrit avec succès")
    except PermissionError:
        return (False, "Permission refusée pour l'écriture")
    except OSError as e:
        return (False, f"Erreur système : {str(e)}")
    except UnicodeEncodeError:
        return (False, "Erreur d'encodage lors de l'écriture")
    except Exception as e:
        return (False, f"Erreur inattendue : {str(e)}")


def copier_fichier_avec_verification(source, destination):
    """
    Copie un fichier avec vérifications et gestion d'erreurs.
    
    Args:
        source (str): Chemin du fichier source
        destination (str): Chemin du fichier destination
    
    Returns:
        tuple: (succès: bool, message: str)
    """
    try:
        # Vérifier que le fichier source existe
        if not Path(source).exists():
            return (False, f"Le fichier source '{source}' n'existe pas")
        
        # Vérifier si le fichier destination existe déjà
        if Path(destination).exists():
            reponse = input(f"Le fichier '{destination}' existe déjà. Remplacer ? (o/n) : ")
            if reponse.lower() != 'o':
                return (False, "Copie annulée par l'utilisateur")
        
        # Créer le dossier de destination si nécessaire
        Path(destination).parent.mkdir(parents=True, exist_ok=True)
        
        # Copier le fichier avec progression
        taille_fichier = Path(source).stat().st_size
        octets_copies = 0
        
        with open(source, 'rb') as f_source, open(destination, 'wb') as f_dest:
            while True:
                chunk = f_source.read(8192)  # Lire par chunks de 8KB
                if not chunk:
                    break
                f_dest.write(chunk)
                octets_copies += len(chunk)
                
                # Afficher la progression
                if taille_fichier > 0:
                    pourcentage = (octets_copies / taille_fichier) * 100
                    print(f"\rProgression : {pourcentage:.1f}% ({octets_copies}/{taille_fichier} octets)", end='')
        
        print()  # Nouvelle ligne après la progression
        return (True, f"Fichier copié avec succès ({octets_copies} octets)")
        
    except PermissionError:
        return (False, "Permission refusée")
    except OSError as e:
        return (False, f"Erreur système : {str(e)}")
    except Exception as e:
        return (False, f"Erreur inattendue : {str(e)}")


def analyser_fichier_texte(chemin_fichier):
    """
    Analyse un fichier texte et retourne des statistiques.
    
    Args:
        chemin_fichier (str): Le chemin vers le fichier
    
    Returns:
        dict: Statistiques du fichier ou None si erreur
    """
    try:
        with open(chemin_fichier, 'r', encoding='utf-8') as fichier:
            contenu = fichier.read()
        
        # Calculer les statistiques
        lignes = contenu.split('\n')
        mots = contenu.split()
        
        # Trouver la ligne la plus longue
        ligne_plus_longue = max(lignes, key=len) if lignes else ""
        
        # Taille du fichier
        taille_octets = Path(chemin_fichier).stat().st_size
        
        statistiques = {
            'taille_octets': taille_octets,
            'nombre_lignes': len(lignes),
            'nombre_mots': len(mots),
            'nombre_caracteres': len(contenu),
            'ligne_plus_longue': ligne_plus_longue
        }
        
        return statistiques
        
    except FileNotFoundError:
        print(f"Erreur : Le fichier '{chemin_fichier}' n'existe pas")
        return None
    except PermissionError:
        print(f"Erreur : Permission refusée pour '{chemin_fichier}'")
        return None
    except UnicodeDecodeError:
        print(f"Erreur : Problème d'encodage pour '{chemin_fichier}'")
        return None
    except Exception as e:
        print(f"Erreur inattendue lors de l'analyse : {str(e)}")
        return None


def journal_erreurs(nom_fichier_log="data/erreurs.log"):
    """
    Crée un système de journalisation des erreurs.
    
    Returns:
        function: Fonction de logging
    """
    from datetime import datetime
    
    def log_error(message, type_erreur="Erreur"):
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        ligne_log = f"[{timestamp}] {type_erreur}: {message}\n"
        
        # Afficher sur la console
        print(f"{type_erreur}: {message}")
        
        try:
            # Créer le dossier si nécessaire
            Path(nom_fichier_log).parent.mkdir(parents=True, exist_ok=True)
            
            # Écrire dans le fichier de log
            with open(nom_fichier_log, 'a', encoding='utf-8') as f_log:
                f_log.write(ligne_log)
        except Exception as e:
            print(f"Impossible d'écrire dans le log : {e}")
    
    return log_error


def gestionnaire_fichiers_interactif():
    """
    Interface interactive pour gérer des fichiers.
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
                chemin = input("Chemin du fichier à lire : ")
                succes, contenu = lire_fichier_securise(chemin)
                if succes:
                    print(f"\nContenu du fichier :\n{contenu}")
                else:
                    log_error(contenu, "Lecture")
                    
            elif choix == '2':
                chemin = input("Chemin du fichier à écrire : ")
                print("Entrez le contenu (tapez 'FIN' sur une ligne seule pour terminer) :")
                lignes = []
                while True:
                    ligne = input()
                    if ligne == 'FIN':
                        break
                    lignes.append(ligne)
                contenu = '\n'.join(lignes)
                
                mode = input("Mode d'écriture (w=remplacer, a=ajouter) [w] : ").strip() or 'w'
                succes, message = ecrire_fichier_securise(chemin, contenu, mode)
                if succes:
                    print(message)
                else:
                    log_error(message, "Écriture")
                    
            elif choix == '3':
                source = input("Fichier source : ")
                destination = input("Fichier destination : ")
                succes, message = copier_fichier_avec_verification(source, destination)
                if succes:
                    print(message)
                else:
                    log_error(message, "Copie")
                    
            elif choix == '4':
                chemin = input("Fichier à analyser : ")
                stats = analyser_fichier_texte(chemin)
                if stats:
                    print("\nStatistiques du fichier :")
                    for cle, valeur in stats.items():
                        print(f"  {cle}: {valeur}")
                        
            elif choix == '5':
                dossier = input("Dossier à lister : ")
                try:
                    if Path(dossier).exists():
                        print(f"\nContenu de '{dossier}' :")
                        for item in Path(dossier).iterdir():
                            type_item = "📁" if item.is_dir() else "📄"
                            print(f"  {type_item} {item.name}")
                    else:
                        log_error(f"Le dossier '{dossier}' n'existe pas", "Listage")
                except Exception as e:
                    log_error(str(e), "Listage")
                    
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
    print("=== Tests Correction Exercice 2 ===")
    
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
    
    print("\n4. Tests terminés avec succès !")
    
    # Décommentez pour tester interactivement
    # gestionnaire_fichiers_interactif()
