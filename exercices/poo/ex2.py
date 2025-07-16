# Exercice 2: Héritage et Polymorphisme
# 
# Dans cet exercice, vous allez créer une hiérarchie de classes pour représenter
# différents types de véhicules et démontrer l'héritage et le polymorphisme.

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
        # TODO: Initialisez les attributs
        self.brand = brand
        self.model = model
        self.year = year
        self.max_speed = max_speed
        self._current_speed = 0  # Vitesse actuelle (protégé)
    
    def start_engine(self):
        """Démarre le moteur"""
        # TODO: Implémentez cette méthode
        # Affichez un message générique de démarrage
        pass
    
    def accelerate(self, speed_increase):
        """
        Accélère le véhicule
        
        Args:
            speed_increase (int): Augmentation de vitesse
        """
        # TODO: Augmentez la vitesse actuelle sans dépasser la vitesse maximale
        pass
    
    def brake(self, speed_decrease):
        """
        Freine le véhicule
        
        Args:
            speed_decrease (int): Diminution de vitesse
        """
        # TODO: Diminuez la vitesse actuelle sans descendre en dessous de 0
        pass
    
    def get_info(self):
        """
        Retourne les informations du véhicule
        
        Returns:
            str: Informations formatées
        """
        # TODO: Retournez les informations du véhicule
        pass
    
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
        # TODO: Appelez le constructeur parent et initialisez les nouveaux attributs
        pass
    
    def start_engine(self):
        """Démarre le moteur de la voiture"""
        # TODO: Override cette méthode avec un message spécifique aux voitures
        pass
    
    def open_trunk(self):
        """Ouvre le coffre"""
        # TODO: Implémentez cette méthode spécifique aux voitures
        pass

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
        # TODO: Appelez le constructeur parent et initialisez engine_size
        pass
    
    def start_engine(self):
        """Démarre le moteur de la moto"""
        # TODO: Override cette méthode avec un message spécifique aux motos
        pass
    
    def wheelie(self):
        """Fait un wheelie"""
        # TODO: Implémentez cette méthode spécifique aux motos
        # Vérifiez que la vitesse est supérieure à 20 km/h
        pass

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
        # TODO: Appelez le constructeur parent et initialisez cargo_capacity
        pass
    
    def start_engine(self):
        """Démarre le moteur du camion"""
        # TODO: Override cette méthode avec un message spécifique aux camions
        pass
    
    def load_cargo(self, weight):
        """
        Charge du fret
        
        Args:
            weight (float): Poids à charger en tonnes
        """
        # TODO: Implémentez cette méthode
        # Vérifiez que le poids ne dépasse pas la capacité
        pass

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
    car.open_trunk()
    moto.accelerate(30)
    moto.wheelie()
    truck.load_cargo(20)
