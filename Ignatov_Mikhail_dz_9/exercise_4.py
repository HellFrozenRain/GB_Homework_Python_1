class Car:
    def __init__(self, speed, color, name, is_police):
        """:param speed, color, name, is_police"""
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = is_police

    def go(self, current_speed):
        self.speed = current_speed
        print(f'{self.name} {self.color} поехала')

    def stop(self):
        self.speed = 0
        print(f'{self.name} приехала')

    def turn(self, direction: str):
        print(f'{self.name} повернула {direction}')

    def show_speed(self):
        print(f'speed: {self.speed}')

class TownCar(Car):

    def __init__(self, speed, color, name, is_police):
        super(TownCar, self).__init__(speed, color, name, is_police)

    def show_speed(self):
        if self.speed > 60:
            print('over speeding')
        else:
            print(f'speed: {self.speed}')

class SportCar(Car):

    def __init__(self, speed, color, name, is_police):
        super(SportCar, self).__init__(speed, color, name, is_police)

class WorkCar(Car):

    def __init__(self, speed, color, name, is_police):
        super(WorkCar, self).__init__(speed, color, name, is_police)

    def show_speed(self):
        if self.speed > 60:
            print('over speeding')
        else:
            print(f'speed: {self.speed}')

class PoliceCar(Car):

    def __init__(self, speed, color, name, is_police):
        super(PoliceCar, self).__init__(speed, color, name, is_police)



sedan = TownCar(0, 'баклажан', 'LADA', False)
sedan.go(61)
sedan.show_speed()
sedan.turn('left')
sedan.stop()
sedan.show_speed()
print('\n')
race = SportCar(0, 'красный', 'McLarenF1', False)
race.go(320)
race.show_speed()
race.turn('right')
race.stop()
race.show_speed()
print('\n')
truck = WorkCar(0, 'желтый', 'Белаз', False)
truck.go(30)
truck.show_speed()
truck.turn('back')
truck.stop()
truck.show_speed()
print('\n')
service = PoliceCar(0, 'белый', 'Ford', True)
service.go(120)
service.show_speed()
service.turn('right')
service.stop()
service.show_speed()
