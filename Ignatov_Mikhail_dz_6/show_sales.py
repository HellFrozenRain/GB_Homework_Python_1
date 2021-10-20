import sys


data = sys.argv
with open('bakery.csv', encoding='utf-8') as f:
    if len(data) > 2:
        first_string = int(data[1])
        last_string = int(data[2])
    elif len(data) == 1:
        first_string = 0
        last_string = sum(1 for line in f)
        f.seek(0)
    else:
        first_string = int(data[1])
        last_string = sum(1 for line in f)
        f.seek(0)

    for i, line in enumerate(f, 1):
        if first_string <= i and i <= last_string:
            print(line.strip())
