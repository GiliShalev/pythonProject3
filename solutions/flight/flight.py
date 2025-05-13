class Flight:
    total_passengers_in_all_flights = 0
    def __init__(self, seats, depart_from, to, date, time):
        self.passengers = {}
        self.num_of_pass = 0
        self.seats = seats
        self.depart_from = depart_from
        self.to = to
        self.date = date
        self.time = time

    def add_passenger(self, passenger):
        self.passengers[passenger.passport_num] = passenger
        Flight.total_passengers_in_all_flights += 1

    def get_total_passengers_in_all_flights(self):
        return Flight.total_passengers_in_all_flights

    def get_num_passengers(self):
        return len(self.passengers)

    def get_passenger(self, passport_num):
        return self.passengers[passport_num]

    def get_pass_list(self):
        return self.passengers

