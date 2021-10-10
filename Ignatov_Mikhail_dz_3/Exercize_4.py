def dict_sort(dict):
    sorted_dict = {}
    for el in sorted(dict):
        sorted_dict[el] = dict[el]
    return sorted_dict


def thesaurus_adv(*full_names):
    dict_1 = {}
    for full_name in full_names:
        name, last_name = full_name.split()
        dict_1.setdefault(last_name[0], {})
        dict_1[last_name[0]].setdefault(name[0], [])
        dict_1[last_name[0]][name[0]].append(full_name)


    return dict_sort(dict_1)


print(thesaurus_adv("Иван Сергеев", "Инна Серова", "Петр Алексеев", "Илья Иванов", "Анна Савельева"))