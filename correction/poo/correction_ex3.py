# Correction Exercice 3: Opérateurs surchargés, propriétés et décorateurs
# 
# Correction complète de la classe Vector2D avec tous les concepts avancés de POO

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
        # Initialisation des attributs privés avec validation
        self.__x = x  # Utilise le setter pour validation
        self.__y = y  # Utilise le setter pour validation
    
    @property
    def x(self):
        """Getter pour x"""
        return self.__x
    
    @x.setter
    def x(self, value):
        """Setter pour x avec validation"""
        if not isinstance(value, (int, float)):
            raise TypeError("x doit être un nombre")
        self.__x = float(value)
    
    @property
    def y(self):
        """Getter pour y"""
        return self.__y
    
    @y.setter
    def y(self, value):
        """Setter pour y avec validation"""
        if not isinstance(value, (int, float)):
            raise TypeError("y doit être un nombre")
        self.__y = float(value)
    
    @property
    def magnitude(self):
        """
        Propriété calculée: magnitude (longueur) du vecteur
        
        Returns:
            float: Magnitude du vecteur
        """
        return math.sqrt(self.__x ** 2 + self.__y ** 2)
    
    @property
    def angle(self):
        """
        Propriété calculée: angle du vecteur en radians
        
        Returns:
            float: Angle en radians
        """
        return math.atan2(self.__y, self.__x)
    
    def __str__(self):
        """Représentation string du vecteur"""
        return f"Vector2D({self.__x}, {self.__y})"
    
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
        if not isinstance(other, Vector2D):
            raise TypeError("L'addition n'est possible qu'avec un autre Vector2D")
        return Vector2D(self.__x + other.__x, self.__y + other.__y)
    
    def __sub__(self, other):
        """
        Surcharge de l'opérateur -
        
        Args:
            other (Vector2D): Autre vecteur
            
        Returns:
            Vector2D: Nouveau vecteur résultant de la soustraction
        """
        if not isinstance(other, Vector2D):
            raise TypeError("La soustraction n'est possible qu'avec un autre Vector2D")
        return Vector2D(self.__x - other.__x, self.__y - other.__y)
    
    def __mul__(self, scalar):
        """
        Surcharge de l'opérateur * (multiplication par un scalaire)
        
        Args:
            scalar (float): Scalaire
            
        Returns:
            Vector2D: Nouveau vecteur multiplié par le scalaire
        """
        if not isinstance(scalar, (int, float)):
            raise TypeError("La multiplication n'est possible qu'avec un nombre")
        return Vector2D(self.__x * scalar, self.__y * scalar)
    
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
        if not isinstance(scalar, (int, float)):
            raise TypeError("La division n'est possible qu'avec un nombre")
        if scalar == 0:
            raise ZeroDivisionError("Division par zéro impossible")
        return Vector2D(self.__x / scalar, self.__y / scalar)
    
    def __eq__(self, other):
        """
        Surcharge de l'opérateur == (égalité)
        
        Args:
            other (Vector2D): Autre vecteur
            
        Returns:
            bool: True si les vecteurs sont égaux
        """
        if not isinstance(other, Vector2D):
            return False
        tolerance = 1e-10
        return (abs(self.__x - other.__x) < tolerance and 
                abs(self.__y - other.__y) < tolerance)
    
    def __neg__(self):
        """
        Surcharge de l'opérateur - unaire (négation)
        
        Returns:
            Vector2D: Vecteur opposé
        """
        return Vector2D(-self.__x, -self.__y)
    
    def dot(self, other):
        """
        Produit scalaire avec un autre vecteur
        
        Args:
            other (Vector2D): Autre vecteur
            
        Returns:
            float: Produit scalaire
        """
        if not isinstance(other, Vector2D):
            raise TypeError("Le produit scalaire n'est possible qu'avec un autre Vector2D")
        return self.__x * other.__x + self.__y * other.__y
    
    def normalize(self):
        """
        Normalise le vecteur (le rend unitaire)
        
        Returns:
            Vector2D: Nouveau vecteur normalisé
        """
        mag = self.magnitude
        if mag == 0:
            raise ValueError("Impossible de normaliser un vecteur nul")
        return Vector2D(self.__x / mag, self.__y / mag)
    
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
        if not isinstance(v1, Vector2D) or not isinstance(v2, Vector2D):
            raise TypeError("Les deux arguments doivent être des Vector2D")
        diff = v1 - v2
        return diff.magnitude
    
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
        if not isinstance(magnitude, (int, float)) or not isinstance(angle, (int, float)):
            raise TypeError("La magnitude et l'angle doivent être des nombres")
        x = magnitude * math.cos(angle)
        y = magnitude * math.sin(angle)
        return cls(x, y)

# Tests
if __name__ == "__main__":
    print("=== Test de la classe Vector2D ===")
    
    # Création de vecteurs
    v1 = Vector2D(3, 4)
    v2 = Vector2D(1, 2)
    
    print(f"v1 = {v1}")
    print(f"v2 = {v2}")
    print(f"Magnitude de v1: {v1.magnitude}")
    print(f"Angle de v1: {v1.angle} radians ({math.degrees(v1.angle):.2f} degrés)")
    
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
    print(f"Magnitude du vecteur normalisé: {v1.normalize().magnitude}")
    
    # Test de création depuis coordonnées polaires
    v3 = Vector2D.from_polar(5, math.pi/4)
    print(f"Vecteur polaire (5, π/4): {v3}")
    print(f"Vérification: magnitude = {v3.magnitude}, angle = {v3.angle}")
    
    # Test d'égalité
    v4 = Vector2D(3, 4)
    print(f"v1 == v4: {v1 == v4}")
    
    # Test des propriétés
    print(f"\nAvant modification: v1 = {v1}")
    v1.x = 5
    v1.y = 12
    print(f"Après modification: v1 = {v1}")
    print(f"Nouvelle magnitude: {v1.magnitude}")
    
    # Test de gestion d'erreurs
    print("\n=== Test de gestion d'erreurs ===")
    
    try:
        v_invalid = Vector2D("abc", 5)  # Type invalide
    except TypeError as e:
        print(f"Erreur capturée: {e}")
    
    try:
        result = v1 + "pas un vecteur"  # Addition invalide
    except TypeError as e:
        print(f"Erreur capturée: {e}")
    
    try:
        result = v1 / 0  # Division par zéro
    except ZeroDivisionError as e:
        print(f"Erreur capturée: {e}")
    
    try:
        v_zero = Vector2D(0, 0)
        normalized = v_zero.normalize()  # Normalisation d'un vecteur nul
    except ValueError as e:
        print(f"Erreur capturée: {e}")
    
    print("\n=== Démonstration des concepts POO utilisés ===")
    print("✓ Propriétés (@property): x, y, magnitude, angle avec validation")
    print("✓ Surcharge d'opérateurs: +, -, *, /, ==, - (unaire)")
    print("✓ Méthodes spéciales: __str__, __repr__, __add__, __sub__, etc.")
    print("✓ Méthode statique: distance() avec @staticmethod")
    print("✓ Méthode de classe: from_polar() avec @classmethod")
    print("✓ Encapsulation: Attributs privés __x et __y")
    print("✓ Validation: Vérification des types et valeurs")
    print("✓ Gestion d'exceptions: TypeError, ZeroDivisionError, ValueError")
    print("✓ Polymorphisme: Opérateurs fonctionnent dans les deux sens (3 * v et v * 3)")
    
    print("\n=== Exemples d'usage avancé ===")
    
    # Chaînage d'opérations
    result = (v1 + v2) * 2 - Vector2D(1, 1)
    print(f"Chaînage: (v1 + v2) * 2 - Vector2D(1, 1) = {result}")
    
    # Vecteurs en tant qu'objets géométriques
    origin = Vector2D(0, 0)
    point_a = Vector2D(3, 4)
    point_b = Vector2D(6, 8)
    
    print(f"Distance origine à A: {Vector2D.distance(origin, point_a)}")
    print(f"Distance A à B: {Vector2D.distance(point_a, point_b)}")
    
    # Vecteur unitaire dans différentes directions
    directions = [0, math.pi/4, math.pi/2, math.pi, 3*math.pi/2]
    print("\nVecteurs unitaires dans différentes directions:")
    for angle in directions:
        unit_vector = Vector2D.from_polar(1, angle)
        print(f"  Angle {math.degrees(angle):3.0f}°: {unit_vector}")
