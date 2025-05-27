class Appointment:
    def __init__(self, id, patient_id, date, time, status="booked"):
        self.id= id 
        self.patient_id= patient_id
        self.date= date
        self.time= time
        self.status= status 

    def to_dict(self):
        return self.__dict__