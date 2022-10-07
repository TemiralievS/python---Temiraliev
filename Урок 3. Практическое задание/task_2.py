"""
Задание 2.
Ваша программа должна запрашивать пароль
Для этого пароля вам нужно вычислить хеш, используя алгоритм sha256
Для генерации хеша обязательно нужно использовать криптографическую соль
Обязательно выведите созданный хеш
Далее программа должна запросить пароль повторно и вновь вычислить хеш
Вам нужно проверить, совпадает ли пароль с исходным
Для проверки необходимо сравнить хеши паролей
ПРИМЕР:
Введите пароль: 123
В базе данных хранится строка: 555a3581d37993843efd4eba1921
f1dcaeeafeb855965535d77c55782349444b
Введите пароль еще раз для проверки: 123
Вы ввели правильный пароль
Важно: для хранения хеша и соли воспользуйтесь или файлом (CSV, JSON)
или, если вы уже знаете, как Python взаимодействует с базами данных,
воспользуйтесь базой данный sqlite, postgres и т.д.
п.с. статья на Хабре - python db-api
"""

from uuid import uuid4
import hashlib
import json

salt = uuid4().hex
password = str(input('Введите пароль: '))


def password_hash(p, s):  # хеширование пароля+соли и запись в файл
    hash_password_salt = hashlib.sha256(s.encode() + p.encode()).hexdigest()
    with open('password_file.json', 'w') as pass_write:
        json.dump(hash_password_salt, pass_write)


password_1 = str(input('Введите пароль еще раз: '))


def password_check(p, s):  # извлечение данных из файла и сравнение с хэшем пароля+соли
    hash_password = hashlib.sha256(s.encode() + p.encode()).hexdigest()
    with open('password_file.json', 'r') as pass_check:
        pass_check_str = pass_check.readline().split('"')[1]
        if pass_check_str == hash_password:
            print('Пароль верный')
        else:
            print('Пароль неверный')


password_hash(password, salt)
password_check(password_1, salt)

