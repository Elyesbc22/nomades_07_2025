from slot import Slot

class Planning:
    def __init__(self, all_doctors, slots: list[Slot]):
        """
        Initialise le planning

        Args:
            all_doctors (list[Doctor]): Liste de tous les médecins
            slots (list[Slot]): Liste des créneaux horaires
        """
        self.all_doctors = all_doctors
        self.slots = slots
    
    def signaler_user(self, slot: Slot):
        """
        Signale à l'utilisateur si pas de médecin disponible pour un créneau
        """
        print(f"Aucun médecin disponible pour le créneau {slot.date}")
    
    def attribute_slots(self):
        """
        Attribue les créneaux horaires aux médecins disponibles
        """
        for slot in self.slots:
            current_doctor = 0
            
            for doctor in self.all_doctors:
                result = slot.attribute_slot(doctor)
                if result == "Success":
                    current_doctor += 1
                    if slot.is_full():
                        continue
                
                elif result == "Full":
                    if current_doctor == len(self.all_doctors):
                        self.signaler_user(slot)
                    else:
                        continue
        print("Tous les créneaux ont été attribués avec succès")
        
        print("- " * 40)
        print(f"Liste des créneaux attribués: (nombre de slots: {len(self.slots)})")
        
        for slot in self.slots:
            print(slot)
            print("-" * 40)