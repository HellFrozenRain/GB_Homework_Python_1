class Cell:
    def __init__(self, number):
        self.number = number

    def __add__(self, other):
        return Cell(self.number + other.number)

    def __sub__(self, other):
        result = self.number - other.number
        if result > 0:
            return Cell(result)
        else:
            print('в первой клетке мало ячеек')
            return Cell(None)

    def __mul__(self, other):
        return Cell(self.number * other.number)

    def __floordiv__(self, other):
        return Cell(self.number // other.number)

    def make_order(self, rows):
        return '\\n'.join(['*' * rows for i in range(self.number // rows)]) + '\\n' + '*' * (self.number % rows)

cell_1 = Cell(17)
cell_2 = Cell(12)

print(f' Сумма: {(cell_1 + cell_2).number}')
print(f' Разность: {(cell_1 - cell_2).number}')
print(f' Разность: {(cell_2 - cell_1).number}')

print(f' Произведение: {(cell_1 * cell_2).number}')
print(f' Деление: {(cell_1 // cell_2).number}')
print(f' Деление: {(cell_2 // cell_1).number}')
print(cell_2.make_order(5))


