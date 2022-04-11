from itertools import zip_longest

with open('users.csv', 'r', encoding='utf-8') as users:
    users_list = []
    line = users.readline()
    while line:
        users_list.append(line.replace(',', ' ').replace('\n', ''))
        line = users.readline()
    print(users_list)

with open('hobby.csv', 'r', encoding='utf-8') as hobby:
    hobby_list = []
    line = hobby.readline()
    while line:
        hobby_list = [line.replace('\n', '') for line in hobby]
        line = hobby.readline()
    print(f'Список хобби: {hobby_list}\n')

if len(users_list) >= len(hobby_list):
    user_hobby_dict = dict(zip_longest(users_list, hobby_list, fillvalue=None))
    print(f'Словарь, в котором ключи имена, а значения хобби:\n{user_hobby_dict}\n')
if len(users_list) < len(hobby_list):
    print('1')

""" Получение отдельных списков имен, фамилий, отчеств, хобби: """
surname_list = [(''.join(user)).split(' ')[0] for user in users_list]  # - фамилия
print(f'Список фамилий: {surname_list}')

name_list = [(''.join(user)).split(' ')[1].split(' ')[0] for user in users_list]  # - имя
print(f'Список имен: {name_list}')

middle_name_list = [(''.join(user)).split(' ', maxsplit=1)[1].split(' ')[1] for user in users_list]  # - отчество
print(f'Список отчеств: {middle_name_list}')
