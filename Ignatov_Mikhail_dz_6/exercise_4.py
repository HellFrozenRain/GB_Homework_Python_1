from itertools import zip_longest

with open('users.csv', 'r', encoding='utf-8') as file_1:
    list_1 = [string.strip() for string in file_1.readlines()]
with open('hobby.csv', 'r', encoding='utf-8') as file_2:
    list_2 = [string.strip() for string in file_2.readlines()]
with open('users_hobby.txt', 'w', encoding='utf-8') as file_3:
    for (name, hobby) in zip_longest(list_1, list_2[:len(list_1)]):
        data = f'{name}: {hobby}' + '\n'
        file_3.write(data)