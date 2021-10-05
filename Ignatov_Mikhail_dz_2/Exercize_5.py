list_1 = [0.7, 44.5, 96, 60, 31.73, 67.2, 48.2, 3.17, 26, 56.54, 24.72, 77, 82.2, 5.1]
# задание A

list_2 = []
for i in range(len(list_1)):
    r = int(list_1[i])
    k = int((list_1[i]*100) % 100)
    result = (f'{r:02} руб {k:02} коп')
    list_2.append(result)
print(list_2)

#задание B

print(id(list_1))
list_1.sort()
print(list_1)
print(id(list_1))

#задание C

list_2 = list_1.copy()
list_2.reverse()
print(list_2)

#задание D

list_3 = []
for i in range(len(list_1)):
    r = int(list_1[i])
    k = int((list_1[i]*100) % 100)
    result = (f'{r:02} руб {k:02} коп')
    list_3.append(result)
print(list_3[-5:])