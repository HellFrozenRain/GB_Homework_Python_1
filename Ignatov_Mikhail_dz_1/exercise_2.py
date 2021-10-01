my_list1 = []
my_list2 = []
my_list3 = []
my_list4 = []
for i in range(1000):
    if i % 2 != 0:
        my_list1.append(i**3) #создание списка кубов нечетных чисел
print(my_list1)
for number in my_list1:
    x = 0
    num = number
    while (num != 0):
        x = x + num % 10
        num = num // 10
    if x % 7 == 0:
        my_list2.append(number)
    result = sum(my_list2) #cумма чисел кратных 7
print(result)

for el in my_list1:
    my_list3.append(el+17)
print(my_list3)
for number in my_list3:
    y = 0
    num = number
    while (num != 0):
        y = y + num % 10
        num = num // 10
    if y % 7 == 0:
        my_list4.append(number)
    result = sum(my_list4) #cумма чисел кратных 7
print(result)