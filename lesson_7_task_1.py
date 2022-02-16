import os

root_dir = 'my_project'
folders = ['settings', 'mainapp', 'adminapp', 'authapp']

for i in folders:
    dir_path = os.path.join(root_dir, i)
    if not os.path.exists(dir_path):
        os.makedirs(dir_path, exist_ok=True)
