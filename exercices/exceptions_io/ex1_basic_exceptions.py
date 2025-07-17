"""
Exercice 1 : Gestion basique des exceptions
==========================================

Objectifs :
- Comprendre les différents types d'exceptions
- Utiliser try/except/else/finally
- Gérer les exceptions spécifiques

Instructions :
Complétez les fonctions ci-dessous en gérant correctement les exceptions.
"""

def division_securisee(a, b):
    """
    Effectue une division sécurisée entre deux nombres.
    
    Args:
        a (float): Le dividende
        b (float): Le diviseur
    
    Returns:
        float: Le résultat de la division ou None si erreur
        
    Exceptions à gérer :
    - ZeroDivisionError : retourner None
    - TypeError : retourner None
    
    Exemple :
        >>> division_securisee(10, 2)
        5.0
        >>> division_securisee(10, 0)
        None
        >>> division_securisee("10", 2)
        None
    """
    # TODO: Implémentez cette fonction
    pass


def acces_liste_securise(liste, index):
    """
    Accède à un élément d'une liste de manière sécurisée.
    
    Args:
        liste (list): La liste
        index (int): L'index à accéder
    
    Returns:
        any: L'élément à l'index donné ou "Index invalide" si erreur
        
    Exceptions à gérer :
    - IndexError : retourner "Index invalide"
    - TypeError : retourner "Type invalide"
    
    Exemple :
        >>> acces_liste_securise([1, 2, 3], 1)
        2
        >>> acces_liste_securise([1, 2, 3], 5)
        'Index invalide'
    """
    # TODO: Implémentez cette fonction
    pass


def convertir_entier(valeur):
    """
    Convertit une valeur en entier avec gestion d'erreurs.
    
    Args:
        valeur (any): La valeur à convertir
    
    Returns:
        tuple: (succès: bool, résultat: int ou message d'erreur: str)
        
    Exemple :
        >>> convertir_entier("123")
        (True, 123)
        >>> convertir_entier("abc")
        (False, "Conversion impossible")
        >>> convertir_entier(12.5)
        (True, 12)
    """
    # TODO: Implémentez cette fonction
    # Utilisez try/except/else pour une gestion propre
    pass


def calculatrice_robuste():
    """
    Une calculatrice interactive qui gère les erreurs.
    
    Demande à l'utilisateur :
    1. Deux nombres
    2. Une opération (+, -, *, /)
    
    Affiche le résultat ou un message d'erreur approprié.
    Continue jusqu'à ce que l'utilisateur tape 'quit'.
    
    Exceptions à gérer :
    - ValueError pour les conversions
    - ZeroDivisionError pour la division par zéro
    - KeyboardInterrupt pour Ctrl+C
    """
    operations = {
        '+': lambda x, y: x + y,
        '-': lambda x, y: x - y,
        '*': lambda x, y: x * y,
        '/': lambda x, y: x / y
    }
    
    print("Calculatrice (tapez 'quit' pour quitter)")
    
    # TODO: Implémentez la boucle principale
    # Gérez toutes les exceptions possibles
    pass


# Tests
if __name__ == "__main__":
    print("=== Tests Exercice 1 ===")
    
    # Test division_securisee
    print("1. Tests division_securisee :")
    print(f"   10 / 2 = {division_securisee(10, 2)}")  # Attendu: 5.0
    print(f"   10 / 0 = {division_securisee(10, 0)}")  # Attendu: None
    print(f"   '10' / 2 = {division_securisee('10', 2)}")  # Attendu: None
    
    # Test acces_liste_securise
    print("\n2. Tests acces_liste_securise :")
    liste_test = [10, 20, 30]
    print(f"   liste[1] = {acces_liste_securise(liste_test, 1)}")  # Attendu: 20
    print(f"   liste[5] = {acces_liste_securise(liste_test, 5)}")  # Attendu: "Index invalide"
    print(f"   liste['a'] = {acces_liste_securise(liste_test, 'a')}")  # Attendu: "Type invalide"
    
    # Test convertir_entier
    print("\n3. Tests convertir_entier :")
    print(f"   '123' -> {convertir_entier('123')}")  # Attendu: (True, 123)
    print(f"   'abc' -> {convertir_entier('abc')}")  # Attendu: (False, "Conversion impossible")
    print(f"   12.7 -> {convertir_entier(12.7)}")  # Attendu: (True, 12)
    
    # Test calculatrice (décommentez pour tester interactivement)
    # calculatrice_robuste()
