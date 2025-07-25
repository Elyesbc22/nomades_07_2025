class Doctor:

    def __init__(self, name: str, diploma: str, activity_percent: float, days_off: int, last_shift: str, number_of_holidays: int, weekend_days: int):
        """
        Initialise un docteur avec ses attributs
        
        Args:
            name (str): Nom du docteur
            activity_percent (float): Pourcentage d'activité du docteur
            days_off (int): Nombre de jours de repos
            last_shift (str): Date du dernier service
            number_of_holidays (int): Nombre de jours de congé
            weekend_days (int): Nombre de jours de week-end
        """
        self.name = name
        self.diploma = diploma
        if not (0 <= activity_percent <= 1):
            raise ValueError("Activity percentage must be between 0 and 1")
        self.activity_percent = activity_percent
        self.days_off = days_off
        self.last_shift = last_shift
        self.number_of_holidays = number_of_holidays
        self.weekend_days = weekend_days
        
    def can_work(self):
        """
        Vérifie si le docteur peut travailler
        
        Returns:
            bool: True si le docteur peut travailler, False sinon
        """
        return self.last_shift == "night"

    def __str__(self):
        """
        Représentation en chaîne de caractères du docteur
        
        Returns:
            str: Informations sur le docteur
        """
        return f"Doctor {self.name} ({self.diploma}) -\nActivity: {self.activity_percent},\nDays off: {self.days_off},\nLast shift: {self.last_shift},\nHolidays: {self.number_of_holidays},\nWeekend days: {self.weekend_days}"
    
    def __repr__(self):
        """
        Représentation en chaîne de caractères pour le docteur
        
        Returns:
            str: Informations sur le docteur
        """
        return self.__str__()