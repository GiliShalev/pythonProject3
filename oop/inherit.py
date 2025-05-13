from typing import override


class Vehicle:
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year

    def drive(self):
        print("V Driving")

class Car(Vehicle):
    def __init__(self, make, model, year):
        super().__init__(make, model, year)

class MotorBike(Vehicle):
    def __init__(self, make, model, year, seats):
        super().__init__(make, model, year)
        self.seats = seats

    def dummy_func(self):
        print("Dummy func")

    def drive(self):
        super().drive()
        print("Driving Motorbike")

ford = Car("Ford", "Mustang", 2024)
ford.drive()

print(ford.make)
honda = MotorBike("Honda", "X500", 2024, 2)
honda.dummy_func()
honda.drive()
