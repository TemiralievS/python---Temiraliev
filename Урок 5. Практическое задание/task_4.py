"""
Задача 4.
Создайте обычный словарь и упорядоченный словарь OrderedDict.
Выполните операции, равные по смыслу, с каждым из словарей и сделайте замеры.
Опишите полученные результаты, сделайте выводы
И есть ли смысл исп-ть OrderedDict в Python 3.6 и более поздних версиях
"""

from timeit import timeit
from collections import OrderedDict
from random import randint

new_std_dict = {'q': 1, 'w': 2, 'e': 3, 'r': 4, 't': 5, 'y': 6}
new_ord_dict = OrderedDict([('q', 1), ('w', 2), ('e', 3), ('r', 4), ('t', 5), ('y', 6)])


def elem_std_dict():
    return new_ord_dict['q']


def elem_ord_dict():
    return new_std_dict['q']


print(f'{timeit("elem_std_dict()", globals=globals(), number=10000)} - elem_std_dict',
      f'{timeit("elem_ord_dict()", globals=globals(), number=10000)} - elem_ord_dict', sep='\n')

"""
0.0011537000000000006 - elem_std_dict
0.001139100000000004 - elem_ord_dict
"""


def new_std_dict_keys():
    return new_std_dict.keys()


def new_ord_dict_keys():
    return new_ord_dict.keys()


print(f'{timeit("new_std_dict_keys()", globals=globals(), number=1000000)} - new_std_dict_keys',
      f'{timeit("new_ord_dict_keys()", globals=globals(), number=1000000)} - new_ord_dict_keys', sep='\n')

"""
0.21992849999999997 - new_std_dict_keys
0.20294030000000002 - new_ord_dict_keys
"""

def new_std_dict_values():
    return new_std_dict.values()


def new_ord_dict_values():
    return new_ord_dict.values()


print(f'{timeit("new_std_dict_values()", globals=globals(), number=1000000)} - new_std_dict_values',
      f'{timeit("new_ord_dict_values()", globals=globals(), number=1000000)} - new_ord_dict_values', sep='\n')

"""
0.19742339999999997 - new_std_dict_values
0.20999059999999992 - new_ord_dict_values
"""


def new_std_dict_items():
    return new_std_dict.items()


def new_ord_dict_items():
    return new_ord_dict.items()


print(f'{timeit("new_std_dict_items()", globals=globals(), number=1000000)} - new_std_dict_items',
      f'{timeit("new_ord_dict_items()", globals=globals(), number=1000000)} - new_ord_dict_items', sep='\n')


"""
0.2023706999999999 - new_std_dict_items
0.22642969999999996 - new_ord_dict_items
"""


def create_std_dict():
    dictionary = dict()
    for i in range(1000):
        dictionary[i] = randint(1, 100)
    return dictionary


def create_ord_dict():
    dictionary = OrderedDict()
    for i in range(1000):
        dictionary[i] = randint(1, 100)
    return dictionary


print(f'{timeit("create_std_dict()", globals=globals(), number=1000000)} - create_std_dict',
      f'{timeit("create_ord_dict()", globals=globals(), number=1000000)} - create_ord_dict', sep='\n')


"""
0.2125767999999999 - new_std_dict_items
0.21669319999999992 - new_ord_dict_items
"""

#  На основании замеров равные по смыслу операции для dict и OrderedDict
#  выполняются примерно с одной скоростью.
#  Использовать OrderedDict в Python 3.6 и более поздних версиях смысла нет,
#  т.к. с версии 3.6 словари сохраняют порядок