class Slot:
    def __init__(self, begin_hour, end_hour, nb_doctors_needed, list_of_doctors, date):
        """
        Initialise un créneau horaire
        
        Args:
            begin_hour (str): Heure de début du créneau
            end_hour (str): Heure de fin du créneau
            nb_doctors_needed (int): Nombre de médecins nécessaires
            list_of_doctors (list): Liste des médecins assignés
            date (str): Date du créneau (time format "DD-MM-YYYY")
        """
        self.begin_hour = begin_hour
        self.end_hour = end_hour
        self.nb_doctors_needed = nb_doctors_needed
        self.list_of_doctors = list_of_doctors
        # date should be a string in the format "DD-MM-YYYY"
        if not self.is_valid_date_format(date):
            raise ValueError("Date must be in the format 'DD-MM-YYYY'")
        self.date = date
        
    def is_valid_date_format(self, date):
        """
        Vérifie si la date est au format "DD-MM-YYYY"
        
        Args:
            date (str): Date à vérifier
            
        Returns:
            bool: True si la date est valide, False sinon
        """
        try:
            day, month, year = map(int, date.split('-'))
            return 1 <= day <= 31 and 1 <= month <= 12 and year > 0
        except ValueError:
            return False
        
    def attribute_slot(self, doctor):
        """
        Attribue un créneau à un médecin
        
        Args:
            doctor (Doctor): Médecin à attribuer au créneau
        """
        if not self.is_full() and doctor.can_work():
            self.list_of_doctors.append(doctor)
            return "Success"
        else:
            return "Full"
        
    def is_full(self):
        """
        Vérifie si le créneau est complet
        
        Returns:
            bool: True si le créneau est complet, False sinon
        """
        return len(self.list_of_doctors) >= self.nb_doctors_needed
    
    def __str__(self):
        info = f"Slot({self.date}, {self.begin_hour}-{self.end_hour}\nDoctors needed: {self.nb_doctors_needed},\nAssigned: {len(self.list_of_doctors)})"
        for doctor in self.list_of_doctors:
            info += f"\n - {doctor.name} ({doctor.diploma})"
        return info
    
    def __repr__(self):
        return self.__str__()