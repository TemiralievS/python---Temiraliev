import os
import shutil

with open("./config.yaml", "r", encoding="utf-8") as structure:
    structure_list = []
    line = structure.readline()
    while line:
        structure_list.append(line.replace('\n', ''))
        line = structure.readline()
    print(structure_list)
    for elem in structure_list:  # создание главной деректории
        if elem[0] != ' ' and elem[-1] == ':':
            main_dir = elem.split(':')[0]
            if not os.path.exists(main_dir):
                os.mkdir(main_dir)
            os.chdir(main_dir)
        directs_list = []
        if elem[1] == ' ' and (elem[-1] == ':' and elem[2] != ' '):  # создание дочерних директорий
            sub_dir = elem.split(':')[0].split('  ')[1]
            directs_list.append(sub_dir)
            if not os.path.exists(sub_dir):
                os.mkdir(sub_dir)

    print(directs_list)
"""Программа недоделана, на данном этапе генерируются папки: главная(my_project) и три дочерних(authapp, 
   mainapp, settings). При дальнейшей работе через цикл и условия if, программа начинает последовательно
   генерировать вложенные папки, например: my_project\authapp\mainapp\settigs\templates), что не соответствует 
   условиям задания."""