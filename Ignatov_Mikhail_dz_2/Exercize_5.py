"""5. Создать вручную список, содержащий цены на товары (10–20 товаров), например:
© geekbrains.ru 19
[57.8, 46.51, 97, ...]
A. Вывести на экран эти цены через запятую в одну строку, цена должна отображаться в виде
<r> руб <kk> коп (например «5 руб 04 коп»). Подумать, как из цены получить рубли и копейки,
как добавить нули, если, например, получилось 7 копеек или 0 копеек (должно быть 07 коп
или 00 коп).
B. Вывести цены, отсортированные по возрастанию, новый список не создавать (доказать, что
объект списка после сортировки остался тот же).
C. Создать новый список, содержащий те же цены, но отсортированные по убыванию.
D. Вывести цены пяти самых дорогих товаров. Сможете ли вывести цены этих товаров по
возрастанию, написав минимум кода?"""
list_1 = [0.7, 44.5, 96, 60, 31.73, 67.2, 48.2, 3.17, 26, 56.54, 24.72, 77, 82.2, 5.1]
print('задание A', '\n')

list_2 = []
for i in range(len(list_1)):
    r = int(list_1[i])
    k = int((list_1[i]*100) % 100)
    result = (f'{r:02} руб {k:02} коп')
    list_2.append(result)
print(list_2)

print('задание B', '\n')

print(id(list_1))
list_1.sort()
print(list_1)
print(id(list_1))

print('задание C', '\n')

list_2 = list_1.copy()
list_2.reverse()
print(list_2)

print('задание D', '\n')

list_3 = []
for i in range(len(list_1)):
    r = int(list_1[i])
    k = int((list_1[i]*100) % 100)
    result = (f'{r:02} руб {k:02} коп')
    list_3.append(result)
print(list_3[-5:])