class Doctor:
    def __init__(self, name, schedule):
        self.name = name
        self.schedule = schedule

    def book_time(self, time):
        if time in self.schedule:
            self.schedule.remove(time)
            return True
        return False

class Dentist(Doctor):
    def __init__(self):
        super().__init__("Dentist", ["10:00", "11:00", "12:00"])

class Therapist(Doctor):
    def __init__(self):
        super().__init__("Therapist", ["13:00", "14:00", "15:00"])

class Cardiologist(Doctor):
    def __init__(self):
        super().__init__("Cardiologist", ["16:00", "17:00", "18:00"])

dentist = Dentist()
therapist = Therapist()
cardiologist = Cardiologist()