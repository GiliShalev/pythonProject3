# 1
def rect_area(num1, num2):
    if num1 == num2:
        return square_area(num1)
    return num1 * num2

def square_area(num1):
    return num1 * num1

x = rect_area(10, 10)
print(x)

# 2
def calc_angle(hour1, hour2):
    angle_per_hour = 360 / 12
    diff = hour2 - hour1
    return diff * angle_per_hour

res = calc_angle(12, 24)
print(res)

# 3
cities = ["London", "paris", "Tel Aviv"]

def fix_cities_arr(cities_arr):
    valid_cities = []
    for city in cities_arr:
        if city[0].isupper() and ' ' in city:
            valid_cities.append(city)
    return valid_cities

res = fix_cities_arr(cities)
print(res)

def default_example(a=1, b=2, c=3, d=2, e=22, f=23):
    print(a, b, c, d, e, f)

default_example(a=22, e=5)

