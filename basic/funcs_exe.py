import math

a = 9
b = 1
dif = a - b
if dif < 0:
    print(math.fabs(dif))
elif dif > 0:
    print(dif * 2)

s = "the price of the shirt is 25$"
s = s.replace("shirt", "product")
print(s)

first_letter = s[0]
if first_letter.islower():
    s = s.replace(first_letter, first_letter.upper(), 1)
print(s)

def calcSquare(length, width):
    if length == width:
        return calcSquareEqual(length)
    return length * width

def calcSquareEqual(x):
    return math.pow(x, 2)
    # return x ** 2

res = calcSquare(10, 20)
print(res)
res = calcSquare(10, 10)
print(res)

def calc_angle(from_hour, to_hour):
    one_hour = 360 / 12
    return (to_hour - from_hour) * one_hour

res = calc_angle(3, 4)
print(res)

cities = ["London", "Paris", "Tel Aviv", "Tokyo"]
for city in cities:
    if city[0].islower() or not ' ' in city:
        cities.remove(city)

print(cities)