class Patients:
    def __init__(self, id , first_name, last_name, age, gender, birthday, phone):
        self.id= id 
        self.first_name= first_name
        self.last_name= last_name
        self.age= age
        self.gender= gender
        self.birthday= birthday
        self.phone= phone 

    def to_dict(self):
        return self.__dict__