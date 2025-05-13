class Passenger:
    def __init__(self, passport_num, first_name, last_name, meal, seat):
        self.meal = None
        self.passport_num = passport_num
        self.first_name = first_name
        self.last_name = last_name
        self.set_meal(meal)
        self.seat = seat

    def print_info(self):
        print("Passport Number: {}".format(self.passport_num))
        print("First Name: {}".format(self.first_name))
        print("Last Name: {}".format(self.last_name))
        print("Meal: {}".format(self.meal))
        print("Seat: {}".format(self.seat))

    def set_passport_num(self, passport_num):
        self.passport_num = passport_num

    def set_meal(self, meal):
        if meal in ["VEG", "MEAT", "FISH"]:
            self.meal = meal
        else:
            print("Invalid meal")
            self.meal = "OTHER"










