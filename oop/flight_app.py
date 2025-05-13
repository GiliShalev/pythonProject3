class Car:
    vat = 1.18
    speed = 0
    def __init__(self, vendor, model, price, wheels=4):
        self.vendor = vendor
        self.model = model
        self.wheels = wheels
        self.price = price

    def set_speed(self, speed):
        if speed > self.speed:
            action = "Speeding to"
        elif speed < self.speed:
            action = "Slowing to"
        else:
            action = "Keeping"

        print(action, speed)

    def go(self, speed):
        self.set_speed(speed)

    def stop(self):
        self.set_speed(0)

    def get_vendor_and_model(self):
        return self.vendor + ' ' + self.model

    def get_price(self):
        return self.price * self.vat
class Flight:
    total_pass_in_all_flights = 0
    def __init__(self, from1, to, date, time, seats):
        self.passengers = {}
        self.from1 = from1
        self.to = to
        self.date = date
        self.time = time
        self.seats = seats

    def add_passenger(self, passenger):
        if self.seats == len(self.passengers):
            print("Too many passengers")
            return
        if passenger in self.passengers.keys():
            print("Passenger already exist in flight")
            return
        self.passengers[passenger.passport_num] = passenger
        Flight.total_pass_in_all_flights += 1

    def get_passenger(self, passport_num):
        return self.passengers[passport_num]

    def get_total_passengers(self):
        return self.total_pass_in_all_flights

    def get_total_passengers_in_flight(self):
        return len(self.passengers)

class Passenger:
    def __init__(self, passport_num, first_name, last_name, meal, seat):
        self.passport_num = passport_num
        self.first_name = first_name
        self.last_name = last_name
        self.meal = meal
        self.seat = seat

    def print_info(self):
        print("passport_num is:", self.passport_num)
        print("first_name is:", self.first_name)
        print("last_name is:", self.last_name)
        print("meal is:", self.meal)
        print("seat is:", self.seat)

    def set_meal(self, meal):
        meals = ['VEG', 'MEAT', 'FISH']
        if not meal in meals:
            print("Meal not valid")
        else:
            self.meal = meal

gil = Passenger(1234, "Gil", "Shalev", "Regular", "22A")
tal = Passenger(5678, "Tali", "Shalev", "Regular", "22B")

f1 = Flight("London", "Paris", "12/12/2025", "12:30", 120)
f2 = Flight("Paris", "London", "18/12/2025", "12:30", 120)

f1.add_passenger(gil)
f1.add_passenger(tal)

f2.add_passenger(gil)

print("Total", Flight.total_pass_in_all_flights)

print(f2.total_pass_in_all_flights)
p1 = f1.get_passenger(1234)
print(p1.first_name)

p1.set_meal("VEG")
print(f1.get_total_passengers())
print(f1.get_total_passengers_in_flight())

passengers1 = f1.passengers
for key, value in passengers1.items():
    print(key, value.first_name + ' ' + value.last_name)

