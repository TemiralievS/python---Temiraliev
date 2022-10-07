"""
Задание 4.
Реализуйте скрипт "Кэширование веб-страниц"
Функция должна принимать url-адрес и проверять
есть ли в кэше соответствующая страница или нет

Пример кэша: {'url-адрес': 'хеш url-а'; 'url-адрес': 'хеш url-а'; ...}
Если страница в кэше есть, просто вернуть значение хеша, например, 'хеш url-а'
Если страницы в кэше нет, то вычислить хеш и записать в кэш
Подсказка: задачу решите обязательно с применением 'соленого' хеширования
и одного из алгоритмов, например, sha512
Можете усложнить задачу, реализовав ее через ООП
"""

import hashlib
from uuid import uuid4

salt = uuid4().hex
cache_dict = {}


def hash_url(some_url: str, s: str):
    hash_some_url = hashlib.sha512(s.encode() + some_url.encode()).hexdigest()
    if some_url in cache_dict.keys():
        return f'Хэш {some_url} - {cache_dict[some_url]}'
    else:
        cache_dict[some_url] = hash_some_url
        return cache_dict


print(hash_url('vk.com', salt))
print(hash_url('github.com', salt))
print(hash_url('vk.com', salt))

"""
{'vk.com': '23ad0b225f4cde1bc23b83538e7f152f0112d2e0be4ed326c0ecf676714f99abcce2294bad0faf1530c75e95ee1cbd7a5028e4858f2366878c934d8156980a6a'}
{'vk.com': '23ad0b225f4cde1bc23b83538e7f152f0112d2e0be4ed326c0ecf676714f99abcce2294bad0faf1530c75e95ee1cbd7a5028e4858f2366878c934d8156980a6a', 'github.com': 'd53d192b4f3993f7d11f0b51424aa3e442280e39568e3e9640b12f9199c12e7cd662338402c1f45af7aaeeb654bb473bad272a6ebc1ca33106c9e33d127025f7'}
Хэш vk.com - 23ad0b225f4cde1bc23b83538e7f152f0112d2e0be4ed326c0ecf676714f99abcce2294bad0faf1530c75e95ee1cbd7a5028e4858f2366878c934d8156980a6a
"""

