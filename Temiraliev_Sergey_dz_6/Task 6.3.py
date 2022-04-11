from itertools import zip_longest

with open('users.csv', 'r', encoding='utf-8') as users:
    user_content = users.read().replace(',', ' ')
    user_list = user_content.split('\n')  # каждая строка становится элементом списка content_list
with open('hobby.csv', 'r', encoding='utf-8') as hobby:
    hobby_content = hobby.read()
    hobby_list = hobby_content.split('\n')
if len(user_list) >= len(hobby_list):
    user_hobby_dict = dict(zip_longest(user_list, hobby_list, fillvalue=None))
    print(user_hobby_dict)
if len(user_list) < len(hobby_list):
    print('1')
