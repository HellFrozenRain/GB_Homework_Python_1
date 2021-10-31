import time

class TrafficLight:
    # class attributes
    __colors = {'red': 7, 'yellow': 2, 'green': 10}

    # class methods

    def running(self, n: int):
        """n: number of cycles"""
        for el in range(n):
             for color, sec in self.__colors.items():
                print(color)
                time.sleep(sec)

example = TrafficLight()
example.running(2)


