import os
import shutil

os.chdir('my_project')
new_dir = 'templates'
file_list = []
if not os.path.exists(new_dir):
    os.mkdir(new_dir)  # создание отдельной папки templates
for dir_path, dir_names, file_names in os.walk('.'):
    for filename in file_names:  # создание списка, в котором указаны пути ко всем файлам
        file_list.append(os.path.join(dir_path, filename))
html_list = []
for file in file_list:
    if file[-4:] == 'html':
        html_list.append(''.join(file).replace('\\', '/'))  # создание списка, в котором указаны пути к .html файлам
print(html_list)
os.chdir('./templates')
for html in html_list:
    html_dir_name = html.split('/')[-2]
    if not os.path.exists(html_dir_name):
        os.mkdir(html_dir_name)  # создание соответствующих папок в templates
    if html_dir_name in html:  # копирование .html файлов в соответствующие папки в templates
        shutil.copyfile(html.replace('./', '../'), f'{html_dir_name}/{html.split("/")[-1]}')
