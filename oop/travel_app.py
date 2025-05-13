class Flight:
    passengers = {}
    num_of_total_pass = 0
    def __init__(self, departure_date, arrival_date):
        self.departure_date = departure_date
        self.arrival_date = arrival_date

    def add_passenger(self, passenger):
        self.passengers[passenger.pass_num] = passenger
        Flight.num_of_total_pass += 1

    def get_total_passengers(self):
        return Flight.num_of_total_pass

    def get_passengers(self):
        return self.passengers

class Passenger:
    def __init__(self, pass_num, name):
        self.name = name
        self.pass_num = pass_num

flight = Flight("11/11/2025", "13/11/2025")
flight_return = Flight("13/11/2025", "15/11/2025")

gil = Passenger(1234, "Gil")
ron = Passenger(5678, "Ron")
flight.add_passenger(gil)
flight.add_passenger(ron)
flight_return.add_passenger(gil)
flight_return.add_passenger(ron)

passengers_in_flight = flight.get_passengers()
for pass_num, passenger in passengers_in_flight.items():
    print(pass_num, passenger.name)

num_of_total_pass = flight.get_total_passengers()
print(num_of_total_pass)