from abc import ABC, abstractmethod

class Clothes(ABC):
    def __init__(self, param):
        self.param = param

        @abstractmethod
        def calculation(self):
            pass

class Coat(Clothes):
    @property
    def calculation(self):
        return round(self.param / 6.5 + 0.5)

class Suit(Clothes):
    @property
    def calculation(self):
        return round(self.param * 2 + 0.3)

coat = Coat(100)
suit = Suit(180)
print(coat.calculation)
print(suit.calculation)
