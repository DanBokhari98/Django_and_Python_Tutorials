class Dog():

    species = "mammal"

    def __init__(self, breed, name):
        self.breed = breed
        self.name = name

type = 'Labador'
mydog = Dog(type, "yer")
print(mydog.breed, mydog.name)
print(mydog.species)
#How to force types
def ape(param1: int, param2: int) -> int:
    return param1 + param2

class Circle():
    pi = 3.14
    def __init__(self, radius=1):
        self.radius = radius

    def area(self):
        return Circle.pi * self.radius * self.radius

    def set_radius(self, new_r):
        self.radius = new_r


myc = Circle(3)
myc.set_radius(2)
print(myc.area())
