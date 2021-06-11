from time import sleep


class TrafficLight:
    def __init__(self):
        self.__color: str = 'RED'
        self.__status: str = 'OFF'

    def running(self):
        self.__status = 'ON'
        self.__color = 'RED'
        print(self.__color)
        sleep(7)
        self.__color = 'YELLOW'
        print(self.__color)
        sleep(2)
        self.__color = 'GREEN'
        print(self.__color)
        sleep(7)
        self.__status = 'OFF'


if __name__ == '__main__':
    light = TrafficLight()
    light.running()
