import math


number = int(input('enter number: '))
generator = (num for num in range(1, number + 1, 2))

for i in range(1, math.ceil(number / 2) + 1):
    print(next(generator))