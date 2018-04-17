class Vehicle(object):
     def __init__(self, seats, engine_type, turning_mechanism):
        self.seats = seats
        self.engine_type = engine_type
        self.turning_mechanism = turning_mechanism

     def move(self):
         print("you move forward")

     def change_direction(self):
        print("you change direction")


class Car(Vehicle):
     def __init__(self, seats, horsepower):
         super(Car, self).__init__(seats, 'engine', 'steering wheel')
         self.hp = horsepower

     def turn_on(self):
         print("you turn the key and the engine starts")


test_car = Car(4, 9001)
test_car.turn_on()
test_car.change_direction()
print(test_car.turning_mechanism)


class KeyLessCar(Car):
    def __init__(self, seats, hp):
        super(KeyLessCar, self).__init__(seats, hp)

    def turn_on(self):
        print("You push the button and the car turns on")


test_car.turn_on()
cool_car = KeyLessCar(4, 9002)
cool_car.turn_on()


class tesla(Car):
    def __init__(self, seats):
        super(tesla, self).__init__(seats, 500)

    def fly(self):
        print("You launch the car into low earth orbit")

