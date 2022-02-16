import os
import shutil


root_dir = os.path.join(os.path.dirname(__file__), 'my_project_2')
temp_folder = os.path.join(root_dir, 'templates')

if not os.path.exists(temp_folder):
    os.makedirs(temp_folder)

for root, dirs, files in os.walk(root_dir):
    if root.count('templates'):
        for folder in dirs:
            if not os.path.exists(os.path.join(temp_folder, folder)):
                os.makedirs(os.path.join(temp_folder, folder))
        for file in files:
            src_file = os.path.join(root, file)
            copy_file = os.path.join(temp_folder, os.path.basename(root))
            if not os.path.dirname(src_file) == copy_file:
                shutil.copy(src_file, copy_file)
