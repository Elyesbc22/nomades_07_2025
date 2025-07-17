"""
Correction complète - Exercice 1 : Gestion basique des exceptions
=================================================================

Cette correction montre les solutions complètes pour l'exercice 1.
"""

def division_securisee(a, b):
    """
    Effectue une division sécurisée entre deux nombres.
    
    Args:
        a (float): Le dividende
        b (float): Le diviseur
    
    Returns:
        float: Le résultat de la division ou None si erreur
    """
    try:
        # Tentative de conversion et division
        resultat = float(a) / float(b)
        return resultat
    except ZeroDivisionError:
        # Division par zéro
        return None
    except (TypeError, ValueError):
        # Types incompatibles ou conversion impossible
        return None


def acces_liste_securise(liste, index):
    """
    Accède à un élément d'une liste de manière sécurisée.
    
    Args:
        liste (list): La liste
        index (int): L'index à accéder
    
    Returns:
        any: L'élément à l'index donné ou message d'erreur
    """
    try:
        return liste[index]
    except IndexError:
        return "Index invalide"
    except TypeError:
        return "Type invalide"


def convertir_entier(valeur):
    """
    Convertit une valeur en entier avec gestion d'erreurs.
    
    Args:
        valeur (any): La valeur à convertir
    
    Returns:
        tuple: (succès: bool, résultat: int ou message d'erreur: str)
    """
    try:
        resultat = int(valeur)
    except (ValueError, TypeError):
        return (False, "Conversion impossible")
    else:
        # Exécuté seulement si aucune exception n'a été levée
        return (True, resultat)


def calculatrice_robuste():
    """
    Une calculatrice interactive qui gère les erreurs.
    """
    operations = {
        '+': lambda x, y: x + y,
        '-': lambda x, y: x - y,
        '*': lambda x, y: x * y,
        '/': lambda x, y: x / y
    }
    
    print("Calculatrice (tapez 'quit' pour quitter)")
    
    while True:
        try:
            # Demander l'entrée utilisateur
            entree = input("\nEntrez votre calcul (ex: 5 + 3) : ").strip()
            
            if entree.lower() == 'quit':
                print("Au revoir !")
                break
            
            # Parser l'entrée (format : nombre opérateur nombre)
            parties = entree.split()
            if len(parties) != 3:
                print("Format attendu : nombre opérateur nombre (ex: 5 + 3)")
                continue
            
            # Extraire les composants
            nombre1_str, operateur, nombre2_str = parties
            
            # Convertir les nombres
            nombre1 = float(nombre1_str)
            nombre2 = float(nombre2_str)
            
            # Vérifier l'opérateur
            if operateur not in operations:
                print(f"Opérateur '{operateur}' non supporté. Utilisez +, -, *, /")
                continue
            
            # Effectuer le calcul
            resultat = operations[operateur](nombre1, nombre2)
            print(f"Résultat : {nombre1} {operateur} {nombre2} = {resultat}")
            
        except ValueError:
            print("Erreur : Veuillez entrer des nombres valides")
        except ZeroDivisionError:
            print("Erreur : Division par zéro impossible")
        except KeyboardInterrupt:
            print("\n\nArrêt demandé par l'utilisateur (Ctrl+C)")
            break
        except Exception as e:
            print(f"Erreur inattendue : {str(e)}")


# Bonus : Version avancée avec exceptions personnalisées
class CalculatriceError(Exception):
    """Exception personnalisée pour la calculatrice."""
    pass

class OperateurInvalideError(CalculatriceError):
    """Exception pour un opérateur invalide."""
    pass

class NombreInvalideError(CalculatriceError):
    """Exception pour un nombre invalide."""
    pass


def calculatrice_avancee():
    """Version avancée avec exceptions personnalisées et plus d'opérateurs."""
    operations = {
        '+': lambda x, y: x + y,
        '-': lambda x, y: x - y,
        '*': lambda x, y: x * y,
        '/': lambda x, y: x / y,
        '**': lambda x, y: x ** y,
        '%': lambda x, y: x % y
    }
    
    def valider_nombre(nombre_str):
        """Valide et convertit une chaîne en nombre."""
        try:
            return float(nombre_str)
        except ValueError:
            raise NombreInvalideError(f"'{nombre_str}' n'est pas un nombre valide")
    
    def valider_operateur(operateur):
        """Valide un opérateur."""
        if operateur not in operations:
            operateurs_valides = ', '.join(operations.keys())
            raise OperateurInvalideError(
                f"Opérateur '{operateur}' invalide. "
                f"Opérateurs valides : {operateurs_valides}"
            )
        return operateur
    
    print("Calculatrice avancée (tapez 'quit' pour quitter)")
    print("Opérateurs supportés : +, -, *, /, **, %")
    
    while True:
        try:
            entree = input("\nCalcul : ").strip()
            
            if entree.lower() == 'quit':
                break
            
            # Parser l'entrée
            parties = entree.split()
            if len(parties) != 3:
                raise CalculatriceError("Format attendu : nombre opérateur nombre")
            
            # Valider et convertir
            nombre1 = valider_nombre(parties[0])
            operateur = valider_operateur(parties[1])
            nombre2 = valider_nombre(parties[2])
            
            # Vérifications spéciales
            if operateur == '/' and nombre2 == 0:
                raise ZeroDivisionError("Division par zéro impossible")
            if operateur == '%' and nombre2 == 0:
                raise ZeroDivisionError("Modulo par zéro impossible")
            
            # Effectuer le calcul
            resultat = operations[operateur](nombre1, nombre2)
            print(f"Résultat : {nombre1} {operateur} {nombre2} = {resultat}")
            
        except CalculatriceError as e:
            print(f"Erreur de calculatrice : {e}")
        except ZeroDivisionError as e:
            print(f"Erreur mathématique : {e}")
        except KeyboardInterrupt:
            print("\n\nAu revoir !")
            break
        except Exception as e:
            print(f"Erreur inattendue : {e}")


def lire_fichier_avec_gestion_erreurs(nom_fichier):
    """
    Exemple complet de lecture de fichier avec gestion d'erreurs.
    
    Args:
        nom_fichier (str): Nom du fichier à lire
    
    Returns:
        tuple: (succès: bool, contenu: str ou message d'erreur: str)
    """
    try:
        with open(nom_fichier, 'r', encoding='utf-8') as fichier:
            contenu = fichier.read()
    except FileNotFoundError:
        return (False, f"Le fichier '{nom_fichier}' n'existe pas")
    except PermissionError:
        return (False, f"Permission refusée pour lire '{nom_fichier}'")
    except UnicodeDecodeError:
        return (False, f"Erreur d'encodage lors de la lecture de '{nom_fichier}'")
    except Exception as e:
        return (False, f"Erreur inattendue : {str(e)}")
    else:
        # Succès - aucune exception levée
        return (True, contenu)
    finally:
        # Cette section s'exécute toujours
        print(f"Tentative de lecture du fichier '{nom_fichier}' terminée")


def gestionnaire_exceptions_complete():
    """
    Exemple complet montrant différents types d'exceptions et leur gestion.
    """
    exemples = [
        # (description, fonction_test)
        ("Division par zéro", lambda: 10 / 0),
        ("Index hors limites", lambda: [1, 2, 3][10]),
        ("Clé inexistante", lambda: {'a': 1}['b']),
        ("Conversion impossible", lambda: int('abc')),
        ("Attribut inexistant", lambda: getattr(42, 'inexistant')),
        ("Import impossible", lambda: __import__('module_inexistant')),
    ]
    
    print("=== Démonstration de gestion d'exceptions ===")
    
    for description, fonction_test in exemples:
        print(f"\nTest : {description}")
        try:
            resultat = fonction_test()
            print(f"Résultat inattendu : {resultat}")
        except ZeroDivisionError:
            print("  → ZeroDivisionError capturée : Division par zéro")
        except IndexError:
            print("  → IndexError capturée : Index hors limites")
        except KeyError as e:
            print(f"  → KeyError capturée : Clé {e} inexistante")
        except ValueError as e:
            print(f"  → ValueError capturée : {e}")
        except AttributeError as e:
            print(f"  → AttributeError capturée : {e}")
        except ImportError as e:
            print(f"  → ImportError capturée : {e}")
        except Exception as e:
            print(f"  → Exception générale capturée : {type(e).__name__}: {e}")


if __name__ == "__main__":
    print("=== Tests Correction Exercice 1 ===")
    
    # Test des fonctions de base
    print("1. Test division_securisee :")
    print(f"   10 / 2 = {division_securisee(10, 2)}")
    print(f"   10 / 0 = {division_securisee(10, 0)}")
    print(f"   'abc' / 2 = {division_securisee('abc', 2)}")
    
    print("\n2. Test acces_liste_securise :")
    liste_test = [10, 20, 30]
    print(f"   liste[1] = {acces_liste_securise(liste_test, 1)}")
    print(f"   liste[5] = {acces_liste_securise(liste_test, 5)}")
    print(f"   liste['a'] = {acces_liste_securise(liste_test, 'a')}")
    
    print("\n3. Test convertir_entier :")
    print(f"   '123' -> {convertir_entier('123')}")
    print(f"   'abc' -> {convertir_entier('abc')}")
    print(f"   12.7 -> {convertir_entier(12.7)}")
    
    # Démonstration des exceptions
    print("\n4. Démonstration des exceptions :")
    gestionnaire_exceptions_complete()
    
    print("\n5. Tests terminés avec succès !")
    
    # Décommentez pour tester interactivement
    # calculatrice_robuste()
    # calculatrice_avancee()
