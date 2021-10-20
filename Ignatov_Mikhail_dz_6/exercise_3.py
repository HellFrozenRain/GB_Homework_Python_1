import json
def my_func(file_a, file_b):
    my_dict = {}
    file_1 = open(file_a, encoding='utf-8')
    list_1 = [string.strip() for string in file_1.readlines()]
    file_2 = open(file_b, encoding='utf-8')
    list_2 = [string.strip() for string in file_2.readlines()]

    if len(list_1) <= len(list_2):
        for el in range(len(list_1)):
            my_dict[list_1[el].strip()] = list_2[el].strip()
        with open('dictionary.json', 'w+', encoding='utf-8') as fw:
            json.dump(my_dict, fw, ensure_ascii=False)

        with open('dictionary.json', 'r', encoding='utf-8') as fr:
            result = json.load(fr)

        print(result)
        exit(1)

    else:
        for el in range(len(list_1) - len(list_2)):
            list_2.append(None)
        for el in range(len(list_1)):
            my_dict[list_1[el]] = list_2[el]


        with open('dictionary.json', 'w+', encoding='utf-8') as fw:
            json.dump(my_dict, fw, ensure_ascii=False)

        with open('dictionary.json', 'r', encoding='utf-8') as fr:
            result = json.load(fr)

        print(result)

my_func('users.csv', 'hobby.csv')