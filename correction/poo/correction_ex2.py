# Correction Exercice 2: Héritage et Polymorphisme
# 
# Correction complète de l'exercice sur la hiérarchie de véhicules

class Vehicle:
    """
    Classe de base pour tous les véhicules
    """
    
    def __init__(self, brand, model, year, max_speed):
        """
        Constructeur de la classe Vehicle
        
        Args:
            brand (str): Marque du véhicule
            model (str): Modèle du véhicule
            year (int): Année de fabrication
            max_speed (int): Vitesse maximale en km/h
        """
        self.brand = brand
        self.model = model
        self.year = year
        self.max_speed = max_speed
        self._current_speed = 0  # Vitesse actuelle (protégé)
    
    def start_engine(self):
        """Démarre le moteur"""
        print(f"Le moteur du {self.brand} {self.model} démarre...")
    
    def accelerate(self, speed_increase):
        """
        Accélère le véhicule
        
        Args:
            speed_increase (int): Augmentation de vitesse
        """
        new_speed = self._current_speed + speed_increase
        if new_speed > self.max_speed:
            self._current_speed = self.max_speed
            print(f"Vitesse maximale atteinte: {self.max_speed} km/h")
        else:
            self._current_speed = new_speed
            print(f"Accélération: nouvelle vitesse {self._current_speed} km/h")
    
    def brake(self, speed_decrease):
        """
        Freine le véhicule
        
        Args:
            speed_decrease (int): Diminution de vitesse
        """
        new_speed = self._current_speed - speed_decrease
        if new_speed < 0:
            self._current_speed = 0
            print("Véhicule arrêté")
        else:
            self._current_speed = new_speed
            print(f"Freinage: nouvelle vitesse {self._current_speed} km/h")
    
    def get_info(self):
        """
        Retourne les informations du véhicule
        
        Returns:
            str: Informations formatées
        """
        return f"{self.brand} {self.model} ({self.year}) - Vitesse max: {self.max_speed} km/h - Vitesse actuelle: {self._current_speed} km/h"
    
    def __str__(self):
        return self.get_info()

class Car(Vehicle):
    """
    Classe représentant une voiture
    """
    
    def __init__(self, brand, model, year, max_speed, doors, fuel_type):
        """
        Constructeur de la classe Car
        
        Args:
            doors (int): Nombre de portes
            fuel_type (str): Type de carburant (essence, diesel, électrique)
        """
        # Appel du constructeur parent
        super().__init__(brand, model, year, max_speed)
        self.doors = doors
        self.fuel_type = fuel_type
    
    def start_engine(self):
        """Démarre le moteur de la voiture"""
        print(f"🚗 La voiture {self.brand} {self.model} ({self.fuel_type}) démarre en douceur...")
    
    def open_trunk(self):
        """Ouvre le coffre"""
        print(f"Le coffre de la {self.brand} {self.model} s'ouvre")
    
    def get_info(self):
        """Override pour ajouter les informations spécifiques à la voiture"""
        base_info = super().get_info()
        return f"{base_info} - {self.doors} portes - Carburant: {self.fuel_type}"

class Motorcycle(Vehicle):
    """
    Classe représentant une moto
    """
    
    def __init__(self, brand, model, year, max_speed, engine_size):
        """
        Constructeur de la classe Motorcycle
        
        Args:
            engine_size (int): Cylindrée en cm³
        """
        # Appel du constructeur parent
        super().__init__(brand, model, year, max_speed)
        self.engine_size = engine_size
    
    def start_engine(self):
        """Démarre le moteur de la moto"""
        print(f"🏍️ La moto {self.brand} {self.model} rugit avec ses {self.engine_size}cm³!")
    
    def wheelie(self):
        """Fait un wheelie"""
        if self._current_speed < 20:
            print("Impossible de faire un wheelie, vitesse trop faible (minimum 20 km/h)")
        else:
            print(f"🤸 Wheelie spectaculaire avec la {self.brand} {self.model} à {self._current_speed} km/h!")
    
    def get_info(self):
        """Override pour ajouter les informations spécifiques à la moto"""
        base_info = super().get_info()
        return f"{base_info} - Cylindrée: {self.engine_size}cm³"

class Truck(Vehicle):
    """
    Classe représentant un camion
    """
    
    def __init__(self, brand, model, year, max_speed, cargo_capacity):
        """
        Constructeur de la classe Truck
        
        Args:
            cargo_capacity (float): Capacité de chargement en tonnes
        """
        # Appel du constructeur parent
        super().__init__(brand, model, year, max_speed)
        self.cargo_capacity = cargo_capacity
        self.current_load = 0  # Charge actuelle
    
    def start_engine(self):
        """Démarre le moteur du camion"""
        print(f"🚛 Le camion {self.brand} {self.model} démarre avec un grondement puissant...")
    
    def load_cargo(self, weight):
        """
        Charge du fret
        
        Args:
            weight (float): Poids à charger en tonnes
        """
        if weight <= 0:
            print("Erreur: Le poids doit être positif")
            return False
        
        if self.current_load + weight > self.cargo_capacity:
            print(f"Erreur: Dépassement de capacité. Capacité: {self.cargo_capacity}t, Charge actuelle: {self.current_load}t")
            return False
        
        self.current_load += weight
        print(f"Chargement de {weight}t réussi. Charge totale: {self.current_load}t / {self.cargo_capacity}t")
        return True
    
    def get_info(self):
        """Override pour ajouter les informations spécifiques au camion"""
        base_info = super().get_info()
        return f"{base_info} - Capacité: {self.cargo_capacity}t - Charge: {self.current_load}t"

def test_polymorphism(vehicles):
    """
    Teste le polymorphisme avec une liste de véhicules
    
    Args:
        vehicles (list): Liste de véhicules
    """
    print("=== Test du polymorphisme ===")
    for vehicle in vehicles:
        print(f"\n{vehicle}")
        vehicle.start_engine()
        vehicle.accelerate(50)
        print(f"Vitesse actuelle: {vehicle._current_speed} km/h")

# Tests
if __name__ == "__main__":
    # Créer différents véhicules
    car = Car("Toyota", "Corolla", 2020, 180, 4, "essence")
    moto = Motorcycle("Yamaha", "R1", 2021, 300, 1000)
    truck = Truck("Mercedes", "Actros", 2019, 120, 25)
    
    # Test du polymorphisme
    vehicles = [car, moto, truck]
    test_polymorphism(vehicles)
    
    # Tests spécifiques
    print("\n=== Tests spécifiques ===")
    
    print("\n--- Test voiture ---")
    car.open_trunk()
    car.accelerate(100)
    car.brake(50)
    
    print("\n--- Test moto ---")
    moto.accelerate(30)
    moto.wheelie()
    moto.accelerate(50)  # Pour atteindre plus de 20 km/h
    moto.wheelie()
    
    print("\n--- Test camion ---")
    truck.load_cargo(20)
    truck.load_cargo(8)  # Ceci devrait échouer
    truck.load_cargo(5)  # Ceci devrait réussir
    
    print("\n=== Démonstration des concepts POO ===")
    print("✓ Héritage: Car, Motorcycle, Truck héritent de Vehicle")
    print("✓ Polymorphisme: Même interface (start_engine) avec des comportements différents")
    print("✓ Surcharge de méthodes: start_engine() redéfinie dans chaque classe fille")
    print("✓ Appel au parent: super().__init__() et super().get_info()")
    print("✓ Attributs protégés: _current_speed accessible aux classes filles")
    print("✓ Encapsulation: Méthodes spécifiques à chaque type de véhicule")
