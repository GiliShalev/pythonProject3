class Car:
    speed = 0
    vat = 1.18
    def __init__(self, make, model, price, wheels=4):
        self.price = 100000
        self.make = make
        self.model = model
        self.set_price(price)
        self.wheels = wheels

    def set_price(self, price):
        if price <= 100000:
            self.price = price

    def get_wheels(self):
        return self.wheels

    def get_price(self):
        return self.price * self.vat

    def print_info(self):
        print(self.make, self.model, self.price, self.wheels)

    def set_speed(self, speed):
        if speed == 0:
            word = "Stoping to"
        elif speed > self.speed:
            word = "Speeding to"
        elif speed < self.speed:
            word = "Slowing to"
        else:
            word = "Keeping"
        self.speed = speed
        print(word, speed)

    def go(self, speed):
        if speed > self.speed:
            self.set_speed(speed)

    def stop(self):
        self.set_speed(0)

    def get_make_and_model(self):
        return f"Make and model are: {self.make} {self.model}"

ford = Car("Ford", "Mustang", 30000)
ford.set_price(200000)
ford.print_info()
ford.set_speed(100)
ford.set_speed(80)
ford.set_speed(80)
ford.stop()
make_and_model = ford.get_make_and_model()
print(make_and_model)
print(ford.get_price())




# g = 33
# print("My name is: " + str(g))
# print("My...", g)
# print(f"My...{g}")



