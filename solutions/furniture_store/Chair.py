class Chair:
    def __init__(self, material, color , length, width, height):
        self.color = None
        self.material = material
        self.set_color(color)
        self.set_length(length)
        self.set_width(width)
        self.set_height(height)

    def set_color(self, color):
        self.color = 'White'
        if color in ['Black', 'White', 'Blue', 'Red', 'Green']:
            self.color = color

    def set_length(self, length):
        self.length = self.set_size(length, 10, 150)

    def set_height(self, height):
        self.height = self.set_size(height, 10, 150)

    def set_width(self, width):
        self.width = self.set_size(width, 10, 150)

    def set_size(self, size, mini, maxi):
        if maxi >= size >= mini:
            return size
        else:
            print("Size is out of range")
            return 0

    def get_volume(self):
        return self.length * self.width * self.height

    def print_info(self):
        print(self.material, self.color, self.length, self.width, self.height, self.get_volume())

class RockingChair(Chair):
    def __init__(self, material, color , length, width, height, max_rocking_angle):
        super().__init__(material, color, length, width, height)
        self.max_rocking_angle = max_rocking_angle

    def set_rocking_angle(self, angle):
        self.max_rocking_angle = self.set_size(angle, 10, 180)

    def print_info(self):
        super().print_info()
        print(self.max_rocking_angle)

chair1 = Chair("Wood", "Red", 100, 100, 100)
print(chair1.color)
chair1.print_info()
print(chair1.color)

rc1 = RockingChair("Wood", "Red", 100, 100, 100, 60)
rc1.print_info()