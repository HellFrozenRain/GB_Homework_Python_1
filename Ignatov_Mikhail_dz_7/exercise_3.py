import os
import shutil

destination = os.path.join('my_project', 'templates')
for root_dir, list_dir, files in os.walk('my_project'):
    if list_dir == ['templates']:
        source = os.path.join(root_dir, 'templates')
        print(source)
        shutil.copytree(source, destination, dirs_exist_ok=True)
