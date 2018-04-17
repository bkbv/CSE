'''
# Defining a class
class Shoes(object):
    def __init__(self, lace_color, lighting, brand):  # TWO understand before and after
        # Things a shoe has
        self.lace_color = lace_color
        self.rgb_lighting = lighting
        self.used = False
        self.brand = brand
        self.clean = True

    def wear(self):
        self.used = True
        self.clean = False
        print("You wear the shoes")

    def wash(self):
        self.clean = True
        print("You clean the shoes")


first_pair = Shoes("Red", True, "Big Baller Brand")
second_pair = Shoes("yellow", False, "Nike")

print(first_pair.brand)
print(first_pair.lace_color)
print(first_pair.clean)

first_pair.wear()
print(first_pair.clean)
first_pair.wash()
print(first_pair.clean)
'''

class car(object):
    def __init__(self, tires, turbo, brand):
        # Things a car has
        self.tires = tires
        self.turbo = turbo
        self.brand = brand
        self.used = False
        self.passenagers = 0
        self.running = False

    def drive_forward(self):
        if self.running:
            print("You move forward")
        else:
            print("Nothing Happens")
    def turn_on(self):
        if self.running:
            print("Nothng Happens")
        else:
            self.running = True
            print("You start the car")
    def turn_off(self):
        if self.running:
            self.running = False
            print("you turn the car off")
        else:
            print("Nothing happens")

    def go_for_drive(self, passenagers):
        print("%d passenagers get in" % passenagers)
        self.passenagers = passenagers
        self.turn_on()
        self.drive_forward()
        self.drive_forward()
        self.drive_forward()
        self.turn_off()
        print("%d passenagers get out" % passenagers)
        self.passenagers = 0


my_car = car(4, True, "Tesla")
my_car.go_for_drive(4)