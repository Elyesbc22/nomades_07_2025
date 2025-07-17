"""
Exercice 4 : Exceptions personnalisées
======================================

Objectifs :
- Créer des exceptions personnalisées
- Hiérarchie d'exceptions
- Gestion avancée des erreurs
- Logging et debugging

Instructions :
Implémentez un système de gestion de bibliothèque avec des exceptions personnalisées.
"""

import json
import csv
from datetime import datetime, timedelta
from pathlib import Path


# ========================
# EXCEPTIONS PERSONNALISÉES
# ========================

class BibliothequeError(Exception):
    """Exception de base pour le système de bibliothèque."""
    def __init__(self, message, code_erreur=None):
        super().__init__(message)
        self.message = message
        self.code_erreur = code_erreur
        self.timestamp = datetime.now()
    
    def __str__(self):
        return f"[{self.code_erreur}] {self.message}"


class LivreError(BibliothequeError):
    """Erreurs liées aux livres."""
    pass


class UtilisateurError(BibliothequeError):
    """Erreurs liées aux utilisateurs."""
    pass


class EmpruntError(BibliothequeError):
    """Erreurs liées aux emprunts."""
    pass


# TODO: Créez les exceptions spécifiques suivantes héritant des classes ci-dessus :

class LivreNonTrouveError(LivreError):
    """Exception levée quand un livre n'est pas trouvé."""
    # TODO: Implémentez cette exception
    pass


class LivreDejaExisteError(LivreError):
    """Exception levée quand on tente d'ajouter un livre qui existe déjà."""
    # TODO: Implémentez cette exception
    pass


class LivreIndisponibleError(EmpruntError):
    """Exception levée quand un livre n'est pas disponible pour l'emprunt."""
    # TODO: Implémentez cette exception
    pass


class UtilisateurNonTrouveError(UtilisateurError):
    """Exception levée quand un utilisateur n'est pas trouvé."""
    # TODO: Implémentez cette exception
    pass


class LimiteEmpruntDepasseeError(EmpruntError):
    """Exception levée quand la limite d'emprunts est dépassée."""
    # TODO: Implémentez cette exception
    pass


class EmpruntExpireError(EmpruntError):
    """Exception levée pour un emprunt expiré."""
    # TODO: Implémentez cette exception
    pass


class DonneeInvalideError(BibliothequeError):
    """Exception levée pour des données invalides."""
    # TODO: Implémentez cette exception
    pass


# ========================
# CLASSES MÉTIER
# ========================

class Livre:
    """Représente un livre dans la bibliothèque."""
    
    def __init__(self, isbn, titre, auteur, annee_publication, exemplaires=1):
        # TODO: Validez les données et levez DonneeInvalideError si nécessaire
        # Contraintes :
        # - ISBN : 10 ou 13 chiffres
        # - Titre : non vide
        # - Auteur : non vide
        # - Année : entre 1800 et année actuelle
        # - Exemplaires : > 0
        pass
    
    def to_dict(self):
        """Convertit le livre en dictionnaire."""
        # TODO: Implémentez cette méthode
        pass
    
    @classmethod
    def from_dict(cls, data):
        """Crée un livre à partir d'un dictionnaire."""
        # TODO: Implémentez cette méthode
        # Gérez les KeyError avec DonneeInvalideError
        pass


class Utilisateur:
    """Représente un utilisateur de la bibliothèque."""
    
    def __init__(self, user_id, nom, email, limite_emprunts=3):
        # TODO: Validez les données
        # Contraintes :
        # - user_id : entier positif
        # - nom : non vide
        # - email : format valide (contient @ et .)
        # - limite_emprunts : > 0
        pass
    
    def to_dict(self):
        """Convertit l'utilisateur en dictionnaire."""
        # TODO: Implémentez cette méthode
        pass
    
    @classmethod
    def from_dict(cls, data):
        """Crée un utilisateur à partir d'un dictionnaire."""
        # TODO: Implémentez cette méthode
        pass


class Emprunt:
    """Représente un emprunt de livre."""
    
    def __init__(self, user_id, isbn, duree_jours=14):
        # TODO: Implémentez cette classe
        # Attributs : user_id, isbn, date_emprunt, date_retour_prevue, rendu
        pass
    
    def est_expire(self):
        """Vérifie si l'emprunt est expiré."""
        # TODO: Implémentez cette méthode
        pass
    
    def to_dict(self):
        """Convertit l'emprunt en dictionnaire."""
        # TODO: Implémentez cette méthode
        pass
    
    @classmethod
    def from_dict(cls, data):
        """Crée un emprunt à partir d'un dictionnaire."""
        # TODO: Implémentez cette méthode
        pass


# ========================
# SYSTÈME DE BIBLIOTHÈQUE
# ========================

class Bibliotheque:
    """Système de gestion de bibliothèque avec exceptions personnalisées."""
    
    def __init__(self, fichier_donnees="data/bibliotheque.json"):
        self.fichier_donnees = fichier_donnees
        self.livres = {}  # {isbn: Livre}
        self.utilisateurs = {}  # {user_id: Utilisateur}
        self.emprunts = {}  # {(user_id, isbn): Emprunt}
        
        # Créer le dossier si nécessaire
        Path(fichier_donnees).parent.mkdir(parents=True, exist_ok=True)
        
        # Charger les données existantes
        self.charger_donnees()
    
    def ajouter_livre(self, livre):
        """
        Ajoute un livre à la bibliothèque.
        
        Args:
            livre (Livre): Le livre à ajouter
        
        Raises:
            LivreDejaExisteError: Si le livre existe déjà
            DonneeInvalideError: Si les données sont invalides
        """
        # TODO: Implémentez cette méthode
        pass
    
    def supprimer_livre(self, isbn):
        """
        Supprime un livre de la bibliothèque.
        
        Args:
            isbn (str): ISBN du livre à supprimer
        
        Raises:
            LivreNonTrouveError: Si le livre n'existe pas
            EmpruntError: Si le livre est actuellement emprunté
        """
        # TODO: Implémentez cette méthode
        pass
    
    def ajouter_utilisateur(self, utilisateur):
        """
        Ajoute un utilisateur à la bibliothèque.
        
        Args:
            utilisateur (Utilisateur): L'utilisateur à ajouter
        
        Raises:
            UtilisateurError: Si l'utilisateur existe déjà
        """
        # TODO: Implémentez cette méthode
        pass
    
    def emprunter_livre(self, user_id, isbn):
        """
        Gère l'emprunt d'un livre.
        
        Args:
            user_id (int): ID de l'utilisateur
            isbn (str): ISBN du livre
        
        Returns:
            Emprunt: L'objet emprunt créé
        
        Raises:
            UtilisateurNonTrouveError: Si l'utilisateur n'existe pas
            LivreNonTrouveError: Si le livre n'existe pas
            LivreIndisponibleError: Si le livre n'est pas disponible
            LimiteEmpruntDepasseeError: Si la limite d'emprunts est atteinte
        """
        # TODO: Implémentez cette méthode
        pass
    
    def rendre_livre(self, user_id, isbn):
        """
        Gère le retour d'un livre.
        
        Args:
            user_id (int): ID de l'utilisateur
            isbn (str): ISBN du livre
        
        Raises:
            EmpruntError: Si aucun emprunt correspondant n'est trouvé
        """
        # TODO: Implémentez cette méthode
        pass
    
    def verifier_emprunts_expires(self):
        """
        Vérifie et retourne les emprunts expirés.
        
        Returns:
            list[Emprunt]: Liste des emprunts expirés
        """
        # TODO: Implémentez cette méthode
        pass
    
    def sauvegarder_donnees(self):
        """
        Sauvegarde les données dans le fichier JSON.
        
        Raises:
            BibliothequeError: En cas d'erreur de sauvegarde
        """
        try:
            donnees = {
                'livres': {isbn: livre.to_dict() for isbn, livre in self.livres.items()},
                'utilisateurs': {str(uid): user.to_dict() for uid, user in self.utilisateurs.items()},
                'emprunts': {f"{uid}_{isbn}": emprunt.to_dict() 
                           for (uid, isbn), emprunt in self.emprunts.items()}
            }
            
            with open(self.fichier_donnees, 'w', encoding='utf-8') as f:
                json.dump(donnees, f, indent=2, ensure_ascii=False, default=str)
                
        except Exception as e:
            raise BibliothequeError(f"Erreur lors de la sauvegarde : {e}", "SAVE_ERROR")
    
    def charger_donnees(self):
        """
        Charge les données depuis le fichier JSON.
        
        Raises:
            BibliothequeError: En cas d'erreur de chargement
        """
        try:
            if not Path(self.fichier_donnees).exists():
                return  # Fichier vide, données par défaut
            
            with open(self.fichier_donnees, 'r', encoding='utf-8') as f:
                donnees = json.load(f)
            
            # Charger les livres
            for isbn, livre_data in donnees.get('livres', {}).items():
                self.livres[isbn] = Livre.from_dict(livre_data)
            
            # Charger les utilisateurs
            for uid, user_data in donnees.get('utilisateurs', {}).items():
                self.utilisateurs[int(uid)] = Utilisateur.from_dict(user_data)
            
            # Charger les emprunts
            for key, emprunt_data in donnees.get('emprunts', {}).items():
                uid, isbn = key.split('_', 1)
                self.emprunts[(int(uid), isbn)] = Emprunt.from_dict(emprunt_data)
                
        except Exception as e:
            raise BibliothequeError(f"Erreur lors du chargement : {e}", "LOAD_ERROR")
    
    def generer_rapport(self, fichier_sortie="results/rapport_bibliotheque.txt"):
        """
        Génère un rapport complet de la bibliothèque.
        
        Args:
            fichier_sortie (str): Chemin du fichier de rapport
        """
        # TODO: Implémentez cette méthode
        # Le rapport doit inclure :
        # - Statistiques générales
        # - Liste des livres avec disponibilité
        # - Liste des emprunts en cours et expirés
        # - Utilisateurs avec le plus d'emprunts
        pass


# ========================
# INTERFACE UTILISATEUR
# ========================

def interface_bibliotheque():
    """Interface interactive pour la gestion de bibliothèque."""
    biblio = Bibliotheque()
    
    while True:
        print("\n=== Système de Bibliothèque ===")
        print("1. Ajouter un livre")
        print("2. Ajouter un utilisateur")
        print("3. Emprunter un livre")
        print("4. Rendre un livre")
        print("5. Vérifier les emprunts expirés")
        print("6. Générer un rapport")
        print("7. Sauvegarder")
        print("8. Quitter")
        
        try:
            choix = input("\nVotre choix (1-8) : ").strip()
            
            if choix == '1':
                # TODO: Implémentez l'ajout de livre
                pass
            elif choix == '2':
                # TODO: Implémentez l'ajout d'utilisateur
                pass
            elif choix == '3':
                # TODO: Implémentez l'emprunt
                pass
            elif choix == '4':
                # TODO: Implémentez le retour
                pass
            elif choix == '5':
                # TODO: Implémentez la vérification des emprunts expirés
                pass
            elif choix == '6':
                # TODO: Implémentez la génération de rapport
                pass
            elif choix == '7':
                biblio.sauvegarder_donnees()
                print("Données sauvegardées avec succès !")
            elif choix == '8':
                biblio.sauvegarder_donnees()
                print("Au revoir !")
                break
            else:
                print("Choix invalide.")
                
        except BibliothequeError as e:
            print(f"Erreur de bibliothèque : {e}")
        except KeyboardInterrupt:
            print("\n\nAu revoir !")
            break
        except Exception as e:
            print(f"Erreur inattendue : {e}")


# Tests
if __name__ == "__main__":
    print("=== Tests Exercice 4 ===")
    
    try:
        # Test création d'objets avec validation
        print("\n1. Test validation des données :")
        
        # Test livre valide
        livre = Livre("1234567890", "Python Programming", "John Doe", 2023)
        print(f"   Livre créé : {livre.titre}")
        
        # Test livre invalide
        try:
            livre_invalide = Livre("123", "Titre", "Auteur", 1500)  # ISBN et année invalides
        except DonneeInvalideError as e:
            print(f"   Erreur attendue : {e}")
        
        # Test utilisateur
        user = Utilisateur(1, "Alice Martin", "alice@email.com")
        print(f"   Utilisateur créé : {user.nom}")
        
        # Test système complet
        print("\n2. Test système bibliothèque :")
        biblio = Bibliotheque("data/test_biblio.json")
        
        # Ajouter des données de test
        biblio.ajouter_livre(livre)
        biblio.ajouter_utilisateur(user)
        
        # Test emprunt
        emprunt = biblio.emprunter_livre(1, "1234567890")
        print(f"   Emprunt créé pour l'utilisateur {emprunt.user_id}")
        
        print("\n3. Tests terminés avec succès !")
        
    except Exception as e:
        print(f"Erreur lors des tests : {e}")
    
    # Décommentez pour tester interactivement
    # interface_bibliotheque()
