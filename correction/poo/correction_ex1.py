# Correction Exercice 1: Classes de base et encapsulation
# 
# Correction complète de l'exercice sur les comptes bancaires

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
        # Initialisation des attributs privés
        self.__account_number = account_number
        self.__owner_name = owner_name
        self.__balance = initial_balance
    
    def deposit(self, amount):
        """
        Effectue un dépôt sur le compte
        
        Args:
            amount (float): Montant à déposer
            
        Returns:
            bool: True si le dépôt est réussi, False sinon
        """
        # Vérification que le montant est positif
        if amount <= 0:
            print("Erreur: Le montant doit être positif")
            return False
        
        # Ajout du montant au solde
        self.__balance += amount
        print(f"Dépôt de {amount}€ effectué avec succès")
        return True
    
    def withdraw(self, amount):
        """
        Effectue un retrait du compte
        
        Args:
            amount (float): Montant à retirer
            
        Returns:
            bool: True si le retrait est réussi, False sinon
        """
        # Vérification que le montant est positif
        if amount <= 0:
            print("Erreur: Le montant doit être positif")
            return False
        
        # Vérification que le solde est suffisant
        if amount > self.__balance:
            print(f"Erreur: Solde insuffisant. Solde actuel: {self.__balance}€")
            return False
        
        # Soustraction du montant du solde
        self.__balance -= amount
        print(f"Retrait de {amount}€ effectué avec succès")
        return True
    
    def get_balance(self):
        """
        Retourne le solde actuel du compte
        
        Returns:
            float: Solde du compte
        """
        return self.__balance
    
    def get_account_info(self):
        """
        Retourne les informations du compte
        
        Returns:
            str: Informations formatées du compte
        """
        return f"Compte {self.__account_number} - Propriétaire: {self.__owner_name} - Solde: {self.__balance}€"
    
    def __str__(self):
        """
        Représentation string du compte
        """
        return self.get_account_info()

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
    
    print("\n=== Démonstration de l'encapsulation ===")
    print("✓ Attributs privés protégés (__account_number, __owner_name, __balance)")
    print("✓ Accès contrôlé via des méthodes publiques")
    print("✓ Validation des données d'entrée")
    print("✓ Messages d'erreur informatifs")
    
    # Test d'accès direct aux attributs privés (ne fonctionne pas)
    try:
        print(compte1.__balance)  # Ceci va générer une erreur
    except AttributeError:
        print("✓ Impossible d'accéder directement aux attributs privés")
    
    # Accès via name mangling (possible mais non recommandé)
    print(f"Accès via name mangling: {compte1._BankAccount__balance}")
    print("Note: L'accès via name mangling est possible mais va à l'encontre de l'encapsulation")
