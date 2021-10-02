my_list1 = []
for i in range(1000):
    if i % 2 != 0:
        my_list1.append(i**3) #создание списка кубов нечетных чисел
print(my_list1)
result = 0
for number in my_list1:
    summ = 0
    num = number
    while (num != 0):
        summ = summ + num % 10
        num = num // 10
    if summ % 7 == 0:
        result = result + number #cумма чисел с цифрами кратными 7
print(result)

resultb = 0
for el in range(len(my_list1)):
    my_list1[el] = my_list1[el] + 17
for number in my_list1:
    summ = 0
    num = number
    while (num != 0):
        summ = summ + num % 10
        num = num // 10
    if summ % 7 == 0:
        resultb = resultb + number #cумма чисел с цифрами кратными 7 с +17
print(resultb)