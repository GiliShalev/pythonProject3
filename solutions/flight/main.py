from solutions.flight.flight import Flight
from solutions.flight.passenger import Passenger

gil = Passenger(1234, "Gil", "Shalev", "VEG", "31A")
ron = Passenger(5678, "Ron", "Shalev", "VEG", "31A")
paris_to_london = Flight(200, "Paris", "London", "12/11/2025", "12:23")
london_to_paris = Flight(200, "London", "Paris", "19/11/2025", "12:23")

paris_to_london.add_passenger(ron)
paris_to_london.add_passenger(gil)

london_to_paris.add_passenger(ron)
london_to_paris.add_passenger(gil)

print(london_to_paris.get_total_passengers_in_all_flights())
print(london_to_paris.get_num_passengers())
g = london_to_paris.get_passenger(1234)
print(g.first_name)
print(g.last_name)

pass_list = london_to_paris.get_pass_list()
for passenger in pass_list.values():
    print(passenger.first_name)
    print(passenger.last_name)


