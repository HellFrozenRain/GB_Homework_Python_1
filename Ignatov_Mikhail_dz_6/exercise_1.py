def my_func(string):
    i = string.split()
    my_tuple = i[0], i[5].replace('"', ''), i[6]
    print(my_tuple)

with open('nginx_logs.txt', 'r', encoding='utf-8') as file_1:
    for line in file_1:
        my_func(line)