import datetime

def get_staff_on_duty():
    hour = datetime.datetime.now().hour
    # সিডিউল লজিক
    if 8 <= hour < 16:
        return {"Shift": "Morning", "Doctor": "Dr. Amin", "Nurse": "Nurse Sumi"}
    elif 16 <= hour < 24:
        return {"Shift": "Evening", "Doctor": "Dr. Karim", "Nurse": "Nurse Shila"}
    else:
        return {"Shift": "Night", "Doctor": "Dr. Rafiq", "Nurse": "Nurse Popy"}