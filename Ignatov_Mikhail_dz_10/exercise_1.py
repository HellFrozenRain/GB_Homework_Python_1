class Matrix:
    def __init__(self, matrix):
        self.matrix = matrix

    def __str__(self):
        return '\n'.join([' '.join(map(str, row)) for row in self.matrix])


    def __add__(self, other):
        result = [[self.matrix[i][j] + other.matrix[i][j] for j in range(len(self.matrix[0]))]
        for i in range(len(self.matrix))]
        return '\n'.join([' '.join(map(str, row)) for row in result])


a = [[1, 2, 3],
     [4, 5, 6],
     [7, 8, 9]]

b = [[10, 9, 8],
     [7, 6, 5],
     [4, 3, 2]]


Matrix(a)
print(Matrix(a))
Matrix(b)
print(Matrix(b))
c = Matrix(a) + Matrix(b)
print(c)