def thesaurus(*names):
    dict_1 = {}
    for name in names:
        dict_1.setdefault(name[0], [])
        dict_1[name[0]].append(name)
    return sorted(dict_1.items(), key=lambda t: t[0])
# посмотрел в документации сортировку по ключам, но вообще не понимаю механизм.
# без лямбды делал бы через пустой словарь
#     sorted_dict = {}
#     for el in sorted(dict_1):
#         sorted_dict[el] = dict_1[el]
#     return sorted_dict



print(thesaurus('Мария', 'Иван', 'Петр', 'Илья', 'Рита', 'Павел'))


