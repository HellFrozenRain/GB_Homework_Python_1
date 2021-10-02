variants = ['процент', 'процента', 'процентов']

for n in range(1, 101):
    if n % 10 == 1 and n % 100 and n != 11:
        print(n, variants[0])
    elif (n % 10 < 5 and n % 10 > 1) and (n % 100 < 10 or n % 100 >= 20):
        print(n, variants[1])
    else:
        print(n, variants[2])