import sys
if len(sys.argv) > 1:
    data = sys.argv[1]
    with open('bakery.csv', 'a', encoding='utf-8') as f:
        f.writelines(data + '\n')

elif len(sys.argv) == 1:
    data = input('enter data')
    print(data)
    with open('bakery.csv', 'a', encoding='utf-8') as f:
        f.writelines(data + '\n')

