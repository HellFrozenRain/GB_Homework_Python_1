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
AUTH_APP_PATH = create_path('my_project', 'authapp')


create_path(BASE_DIR, SETTINGS_PATH)
create_path(BASE_DIR, MAIN_APP_PATH)
create_path(BASE_DIR, AUTH_APP_PATH)

# команды для создания папок

make_dir(SETTINGS_PATH)
make_dir(MAIN_APP_PATH)
make_dir(AUTH_APP_PATH)

# команды для создания файлов в settings

init_path = create_path(SETTINGS_PATH, '__init__.py')
dev_path = create_path(SETTINGS_PATH, 'dev.py')
prod_path = create_path(SETTINGS_PATH, 'prod.py')
create_file(init_path)
create_file(dev_path)
create_file(prod_path)

# команды для создания файлов и папок в mainapp

init_path = create_path(MAIN_APP_PATH, '__init__.py')
models_path = create_path(MAIN_APP_PATH, 'models.py')
views_path = create_path(MAIN_APP_PATH, 'views.py')
create_file(init_path)
create_file(models_path)
create_file(views_path)

TEMPLATES_PATH = create_path(MAIN_APP_PATH, 'templates')
make_dir(TEMPLATES_PATH)

mainapp_path = create_path(TEMPLATES_PATH, 'mainapp')
make_dir(mainapp_path)
base_path = create_path(mainapp_path, 'base.html')
index_path = create_path(mainapp_path, 'index.html')
create_file(base_path)
create_file(index_path)

# команды для создания файлов и папок в authapp

init_path = create_path(AUTH_APP_PATH, '__init__.py')
models_path = create_path(AUTH_APP_PATH, 'models.py')
views_path = create_path(AUTH_APP_PATH, 'views.py')
create_file(init_path)
create_file(models_path)
create_file(views_path)

TEMPLATES_PATH = create_path(AUTH_APP_PATH, 'templates')
make_dir(TEMPLATES_PATH)

authapp_path = create_path(TEMPLATES_PATH, 'authapp')
make_dir(authapp_path)
base_path = create_path(authapp_path, 'base.html')
index_path = create_path(authapp_path, 'index.html')
create_file(base_path)
create_file(index_path)
