class Car:
    def __init__(self):
        self.__speed = 0

    def set_speed(self, speed):
        if speed < 0:
            print("Speed cannot be negative.")
        else:
            self.__speed = speed

    def get_speed(self):
        return self.__speed

my_car = Car()
my_car.set_speed(80)
print("Current speed:", my_car.get_speed())
