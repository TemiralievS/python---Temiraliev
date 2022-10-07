"""
Задание 1.
Реализуйте функции:
a) заполнение списка, оцените сложность в O-нотации (операции нужно провдить в цикле)
   заполнение словаря, оцените сложность в O-нотации (операции нужно провдить в цикле)
   сделайте аналитику, что заполняется быстрее и почему
   сделайте замеры времени
b) получение элемента списка, оцените сложность в O-нотации (операции нужно провдить в цикле)
   получение элемента словаря, оцените сложность в O-нотации (операции нужно провдить в цикле)
   сделайте аналитику, что заполняется быстрее и почему
   сделайте замеры времени
с) удаление элемента списка, оцените сложность в O-нотации (операции нужно провдить в цикле)
   удаление элемента словаря, оцените сложность в O-нотации (операции нужно провдить в цикле)
   сделайте аналитику, что заполняется быстрее и почему
   сделайте замеры времени
ВНИМАНИЕ: в задании три пункта
НУЖНО выполнить каждый пункт
обязательно отделяя каждый пункт друг от друга
Подсказка: для замеров воспользуйтесь модулем time (см. примеры урока 1)
вы уже знаете, что такое декоратор и как его реализовать,
обязательно реализуйте ф-цию-декоратор и пусть она считает время
И примените ее к своим функциям!
"""

from time import perf_counter


def time_decorator(func):
    def wrapper(*args):
        start = perf_counter()
        func(*args)
        finish = perf_counter()
        print('time: ', finish-start)
    return wrapper

# a) заполнение списка, заполнение словаря

@time_decorator
def list_fill(n):  # O(N)
    new_list = []
    for i in range(n):
        new_list.append(i)
    print('list_fill')
    return new_list


@time_decorator
def dict_fill(n):  # O(N)
    new_dict = {}
    for i in range(n):
        new_dict[i] = i
    print('dict_fill')
    return new_dict


@time_decorator
def list_fill_compr(n):  # O(N)
    new_list = [i for i in range(n)]
    print('list_fill_compr')
    return new_list


@time_decorator
def dict_fill_compr(n):  # O(N)
    new_dict = {i: i for i in range(n)}
    print('dict_fill_comp')
    return new_dict


list_fill(100000000)
dict_fill(100000000)
list_fill_compr(100000000)
dict_fill_compr(100000000)


"""
list_fill
time:  23.6821394
dict_fill
time:  332.7927443
list_fill_compr
time:  13.243797200000017
dict_fill_comp
time:  192.95596019999994

Скорость заполнения списка выше скорости заполнения словаря как при использовании
обычного цикла, так и при использовании генераторных выражений(списковых включений).
Словарь заполняется медленнее, т.к. в отличие от списка, словарю необходимо 
производить хеширование.

"""

# b) получение элемента списка, получение элемента словаря

list_new = [i for i in range(100)]  # создал словарь и список отдельно, что бы исключить
new_dict = {i: i for i in range(100)}  # время создания из замеров времени


@time_decorator
def get_elem_list(some_list: list):  # O(N)
    print('Получение элементов списка:')
    for i in range(len(some_list)):
        return some_list[i]


@time_decorator
def get_elem_dict(some_dict: dict):  # O(N)
    print('Получение элементов словаря:')
    for i in range(len(some_dict)):
        return i, some_dict[i]


get_elem_list(list_new)
get_elem_dict(new_dict)


"""
Получение элементов списка:
time:  4.529999999999812e-05
Получение элементов словаря:
time:  1.7699999999995497e-05

Получение элемента в цикле из словаря быстрее, чем из списка, т.к. словарь 
использует поиск по хэшу(ключу), в то время как список требует каждый раз 
прохождения по списку от начала до результата. 
"""

# c) удаление элемента списка, удаление элемента словаря

@time_decorator
def del_elem_list(some_list: list):  # O(N)
    print('Удаление элементов списка:')
    for i in range(len(some_list)):
        some_list.pop()
    return some_list


@time_decorator
def del_elem_dict(some_dict: dict):  # O(N)
    print('Удаление элементов словаря:')
    for i in range(len(some_dict)):
        some_dict.pop(i)
    return some_dict


del_elem_list(list_new)
del_elem_dict(new_dict)

"""
Удаление элементов списка:
time:  5.3699999999996806e-05
Удаление элементов словаря:
time:  2.669999999999756e-05

Удаление элементов словаря происходит быстрее, т.к. словарь 
использует поиск по хэшу(ключу), в то время как список требует каждый раз 
прохождения по списку от начала до результата.
"""

