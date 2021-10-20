import sys
from itertools import zip_longest

def my_func(file_1, file_2, file_3):
    with open(file_1, 'r', encoding='utf-8') as file_1:
        list_1 = [string.strip() for string in file_1.readlines()]
    with open(file_2, 'r', encoding='utf-8') as file_2:
        list_2 = [string.strip() for string in file_2.readlines()]
    with open(file_3, 'w', encoding='utf-8') as file_3:
        for (name, hobby) in zip_longest(list_1, list_2[:len(list_1)]):
            data = f'{name}: {hobby}' + '\n'
            file_3.write(data)

if len(sys.argv) == 1:
    file_1_name = input('enter file 1 name')
    file_2_name = input('enter file 2 name')
    file_3_name = input('enter file 3 name')
    my_func(file_1_name, file_2_name, file_3_name)
elif len(sys.argv) == 4:
    file_1_name = sys.argv[1]
    file_2_name = sys.argv[2]
    file_3_name = sys.argv[3]
    my_func(file_1_name, file_2_name, file_3_name)

