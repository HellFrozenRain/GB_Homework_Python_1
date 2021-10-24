import os

# функция создания пути
def create_path(folder_name, subfolder_name):
    return os.path.join(folder_name, subfolder_name)

# функция создания папок
def make_dir(path):
    os.makedirs(path, exist_ok=True)

# функция создания файлов
def create_file(name, text=None):
    with open(name, 'w', encoding='utf-8') as f:
        if text:
            f.write(text)

# абсолютный путь

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

# команды для создания путей

SETTINGS_PATH = create_path('my_project', 'settings')
MAIN_APP_PATH = create_path('my_project', 'mainapp')
ADMIN_APP_PATH = create_path('my_project', 'adminapp')
AUTH_APP_PATH = create_path('my_project', 'authapp')


create_path(BASE_DIR, SETTINGS_PATH)
create_path(BASE_DIR, MAIN_APP_PATH)
create_path(BASE_DIR, ADMIN_APP_PATH)
create_path(BASE_DIR, AUTH_APP_PATH)

# команды для создания папок

make_dir(SETTINGS_PATH)
make_dir(MAIN_APP_PATH)
make_dir(ADMIN_APP_PATH)
make_dir(AUTH_APP_PATH)


# команды для создания файлов

#     test_path = create_path(SETTINGS_PATH, 'test.txt')
#     create_file(test_path)


