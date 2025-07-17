"""
Correction complète - Exercice 4 : Exceptions personnalisées
=============================================================

Cette correction montre l'implémentation complète d'un système de gestion de bibliothèque
avec une hiérarchie d'exceptions personnalisées robuste.
"""

from datetime import datetime, timedelta
from typing import Dict, List, Optional, Set
import re
import json
from pathlib import Path


# ===== HIÉRARCHIE DES EXCEPTIONS PERSONNALISÉES =====

class BibliothequeError(Exception):
    """Exception de base pour le système de bibliothèque."""
    
    def __init__(self, message: str, code_erreur: Optional[str] = None, details: Optional[dict] = None):
        self.message = message
        self.code_erreur = code_erreur or "BIBLIO_ERROR"
        self.details = details or {}
        self.timestamp = datetime.now()
        super().__init__(self.message)
    
    def __str__(self):
        base_msg = f"[{self.code_erreur}] {self.message}"
        if self.details:
            details_str = ", ".join([f"{k}={v}" for k, v in self.details.items()])
            base_msg += f" (Détails: {details_str})"
        return base_msg
    
    def to_dict(self):
        """Convertit l'exception en dictionnaire pour la sérialisation."""
        return {
            'type': self.__class__.__name__,
            'message': self.message,
            'code_erreur': self.code_erreur,
            'details': self.details,
            'timestamp': self.timestamp.isoformat()
        }


class LivreError(BibliothequeError):
    """Erreurs liées aux livres."""
    pass


class LivreExistantError(LivreError):
    """Erreur levée quand un livre existe déjà."""
    
    def __init__(self, isbn: str, titre: Optional[str] = None):
        message = f"Le livre avec l'ISBN {isbn} existe déjà"
        if titre:
            message += f" (titre: {titre})"
        super().__init__(message, "LIVRE_EXISTANT", {"isbn": isbn, "titre": titre})


class LivreIntrouvableError(LivreError):
    """Erreur levée quand un livre n'est pas trouvé."""
    
    def __init__(self, critere: str, valeur: str):
        message = f"Livre non trouvé avec {critere}: {valeur}"
        super().__init__(message, "LIVRE_INTROUVABLE", {critere: valeur})


class LivreIndisponibleError(LivreError):
    """Erreur levée quand un livre n'est pas disponible."""
    
    def __init__(self, isbn: str, titre: Optional[str] = None, date_retour: Optional[datetime] = None):
        message = f"Le livre {isbn} n'est pas disponible"
        if titre:
            message += f" ('{titre}')"
        if date_retour:
            message += f", retour prévu le {date_retour.strftime('%d/%m/%Y')}"
        
        details = {"isbn": isbn, "titre": titre}
        if date_retour:
            details["date_retour"] = date_retour.isoformat()
        
        super().__init__(message, "LIVRE_INDISPONIBLE", details)


class UtilisateurError(BibliothequeError):
    """Erreurs liées aux utilisateurs."""
    pass


class UtilisateurExistantError(UtilisateurError):
    """Erreur levée quand un utilisateur existe déjà."""
    
    def __init__(self, identifiant: str):
        message = f"L'utilisateur {identifiant} existe déjà"
        super().__init__(message, "UTILISATEUR_EXISTANT", {"identifiant": identifiant})


class UtilisateurIntrouvableError(UtilisateurError):
    """Erreur levée quand un utilisateur n'est pas trouvé."""
    
    def __init__(self, identifiant: str):
        message = f"L'utilisateur {identifiant} n'existe pas"
        super().__init__(message, "UTILISATEUR_INTROUVABLE", {"identifiant": identifiant})


class UtilisateurSuspenduError(UtilisateurError):
    """Erreur levée quand un utilisateur est suspendu."""
    
    def __init__(self, identifiant: str, raison: Optional[str] = None, fin_suspension: Optional[datetime] = None):
        message = f"L'utilisateur {identifiant} est suspendu"
        if raison:
            message += f" (raison: {raison})"
        if fin_suspension:
            message += f" jusqu'au {fin_suspension.strftime('%d/%m/%Y')}"
        
        details = {"identifiant": identifiant, "raison": raison}
        if fin_suspension:
            details["fin_suspension"] = fin_suspension.isoformat()
        
        super().__init__(message, "UTILISATEUR_SUSPENDU", details)


class EmpruntError(BibliothequeError):
    """Erreurs liées aux emprunts."""
    pass


class LimiteEmpruntDepasseeError(EmpruntError):
    """Erreur levée quand la limite d'emprunts est dépassée."""
    
    def __init__(self, utilisateur: str, limite: int, emprunts_actuels: int):
        message = f"L'utilisateur {utilisateur} a atteint sa limite d'emprunts ({emprunts_actuels}/{limite})"
        super().__init__(message, "LIMITE_EMPRUNT_DEPASSEE", {
            "utilisateur": utilisateur,
            "limite": limite,
            "emprunts_actuels": emprunts_actuels
        })


class EmpruntIntrouvableError(EmpruntError):
    """Erreur levée quand un emprunt n'est pas trouvé."""
    
    def __init__(self, utilisateur: str, isbn: str):
        message = f"Aucun emprunt trouvé pour le livre {isbn} par l'utilisateur {utilisateur}"
        super().__init__(message, "EMPRUNT_INTROUVABLE", {
            "utilisateur": utilisateur,
            "isbn": isbn
        })


class RetardEmpruntError(EmpruntError):
    """Erreur levée pour les emprunts en retard."""
    
    def __init__(self, utilisateur: str, isbn: str, jours_retard: int, amende: Optional[float] = None):
        message = f"L'emprunt du livre {isbn} par {utilisateur} a {jours_retard} jour(s) de retard"
        if amende:
            message += f" (amende: {amende}€)"
        
        details = {
            "utilisateur": utilisateur,
            "isbn": isbn,
            "jours_retard": jours_retard
        }
        if amende:
            details["amende"] = amende
        
        super().__init__(message, "RETARD_EMPRUNT", details)


class ValidationError(BibliothequeError):
    """Erreurs de validation de données."""
    pass


class ISBNInvalideError(ValidationError):
    """Erreur levée pour un ISBN invalide."""
    
    def __init__(self, isbn: str):
        message = f"ISBN invalide: {isbn}"
        super().__init__(message, "ISBN_INVALIDE", {"isbn": isbn})


class DonneesInvalidesError(ValidationError):
    """Erreur levée pour des données invalides."""
    
    def __init__(self, champ: str, valeur: str, raison: str):
        message = f"Valeur invalide pour {champ}: {valeur} ({raison})"
        super().__init__(message, "DONNEES_INVALIDES", {
            "champ": champ,
            "valeur": valeur,
            "raison": raison
        })


# ===== CLASSES MÉTIER =====

class Livre:
    """Représente un livre dans la bibliothèque."""
    
    def __init__(self, isbn: str, titre: str, auteur: str, annee: int, genre: Optional[str] = None):
        self.isbn = self._valider_isbn(isbn)
        self.titre = self._valider_titre(titre)
        self.auteur = self._valider_auteur(auteur)
        self.annee = self._valider_annee(annee)
        self.genre = genre
        self.disponible = True
        self.date_ajout = datetime.now()
    
    def _valider_isbn(self, isbn: str) -> str:
        """Valide le format ISBN."""
        isbn_clean = re.sub(r'[^0-9X]', '', isbn.upper())
        
        if len(isbn_clean) == 10:
            # ISBN-10
            if not re.match(r'^\d{9}[\dX]$', isbn_clean):
                raise ISBNInvalideError(isbn)
        elif len(isbn_clean) == 13:
            # ISBN-13
            if not re.match(r'^\d{13}$', isbn_clean):
                raise ISBNInvalideError(isbn)
        else:
            raise ISBNInvalideError(isbn)
        
        return isbn_clean
    
    def _valider_titre(self, titre: str) -> str:
        """Valide le titre."""
        if not titre or not titre.strip():
            raise DonneesInvalidesError("titre", titre, "titre vide")
        if len(titre.strip()) < 2:
            raise DonneesInvalidesError("titre", titre, "titre trop court")
        return titre.strip()
    
    def _valider_auteur(self, auteur: str) -> str:
        """Valide l'auteur."""
        if not auteur or not auteur.strip():
            raise DonneesInvalidesError("auteur", auteur, "auteur vide")
        if len(auteur.strip()) < 2:
            raise DonneesInvalidesError("auteur", auteur, "nom d'auteur trop court")
        return auteur.strip()
    
    def _valider_annee(self, annee: int) -> int:
        """Valide l'année de publication."""
        annee_actuelle = datetime.now().year
        if not isinstance(annee, int):
            raise DonneesInvalidesError("annee", str(annee), "doit être un entier")
        if annee < 1000 or annee > annee_actuelle + 1:
            raise DonneesInvalidesError("annee", str(annee), f"doit être entre 1000 et {annee_actuelle + 1}")
        return annee
    
    def to_dict(self):
        """Convertit le livre en dictionnaire."""
        return {
            'isbn': self.isbn,
            'titre': self.titre,
            'auteur': self.auteur,
            'annee': self.annee,
            'genre': self.genre,
            'disponible': self.disponible,
            'date_ajout': self.date_ajout.isoformat()
        }


class Utilisateur:
    """Représente un utilisateur de la bibliothèque."""
    
    def __init__(self, identifiant: str, nom: str, email: str, limite_emprunts: int = 3):
        self.identifiant = self._valider_identifiant(identifiant)
        self.nom = self._valider_nom(nom)
        self.email = self._valider_email(email)
        self.limite_emprunts = limite_emprunts
        self.date_creation = datetime.now()
        self.suspendu = False
        self.raison_suspension = None
        self.fin_suspension = None
        self.historique_emprunts = []
    
    def _valider_identifiant(self, identifiant: str) -> str:
        """Valide l'identifiant utilisateur."""
        if not identifiant or not identifiant.strip():
            raise DonneesInvalidesError("identifiant", identifiant, "identifiant vide")
        if not re.match(r'^[a-zA-Z0-9_-]+$', identifiant):
            raise DonneesInvalidesError("identifiant", identifiant, "caractères invalides")
        if len(identifiant) < 3:
            raise DonneesInvalidesError("identifiant", identifiant, "trop court (min 3 caractères)")
        return identifiant.strip()
    
    def _valider_nom(self, nom: str) -> str:
        """Valide le nom."""
        if not nom or not nom.strip():
            raise DonneesInvalidesError("nom", nom, "nom vide")
        if len(nom.strip()) < 2:
            raise DonneesInvalidesError("nom", nom, "nom trop court")
        return nom.strip()
    
    def _valider_email(self, email: str) -> str:
        """Valide l'email."""
        pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
        if not re.match(pattern, email):
            raise DonneesInvalidesError("email", email, "format email invalide")
        return email.lower()
    
    def suspendre(self, raison: str, duree_jours: Optional[int] = None):
        """Suspend l'utilisateur."""
        self.suspendu = True
        self.raison_suspension = raison
        if duree_jours:
            self.fin_suspension = datetime.now() + timedelta(days=duree_jours)
    
    def lever_suspension(self):
        """Lève la suspension."""
        self.suspendu = False
        self.raison_suspension = None
        self.fin_suspension = None
    
    def est_suspendu(self) -> bool:
        """Vérifie si l'utilisateur est suspendu."""
        if not self.suspendu:
            return False
        
        if self.fin_suspension and datetime.now() > self.fin_suspension:
            self.lever_suspension()
            return False
        
        return True
    
    def to_dict(self):
        """Convertit l'utilisateur en dictionnaire."""
        return {
            'identifiant': self.identifiant,
            'nom': self.nom,
            'email': self.email,
            'limite_emprunts': self.limite_emprunts,
            'date_creation': self.date_creation.isoformat(),
            'suspendu': self.suspendu,
            'raison_suspension': self.raison_suspension,
            'fin_suspension': self.fin_suspension.isoformat() if self.fin_suspension else None
        }


class Emprunt:
    """Représente un emprunt de livre."""
    
    def __init__(self, utilisateur_id: str, isbn: str, duree_jours: int = 14):
        self.utilisateur_id = utilisateur_id
        self.isbn = isbn
        self.date_emprunt = datetime.now()
        self.date_retour_prevue = self.date_emprunt + timedelta(days=duree_jours)
        self.date_retour_effective = None
        self.retourne = False
        self.amende = 0.0
    
    def est_en_retard(self) -> bool:
        """Vérifie si l'emprunt est en retard."""
        return datetime.now() > self.date_retour_prevue and not self.retourne
    
    def jours_retard(self) -> int:
        """Calcule le nombre de jours de retard."""
        if not self.est_en_retard():
            return 0
        return (datetime.now() - self.date_retour_prevue).days
    
    def calculer_amende(self, tarif_par_jour: float = 0.5) -> float:
        """Calcule l'amende pour retard."""
        if not self.est_en_retard():
            return 0.0
        return self.jours_retard() * tarif_par_jour
    
    def retourner(self, amende: Optional[float] = None):
        """Marque l'emprunt comme retourné."""
        self.date_retour_effective = datetime.now()
        self.retourne = True
        if amende is not None:
            self.amende = amende
    
    def to_dict(self):
        """Convertit l'emprunt en dictionnaire."""
        return {
            'utilisateur_id': self.utilisateur_id,
            'isbn': self.isbn,
            'date_emprunt': self.date_emprunt.isoformat(),
            'date_retour_prevue': self.date_retour_prevue.isoformat(),
            'date_retour_effective': self.date_retour_effective.isoformat() if self.date_retour_effective else None,
            'retourne': self.retourne,
            'amende': self.amende
        }


class SystemeBibliotheque:
    """Système de gestion de bibliothèque avec gestion d'exceptions complète."""
    
    def __init__(self):
        self.livres: Dict[str, Livre] = {}
        self.utilisateurs: Dict[str, Utilisateur] = {}
        self.emprunts: List[Emprunt] = []
        self.historique_erreurs: List[dict] = []
        self.configuration = {
            'duree_emprunt_defaut': 14,
            'limite_emprunts_defaut': 3,
            'tarif_amende_jour': 0.5,
            'max_jours_retard_suspension': 30
        }
    
    def _enregistrer_erreur(self, erreur: BibliothequeError):
        """Enregistre une erreur dans l'historique."""
        self.historique_erreurs.append(erreur.to_dict())
    
    def ajouter_livre(self, isbn: str, titre: str, auteur: str, annee: int, genre: Optional[str] = None) -> Livre:
        """
        Ajoute un livre à la bibliothèque.
        
        Raises:
            LivreExistantError: Si le livre existe déjà
            ValidationError: Si les données sont invalides
        """
        try:
            # Créer le livre (validation automatique)
            livre = Livre(isbn, titre, auteur, annee, genre)
            
            # Vérifier s'il existe déjà
            if livre.isbn in self.livres:
                erreur = LivreExistantError(livre.isbn, livre.titre)
                self._enregistrer_erreur(erreur)
                raise erreur
            
            # Ajouter le livre
            self.livres[livre.isbn] = livre
            return livre
            
        except ValidationError as e:
            self._enregistrer_erreur(e)
            raise
        except Exception as e:
            erreur = BibliothequeError(f"Erreur lors de l'ajout du livre : {str(e)}")
            self._enregistrer_erreur(erreur)
            raise erreur
    
    def rechercher_livre(self, **criteres) -> List[Livre]:
        """
        Recherche des livres selon des critères.
        
        Args:
            **criteres: isbn, titre, auteur, annee, genre
        
        Returns:
            Liste des livres correspondants
        """
        resultats = []
        
        for livre in self.livres.values():
            correspond = True
            
            for critere, valeur in criteres.items():
                if not hasattr(livre, critere):
                    continue
                
                valeur_livre = getattr(livre, critere)
                
                if critere in ['titre', 'auteur', 'genre']:
                    # Recherche insensible à la casse
                    if valeur.lower() not in str(valeur_livre).lower():
                        correspond = False
                        break
                else:
                    # Correspondance exacte
                    if valeur_livre != valeur:
                        correspond = False
                        break
            
            if correspond:
                resultats.append(livre)
        
        return resultats
    
    def obtenir_livre(self, isbn: str) -> Livre:
        """
        Obtient un livre par son ISBN.
        
        Raises:
            LivreIntrouvableError: Si le livre n'existe pas
        """
        if isbn not in self.livres:
            erreur = LivreIntrouvableError("isbn", isbn)
            self._enregistrer_erreur(erreur)
            raise erreur
        
        return self.livres[isbn]
    
    def ajouter_utilisateur(self, identifiant: str, nom: str, email: str, limite_emprunts: Optional[int] = None) -> Utilisateur:
        """
        Ajoute un utilisateur.
        
        Raises:
            UtilisateurExistantError: Si l'utilisateur existe déjà
            ValidationError: Si les données sont invalides
        """
        try:
            if limite_emprunts is None:
                limite_emprunts = self.configuration['limite_emprunts_defaut']
            
            # Créer l'utilisateur (validation automatique)
            utilisateur = Utilisateur(identifiant, nom, email, limite_emprunts)
            
            # Vérifier s'il existe déjà
            if utilisateur.identifiant in self.utilisateurs:
                erreur = UtilisateurExistantError(utilisateur.identifiant)
                self._enregistrer_erreur(erreur)
                raise erreur
            
            # Ajouter l'utilisateur
            self.utilisateurs[utilisateur.identifiant] = utilisateur
            return utilisateur
            
        except ValidationError as e:
            self._enregistrer_erreur(e)
            raise
        except Exception as e:
            erreur = BibliothequeError(f"Erreur lors de l'ajout de l'utilisateur : {str(e)}")
            self._enregistrer_erreur(erreur)
            raise erreur
    
    def obtenir_utilisateur(self, identifiant: str) -> Utilisateur:
        """
        Obtient un utilisateur par son identifiant.
        
        Raises:
            UtilisateurIntrouvableError: Si l'utilisateur n'existe pas
        """
        if identifiant not in self.utilisateurs:
            erreur = UtilisateurIntrouvableError(identifiant)
            self._enregistrer_erreur(erreur)
            raise erreur
        
        return self.utilisateurs[identifiant]
    
    def emprunter_livre(self, utilisateur_id: str, isbn: str, duree_jours: Optional[int] = None) -> Emprunt:
        """
        Effectue un emprunt de livre.
        
        Raises:
            UtilisateurIntrouvableError: Si l'utilisateur n'existe pas
            UtilisateurSuspenduError: Si l'utilisateur est suspendu
            LivreIntrouvableError: Si le livre n'existe pas
            LivreIndisponibleError: Si le livre n'est pas disponible
            LimiteEmpruntDepasseeError: Si la limite d'emprunts est atteinte
        """
        try:
            if duree_jours is None:
                duree_jours = self.configuration['duree_emprunt_defaut']
            
            # Vérifier l'utilisateur
            utilisateur = self.obtenir_utilisateur(utilisateur_id)
            
            if utilisateur.est_suspendu():
                erreur = UtilisateurSuspenduError(
                    utilisateur_id, 
                    utilisateur.raison_suspension, 
                    utilisateur.fin_suspension
                )
                self._enregistrer_erreur(erreur)
                raise erreur
            
            # Vérifier le livre
            livre = self.obtenir_livre(isbn)
            
            if not livre.disponible:
                # Trouver la date de retour prévue
                emprunt_actuel = next((e for e in self.emprunts 
                                     if e.isbn == isbn and not e.retourne), None)
                date_retour = emprunt_actuel.date_retour_prevue if emprunt_actuel else None
                
                erreur = LivreIndisponibleError(isbn, livre.titre, date_retour)
                self._enregistrer_erreur(erreur)
                raise erreur
            
            # Vérifier la limite d'emprunts
            emprunts_actifs = self._obtenir_emprunts_actifs(utilisateur_id)
            if len(emprunts_actifs) >= utilisateur.limite_emprunts:
                erreur = LimiteEmpruntDepasseeError(
                    utilisateur_id, 
                    utilisateur.limite_emprunts, 
                    len(emprunts_actifs)
                )
                self._enregistrer_erreur(erreur)
                raise erreur
            
            # Effectuer l'emprunt
            emprunt = Emprunt(utilisateur_id, isbn, duree_jours)
            self.emprunts.append(emprunt)
            livre.disponible = False
            
            return emprunt
            
        except BibliothequeError:
            raise
        except Exception as e:
            erreur = BibliothequeError(f"Erreur lors de l'emprunt : {str(e)}")
            self._enregistrer_erreur(erreur)
            raise erreur
    
    def retourner_livre(self, utilisateur_id: str, isbn: str) -> Emprunt:
        """
        Effectue le retour d'un livre.
        
        Raises:
            EmpruntIntrouvableError: Si l'emprunt n'existe pas
            RetardEmpruntError: Si l'emprunt est en retard (warning)
        """
        try:
            # Trouver l'emprunt
            emprunt = next((e for e in self.emprunts 
                           if e.utilisateur_id == utilisateur_id and e.isbn == isbn and not e.retourne), None)
            
            if not emprunt:
                erreur = EmpruntIntrouvableError(utilisateur_id, isbn)
                self._enregistrer_erreur(erreur)
                raise erreur
            
            # Vérifier les retards
            amende = 0.0
            if emprunt.est_en_retard():
                jours_retard = emprunt.jours_retard()
                amende = emprunt.calculer_amende(self.configuration['tarif_amende_jour'])
                
                # Créer une erreur de retard (comme avertissement)
                erreur_retard = RetardEmpruntError(utilisateur_id, isbn, jours_retard, amende)
                self._enregistrer_erreur(erreur_retard)
                
                # Suspendre si retard trop important
                if jours_retard > self.configuration['max_jours_retard_suspension']:
                    utilisateur = self.obtenir_utilisateur(utilisateur_id)
                    utilisateur.suspendre(f"Retard de {jours_retard} jours", 7)
            
            # Effectuer le retour
            emprunt.retourner(amende)
            livre = self.obtenir_livre(isbn)
            livre.disponible = True
            
            # Ajouter à l'historique de l'utilisateur
            utilisateur = self.obtenir_utilisateur(utilisateur_id)
            utilisateur.historique_emprunts.append(emprunt.to_dict())
            
            return emprunt
            
        except BibliothequeError:
            raise
        except Exception as e:
            erreur = BibliothequeError(f"Erreur lors du retour : {str(e)}")
            self._enregistrer_erreur(erreur)
            raise erreur
    
    def _obtenir_emprunts_actifs(self, utilisateur_id: str) -> List[Emprunt]:
        """Obtient les emprunts actifs d'un utilisateur."""
        return [e for e in self.emprunts if e.utilisateur_id == utilisateur_id and not e.retourne]
    
    def obtenir_emprunts_en_retard(self) -> List[Emprunt]:
        """Obtient tous les emprunts en retard."""
        return [e for e in self.emprunts if e.est_en_retard()]
    
    def generer_rapport_erreurs(self) -> str:
        """Génère un rapport des erreurs."""
        if not self.historique_erreurs:
            return "Aucune erreur enregistrée."
        
        rapport = ["=== RAPPORT DES ERREURS ===", ""]
        
        # Compter les types d'erreurs
        compteurs = {}
        for erreur in self.historique_erreurs:
            type_erreur = erreur['type']
            compteurs[type_erreur] = compteurs.get(type_erreur, 0) + 1
        
        rapport.append("RÉSUMÉ PAR TYPE D'ERREUR :")
        for type_err, count in sorted(compteurs.items()):
            rapport.append(f"  {type_err}: {count}")
        
        rapport.append("")
        rapport.append("DÉTAIL DES ERREURS :")
        
        for i, erreur in enumerate(self.historique_erreurs[-10:], 1):  # 10 dernières
            rapport.append(f"{i}. [{erreur['timestamp']}] {erreur['type']}")
            rapport.append(f"   Message: {erreur['message']}")
            if erreur['details']:
                details = ", ".join([f"{k}={v}" for k, v in erreur['details'].items()])
                rapport.append(f"   Détails: {details}")
            rapport.append("")
        
        return "\n".join(rapport)
    
    def sauvegarder_donnees(self, chemin_fichier: str):
        """Sauvegarde les données dans un fichier JSON."""
        try:
            donnees = {
                'livres': {isbn: livre.to_dict() for isbn, livre in self.livres.items()},
                'utilisateurs': {id_: utilisateur.to_dict() for id_, utilisateur in self.utilisateurs.items()},
                'emprunts': [emprunt.to_dict() for emprunt in self.emprunts],
                'configuration': self.configuration,
                'historique_erreurs': self.historique_erreurs
            }
            
            Path(chemin_fichier).parent.mkdir(parents=True, exist_ok=True)
            
            with open(chemin_fichier, 'w', encoding='utf-8') as f:
                json.dump(donnees, f, indent=2, ensure_ascii=False)
                
        except Exception as e:
            erreur = BibliothequeError(f"Erreur lors de la sauvegarde : {str(e)}")
            self._enregistrer_erreur(erreur)
            raise erreur


def interface_bibliotheque():
    """Interface interactive pour tester le système."""
    biblio = SystemeBibliotheque()
    
    print("=== SYSTÈME DE BIBLIOTHÈQUE ===")
    
    while True:
        print("\nMenu principal :")
        print("1. Ajouter un livre")
        print("2. Ajouter un utilisateur")
        print("3. Emprunter un livre")
        print("4. Retourner un livre")
        print("5. Rechercher des livres")
        print("6. Voir les emprunts en retard")
        print("7. Rapport des erreurs")
        print("8. Quitter")
        
        try:
            choix = input("\nVotre choix (1-8) : ").strip()
            
            if choix == '1':
                isbn = input("ISBN : ")
                titre = input("Titre : ")
                auteur = input("Auteur : ")
                annee = int(input("Année : "))
                genre = input("Genre (optionnel) : ") or None
                
                try:
                    livre = biblio.ajouter_livre(isbn, titre, auteur, annee, genre)
                    print(f"✅ Livre ajouté : {livre.titre}")
                except BibliothequeError as e:
                    print(f"❌ Erreur : {e}")
                    
            elif choix == '2':
                identifiant = input("Identifiant : ")
                nom = input("Nom : ")
                email = input("Email : ")
                
                try:
                    utilisateur = biblio.ajouter_utilisateur(identifiant, nom, email)
                    print(f"✅ Utilisateur ajouté : {utilisateur.nom}")
                except BibliothequeError as e:
                    print(f"❌ Erreur : {e}")
                    
            elif choix == '3':
                utilisateur_id = input("ID utilisateur : ")
                isbn = input("ISBN du livre : ")
                
                try:
                    emprunt = biblio.emprunter_livre(utilisateur_id, isbn)
                    print(f"✅ Emprunt effectué, retour prévu le {emprunt.date_retour_prevue.strftime('%d/%m/%Y')}")
                except BibliothequeError as e:
                    print(f"❌ Erreur : {e}")
                    
            elif choix == '4':
                utilisateur_id = input("ID utilisateur : ")
                isbn = input("ISBN du livre : ")
                
                try:
                    emprunt = biblio.retourner_livre(utilisateur_id, isbn)
                    if emprunt.amende > 0:
                        print(f"✅ Livre retourné avec amende : {emprunt.amende}€")
                    else:
                        print("✅ Livre retourné")
                except BibliothequeError as e:
                    print(f"❌ Erreur : {e}")
                    
            elif choix == '5':
                print("Critères de recherche (laisser vide pour ignorer) :")
                criteres = {}
                
                titre = input("Titre : ").strip()
                if titre:
                    criteres['titre'] = titre
                    
                auteur = input("Auteur : ").strip()
                if auteur:
                    criteres['auteur'] = auteur
                
                if criteres:
                    livres = biblio.rechercher_livre(**criteres)
                    if livres:
                        print(f"\n{len(livres)} livre(s) trouvé(s) :")
                        for livre in livres:
                            dispo = "✅" if livre.disponible else "❌"
                            print(f"  {dispo} {livre.titre} par {livre.auteur} ({livre.isbn})")
                    else:
                        print("Aucun livre trouvé")
                        
            elif choix == '6':
                retards = biblio.obtenir_emprunts_en_retard()
                if retards:
                    print(f"\n{len(retards)} emprunt(s) en retard :")
                    for emprunt in retards:
                        jours = emprunt.jours_retard()
                        amende = emprunt.calculer_amende()
                        print(f"  📚 {emprunt.isbn} par {emprunt.utilisateur_id} - {jours} jour(s) ({amende}€)")
                else:
                    print("Aucun emprunt en retard")
                    
            elif choix == '7':
                rapport = biblio.generer_rapport_erreurs()
                print(f"\n{rapport}")
                
            elif choix == '8':
                # Sauvegarder avant de quitter
                try:
                    biblio.sauvegarder_donnees("bibliotheque_data.json")
                    print("Données sauvegardées !")
                except Exception as e:
                    print(f"Erreur de sauvegarde : {e}")
                print("Au revoir !")
                break
            else:
                print("Choix invalide")
                
        except KeyboardInterrupt:
            print("\n\nAu revoir !")
            break
        except ValueError as e:
            print(f"❌ Erreur de saisie : {e}")
        except Exception as e:
            print(f"❌ Erreur inattendue : {e}")


# Tests
if __name__ == "__main__":
    print("=== Tests Correction Exercice 4 ===")
    
    biblio = SystemeBibliotheque()
    
    try:
        # Test ajout livres
        print("\n1. Test ajout de livres :")
        livre1 = biblio.ajouter_livre("978-2-07-036196-8", "1984", "George Orwell", 1949, "Dystopie")
        print(f"   ✅ Ajouté : {livre1.titre}")
        
        # Test ISBN invalide
        try:
            biblio.ajouter_livre("123", "Titre", "Auteur", 2000)
        except ISBNInvalideError as e:
            print(f"   ✅ ISBN invalide détecté : {e}")
        
        # Test livre existant
        try:
            biblio.ajouter_livre("978-2-07-036196-8", "Autre titre", "Autre auteur", 2000)
        except BibliothequeError as e:
            print(f"   ✅ Livre existant détecté : {e}")
        
        # Test ajout utilisateurs
        print("\n2. Test ajout d'utilisateurs :")
        user1 = biblio.ajouter_utilisateur("john_doe", "John Doe", "john@example.com")
        print(f"   ✅ Ajouté : {user1.nom}")
        
        # Test email invalide
        try:
            biblio.ajouter_utilisateur("jane", "Jane", "email_invalide")
        except DonneesInvalidesError as e:
            print(f"   ✅ Email invalide détecté : {e}")
        
        # Test emprunts
        print("\n3. Test emprunts :")
        emprunt1 = biblio.emprunter_livre("john_doe", "9782070361968")  # ISBN sans tirets
        print(f"   ✅ Emprunt effectué : {emprunt1.date_retour_prevue.strftime('%d/%m/%Y')}")
        
        # Test livre indisponible
        try:
            biblio.emprunter_livre("john_doe", "9782070361968")
        except LivreIndisponibleError as e:
            print(f"   ✅ Livre indisponible détecté : {e}")
        
        # Test retour
        print("\n4. Test retour :")
        retour = biblio.retourner_livre("john_doe", "9782070361968")
        print(f"   ✅ Retour effectué, amende : {retour.amende}€")
        
        print("\n5. Rapport des erreurs :")
        rapport = biblio.generer_rapport_erreurs()
        print(rapport)
        
        print("\n✅ Tous les tests réussis !")
        
    except Exception as e:
        print(f"\n❌ Erreur dans les tests : {e}")
    
    # Décommentez pour tester interactivement
    # interface_bibliotheque()
