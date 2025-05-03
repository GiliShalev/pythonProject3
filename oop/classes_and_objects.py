class Vehicle:
    vat = 1.18
    def __init__(self, model, wheels=4, color='white'):
        self.model = model
        self.wheels = wheels
        self.color = color

    def drive(self):
        print("Drive on all wheels", self.wheels)

class Vehicle1:
    def __init__(self, model, wheels, color='white'):
        self.model = model
        self.wheels = wheels
        self.color = color

    def drive(self):
        print("Drive on all wheels 1", self.wheels)

class MotorBike(Vehicle1, Vehicle):
    def __init__(self, model, wheels, color='white'):
        super().__init__(model, wheels, color)

    def drive(self):
        super().drive()
        Vehicle.drive(self)
        print("More in drive")

car = Vehicle("Ford", 4, "Red")
car1 = Vehicle("Mazda", 4)
motor_bike = Vehicle("Honda", 2, "Red")
motor_bike1 = MotorBike("Honda", 2, "Red")

print(car.color)
print(car1.model)
print(car1.color)
motor_bike1.drive()