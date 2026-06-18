from datetime import date 

class Person:
    def __init__(self, name, country, dob):
        self.name = name
        self.country = country
        self.dob = dob

    def calculate_age(self):
        today = date.today()
        age = today.year - self.dob.year
        if today < date(today.year, self.dob.month, self.dob.day):
            age-=1
        return age

birthday = date(2006,12,1)
name = "Pearl"
country = "Chile"

person1 = Person(name,country, birthday)

print("Pearl is " + str(person1.calculate_age()) + " years old")

