import pandas as pd
from doctor import Doctor 
from slot import Slot
import random
from planning import Planning
import datetime

# Function to generate a list of sample Slot objects
def generate_sample_slots(num_slots=10):
    slots = []
    for i in range(num_slots):
        begin_hour = f"{8 + i % 3 * 4}:00"  # e.g., 8:00, 12:00, 16:00
        end_hour = f"{8 + (i % 3 + 1) * 4}:00"  # e.g., 12:00, 16:00, 20:00
        nb_doctors_needed = random.randint(1, 20)
        date = (datetime.datetime.now() + datetime.timedelta(days=i)).strftime("%d-%m-%Y")
        new_slot = Slot(begin_hour=begin_hour, end_hour=end_hour, nb_doctors_needed=nb_doctors_needed, list_of_doctors=[], date=date)
        slots.append(new_slot)
    return slots

def doctors_from_df(df_doctors):
    all_doctors = []
    for _, row in df_doctors.iterrows():
        doctor_tmp = Doctor(row["name"],
                            row["diploma"],
                            row["activity_percent"], 
                            row["days_off"],
                            row["last_shift"],
                            row["number_of_holidays"],
                            row["weekend_days"])
        
        all_doctors.append(doctor_tmp)
    return all_doctors

# convert all doctors in csv to list of Doctor objects
# columns available: name,activity_percent,diploma,position,days_off,last_shift,number_of_holidays,weekend_days
df_doctors = pd.read_csv("../res/doctors.csv")
all_slots = generate_sample_slots(num_slots=10)
all_doctors = doctors_from_df(df_doctors)

planning = Planning(all_doctors, all_slots)
planning.attribute_slots()