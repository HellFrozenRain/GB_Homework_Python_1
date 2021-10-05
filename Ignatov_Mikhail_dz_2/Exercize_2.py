list_1 =['в', '5', 'часов', '17', 'минут', 'температура', 'воздуха', 'была', '+5', 'градусов']
list_2 = []
for el in list_1:
    if el[0] in ('+', '-'):
        el = f'"{el.zfill(3)}"'
    if el.isdigit():
        el = f'"{el.zfill(2)}"'
    list_2.append(el)
print(' '.join(list_2))
