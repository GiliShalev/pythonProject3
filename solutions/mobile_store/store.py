from typing import override

class Mobile:
    def __init__(self, manufacturer, model, screen_size):
        self.screen_size = None
        self.manufacturer = manufacturer
        self.model = model
        self.set_screen_size(screen_size)

    def set_screen_size(self, screen_size):
        if 20 >= screen_size >= 5:
            self.screen_size = screen_size
        else:
            self.screen_size = 10

    def print_info(self):
        print("Manufacturer: " + self.manufacturer)
        print("Model: " + self.model)
        print("Screen Size: " + str(self.screen_size))

class Iphone(Mobile):
    def __init__(self, model, screen_size, num_of_apps):
        Mobile.__init__(self, "Iphone", model, screen_size)
        self.num_of_apps = num_of_apps

    def print_info(self):
        super().print_info()
        print("Number of apps: " + str(self.num_of_apps))

class Samsung(Mobile):
    def __init__(self, model, screen_size, jail_break):
        super().__init__("Samsung", model, screen_size)
        self.jail_break = jail_break

    @override
    def print_info(self):
        super().print_info()
        print("Is jail broken: " + str(self.jail_break))

s1 = Samsung("S25", 20, True)
s2 = Samsung("S25", 40, False)
I1 = Iphone("16", 20, 5)
I2 = Iphone("16", 40, 7)
s1.print_info()
I1.print_info()