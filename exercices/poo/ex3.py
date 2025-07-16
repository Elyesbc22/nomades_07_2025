# Exercice 3: Opérateurs surchargés, propriétés et décorateurs
# 
# Dans cet exercice, vous allez créer une classe Vector2D qui démontre
# la surcharge d'opérateurs, les propriétés et les décorateurs.

import math

class Vector2D:
    """
    Classe représentant un vecteur 2D avec surcharge d'opérateurs
    """
    
    def __init__(self, x=0, y=0):
        """
        Constructeur du vecteur 2D
        
        Args:
            x (float): Composante x
            y (float): Composante y
        """
        # TODO: Initialisez les attributs privés __x et __y
        pass
    
    @property
    def x(self):
        """Getter pour x"""
        # TODO: Retournez __x
        pass
    
    @x.setter
    def x(self, value):
        """Setter pour x avec validation"""
        # TODO: Vérifiez que value est un nombre et assignez à __x
        pass
    
    @property
    def y(self):
        """Getter pour y"""
        # TODO: Retournez __y
        pass
    
    @y.setter
    def y(self, value):
        """Setter pour y avec validation"""
        # TODO: Vérifiez que value est un nombre et assignez à __y
        pass
    
    @property
    def magnitude(self):
        """
        Propriété calculée: magnitude (longueur) du vecteur
        
        Returns:
            float: Magnitude du vecteur
        """
        # TODO: Calculez et retournez la magnitude sqrt(x² + y²)
        pass
    
    @property
    def angle(self):
        """
        Propriété calculée: angle du vecteur en radians
        
        Returns:
            float: Angle en radians
        """
        # TODO: Calculez et retournez l'angle avec math.atan2(y, x)
        pass
    
    def __str__(self):
        """Représentation string du vecteur"""
        # TODO: Retournez une représentation comme "Vector2D(x, y)"
        pass
    
    def __repr__(self):
        """Représentation pour le débogage"""
        return self.__str__()
    
    def __add__(self, other):
        """
        Surcharge de l'opérateur +
        
        Args:
            other (Vector2D): Autre vecteur
            
        Returns:
            Vector2D: Nouveau vecteur résultant de l'addition
        """
        # TODO: Vérifiez que other est un Vector2D
        # Retournez un nouveau Vector2D avec la somme des composantes
        pass
    
    def __sub__(self, other):
        """
        Surcharge de l'opérateur -
        
        Args:
            other (Vector2D): Autre vecteur
            
        Returns:
            Vector2D: Nouveau vecteur résultant de la soustraction
        """
        # TODO: Implémentez la soustraction de vecteurs
        pass
    
    def __mul__(self, scalar):
        """
        Surcharge de l'opérateur * (multiplication par un scalaire)
        
        Args:
            scalar (float): Scalaire
            
        Returns:
            Vector2D: Nouveau vecteur multiplié par le scalaire
        """
        # TODO: Vérifiez que scalar est un nombre
        # Retournez un nouveau Vector2D avec les composantes multipliées
        pass
    
    def __rmul__(self, scalar):
        """Multiplication par un scalaire (ordre inversé)"""
        return self.__mul__(scalar)
    
    def __truediv__(self, scalar):
        """
        Surcharge de l'opérateur / (division par un scalaire)
        
        Args:
            scalar (float): Scalaire (non nul)
            
        Returns:
            Vector2D: Nouveau vecteur divisé par le scalaire
        """
        # TODO: Vérifiez que scalar n'est pas zéro
        # Retournez un nouveau Vector2D avec les composantes divisées
        pass
    
    def __eq__(self, other):
        """
        Surcharge de l'opérateur == (égalité)
        
        Args:
            other (Vector2D): Autre vecteur
            
        Returns:
            bool: True si les vecteurs sont égaux
        """
        # TODO: Comparez les composantes x et y avec une tolérance
        pass
    
    def __neg__(self):
        """
        Surcharge de l'opérateur - unaire (négation)
        
        Returns:
            Vector2D: Vecteur opposé
        """
        # TODO: Retournez un nouveau Vector2D avec les composantes négatives
        pass
    
    def dot(self, other):
        """
        Produit scalaire avec un autre vecteur
        
        Args:
            other (Vector2D): Autre vecteur
            
        Returns:
            float: Produit scalaire
        """
        # TODO: Calculez et retournez le produit scalaire (x1*x2 + y1*y2)
        pass
    
    def normalize(self):
        """
        Normalise le vecteur (le rend unitaire)
        
        Returns:
            Vector2D: Nouveau vecteur normalisé
        """
        # TODO: Divisez le vecteur par sa magnitude
        # Attention au cas où la magnitude est zéro
        pass
    
    @staticmethod
    def distance(v1, v2):
        """
        Calcule la distance entre deux vecteurs
        
        Args:
            v1 (Vector2D): Premier vecteur
            v2 (Vector2D): Deuxième vecteur
            
        Returns:
            float: Distance entre les vecteurs
        """
        # TODO: Calculez la distance euclidienne entre v1 et v2
        pass
    
    @classmethod
    def from_polar(cls, magnitude, angle):
        """
        Crée un vecteur à partir de coordonnées polaires
        
        Args:
            magnitude (float): Magnitude du vecteur
            angle (float): Angle en radians
            
        Returns:
            Vector2D: Nouveau vecteur
        """
        # TODO: Convertissez les coordonnées polaires en cartésiennes
        # x = magnitude * cos(angle), y = magnitude * sin(angle)
        pass

# Tests
if __name__ == "__main__":
    print("=== Test de la classe Vector2D ===")
    
    # Création de vecteurs
    v1 = Vector2D(3, 4)
    v2 = Vector2D(1, 2)
    
    print(f"v1 = {v1}")
    print(f"v2 = {v2}")
    print(f"Magnitude de v1: {v1.magnitude}")
    print(f"Angle de v1: {v1.angle} radians")
    
    # Test des opérateurs
    print(f"\nv1 + v2 = {v1 + v2}")
    print(f"v1 - v2 = {v1 - v2}")
    print(f"v1 * 2 = {v1 * 2}")
    print(f"3 * v2 = {3 * v2}")
    print(f"v1 / 2 = {v1 / 2}")
    print(f"-v1 = {-v1}")
    
    # Test des méthodes
    print(f"\nProduit scalaire v1.v2: {v1.dot(v2)}")
    print(f"Distance entre v1 et v2: {Vector2D.distance(v1, v2)}")
    print(f"v1 normalisé: {v1.normalize()}")
    
    # Test de création depuis coordonnées polaires
    v3 = Vector2D.from_polar(5, math.pi/4)
    print(f"Vecteur polaire (5, π/4): {v3}")
    
    # Test d'égalité
    v4 = Vector2D(3, 4)
    print(f"v1 == v4: {v1 == v4}")
    
    # Test des propriétés
    v1.x = 5
    v1.y = 12
    print(f"v1 modifié: {v1}")
    print(f"Nouvelle magnitude: {v1.magnitude}")
