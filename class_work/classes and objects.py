class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def print_name(self):
        print(self.name)

gil = Person('Gil', 18)
chen = Person('Chen', 12)
gil.print_name()
chen.print_name()