@dataclass
class Doctor:
    def __init__(self, name:str, diploma: str, activity_percentage: float, max_day_streak: int = 6, current_day_streak: int = 0):
        """initialise un medecin

        Args:
            name (str): _description_
            diploma (str): _description_
            activity_percentage (float): entre 0 et 1
            max_day_streak (int): _description_
            current_day_streak (int): _description_
        """
        
        self.name = name
        self.diploma = diploma
        self.activity_percentage = activity_percentage
        self.max_day_streak = max_day_streak
        self.current_day_streak = current_day_streak
    
    def max_streak_reached(self):
        return self.current_day_streak == self.max_day_streak
    
    @classmethod
    def smth(cls, a):
        return cls(name, str, ...)
        
    
    
janine = Doctor("Janine", "UNIGE Psychiatrie", 1)

janine.max_streak_reached()

doctors = []

for _, row in df.iterrows():
    doctor_tmp = Doctor(row["name"], row["diploma"], row["activi-..."])
    doctors.append(doctor_tmp)

print(janine.max_streak_reached())