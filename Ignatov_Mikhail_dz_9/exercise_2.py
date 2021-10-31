class Road:
    m = 25
    def __init__(self, length: int, width:int):
        self._length = length
        self._width = width
    def calculatiion(self, s: int):
        print(f' road length: {self._length} m')
        print(f' road width: {self._width} m')
        print(f' road thikness: {s} cm')

        result = self._length * self._width * self.m * s
        return f'The mass of asphalt required to cover the entire road: {result / 1000} t.'

example = Road(5000, 20)
print(example.calculatiion(5))