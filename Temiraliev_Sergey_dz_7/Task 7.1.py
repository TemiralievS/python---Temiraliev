import os

dir_name = 'my_project'
if not os.path.exists(dir_name):
    os.mkdir(dir_name)
os.chdir('my_project')
dir_list = ['settings', 'mainapp', 'adminapp', 'authapp']
for name in dir_list:
    if not os.path.exists(name):
        os.mkdir(name)
