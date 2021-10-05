list_1 =['в', '5', 'часов', '17', 'минут', 'температура', 'воздуха', 'была', '+5', 'градусов']
for el in list_1:
    el_index = list_1.index(el)
    list_1.remove(el)
    if el[0] in ('+', '-'):
        el = f'"{el.zfill(3)}"'
    if el.isdigit():
        el = f'"{el.zfill(2)}"'
    list_1.insert(el_index, el)
print(' '.join(list_1))
