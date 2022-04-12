class Car:

    def __init__(self, speed, color, name, is_police=False):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = is_police

    def go(self):
        print(f'the car {self.name} is moving')

    def stop(self):
        print(f'the car {self.name} has stopped')

    def turn(self, direction):
        print(f'the car {self.name}  turned {direction}')

    def show_speed(self, speed=60):
        print(f'current speed of {self.name} is {speed}')


class TownCar(Car):

    def show_speed(self):
        if self.speed > 60:
            print(f'the speed of {self.name} is too high')
        else:
            print(f'current of speed of {self.name} is {self.speed}')


class SportCar(Car):
    """sport car is here"""


class WorkCar(Car):
    def __init__(self, speed, color, name):
        super().__init__(speed, color, name)

    def show_speed(self):
        if self.speed > 40:
            print(f'the speed of {self.name} {self.speed} km/h is too high')
        else:
            print(f'current of speed of {self.name} is {self.speed}')


class PoliceCar(Car):
    def __init__(self, speed, color, name, is_police=True):
        super().__init__(speed, color, name, is_police)


a = WorkCar(70, 'black', 'Lexus')
a.show_speed()
