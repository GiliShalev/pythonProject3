class Car:
    vat = 1.18
    def __init__(self, make, model, year, color, price=100000):
        self.color = None
        self.model = model
        self.make = make
        self.year = year
        self.price = price
        self.set_color(color)

    def print_info(self):
        print("Model:", self.model)
        print("Make:", self.make)
        print("Year:", self.year)

    def set_color(self, color):
        if color != 'Green' and color != 'Red' and color != 'White':
            self.color = 'White'
        else:
            self.color = color

volvo = Car('Volvo', 22, 2020, 'Red')
ford = Car('Ford', 'Escort', 2021, 'White')
print(ford.color)
ford.set_color('Grey')
print(ford.color)
volvo.print_info()
print(volvo.year)
print(volvo.color)
volvo.color = 'Black'
volvo.set_color('Green')
print(volvo.color)