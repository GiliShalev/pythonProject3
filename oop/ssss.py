from oop.travel_app import Passenger

gil = Passenger(1234, "Gil")
ron = Passenger(5678, "Ron")

d = {'a': gil, 'b': ron}
print(d['a'].name)
