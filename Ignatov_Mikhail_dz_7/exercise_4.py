import os
folder = input('enter folder') # директория
files_size_list = []
result_dict = {}

for root, dirs, files in os.walk(folder): # путь, список папок, список файлов
    for file in files:
        file_path = os.path.join(root, file) # путь к файлу
        files_size_list.append(os.stat(file_path).st_size) # размер файла
max_size = max(files_size_list) # размер самого большого файла


# цикл создания ключей в зависимости от размера самого большого файла
i = 1
for el in range(len(str(max_size))):
    i = i * 10
    result_dict[i] = 0

# цикл присваивания значений
for number in files_size_list:
    result_dict[10 ** len(str(number))] = result_dict[10 ** len(str(number))] + 1

print(result_dict)

