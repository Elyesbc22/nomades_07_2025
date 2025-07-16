# Exercice 1: Classes de base et encapsulation
# 
# Dans cet exercice, vous allez créer une classe BankAccount (compte bancaire)
# qui démontre les concepts de base de la POO: constructeur, méthodes, et encapsulation.

class BankAccount:
    """
    Classe représentant un compte bancaire
    """
    
    def __init__(self, account_number, owner_name, initial_balance=0):
        """
        Constructeur de la classe BankAccount
        
        Args:
            account_number (str): Numéro du compte
            owner_name (str): Nom du propriétaire
            initial_balance (float): Solde initial (par défaut 0)
        """
        # TODO: Initialisez les attributs privés
        # - __account_number: numéro du compte (privé)
        # - __owner_name: nom du propriétaire (privé)  
        # - __balance: solde du compte (privé)
        pass
    
    def deposit(self, amount):
        """
        Effectue un dépôt sur le compte
        
        Args:
            amount (float): Montant à déposer
            
        Returns:
            bool: True si le dépôt est réussi, False sinon
        """
        # TODO: Vérifiez que le montant est positif
        # Si oui, ajoutez le montant au solde et retournez True
        # Sinon, affichez un message d'erreur et retournez False
        pass
    
    def withdraw(self, amount):
        """
        Effectue un retrait du compte
        
        Args:
            amount (float): Montant à retirer
            
        Returns:
            bool: True si le retrait est réussi, False sinon
        """
        # TODO: Vérifiez que le montant est positif et que le solde est suffisant
        # Si oui, soustrayez le montant du solde et retournez True
        # Sinon, affichez un message d'erreur approprié et retournez False
        pass
    
    def get_balance(self):
        """
        Retourne le solde actuel du compte
        
        Returns:
            float: Solde du compte
        """
        # TODO: Retournez le solde
        pass
    
    def get_account_info(self):
        """
        Retourne les informations du compte
        
        Returns:
            str: Informations formatées du compte
        """
        # TODO: Retournez une chaîne avec le numéro de compte, 
        # le propriétaire et le solde
        pass
    
    def __str__(self):
        """
        Représentation string du compte
        """
        # TODO: Utilisez get_account_info() pour retourner les informations
        pass

# Tests
if __name__ == "__main__":
    # Créer un compte
    compte1 = BankAccount("12345", "Alice Dupont", 1000)
    
    # Tester les opérations
    print("=== Test du compte bancaire ===")
    print(compte1)
    
    print("\n=== Test dépôt ===")
    success = compte1.deposit(500)
    print(f"Dépôt réussi: {success}")
    print(f"Nouveau solde: {compte1.get_balance()}")
    
    print("\n=== Test retrait ===")
    success = compte1.withdraw(200)
    print(f"Retrait réussi: {success}")
    print(f"Nouveau solde: {compte1.get_balance()}")
    
    print("\n=== Test retrait impossible ===")
    success = compte1.withdraw(2000)
    print(f"Retrait réussi: {success}")
    
    print("\n=== Test dépôt invalide ===")
    success = compte1.deposit(-100)
    print(f"Dépôt réussi: {success}")
