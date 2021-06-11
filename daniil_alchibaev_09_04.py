
class Car:
    def __init__(self, speed, color, name, is_police=False):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = is_police

    def go(self):
        print(f'{self.name} is moving')

    def stop(self):
        print(f'{self.name} has stopped')

    def turn(self, direction):
        print(f'{self.name} turned to {direction}')

    def show_speed(self):
        print(f"{self.name}'s speed is {self.speed}")


class TownCar(Car):
    def show_speed(self):
        super().show_speed()
        if 60 < self.speed:
            print("Slower!")


class WorkCar(Car):
    def show_speed(self):
        super().show_speed()
        if 40 < self.speed:
            print("Slower!")


class SportCar(Car):
    pass


class PoliceCar(Car):
    def __init__(self, speed, color, name, _=True):
        super().__init__(speed, color, name, True)


if __name__ == '__main__':
    town_car = TownCar(55, 'yellow', 'taxi')
    work_car = WorkCar(45, 'blue', 'bus')
    sport_car = SportCar(200, 'green', 'Lambo')
    police_car = PoliceCar(250, 'black', 'NFS')
    town_car.show_speed()
    work_car.show_speed()
    sport_car.show_speed()
    police_car.show_speed()
