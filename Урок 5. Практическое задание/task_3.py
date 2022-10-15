"""
Задача 3.
В соответствии с документацией Python,
deque – это обобщение стеков и очередей.
Вот основное правило: если вам нужно
что-то быстро дописать или вытащить, используйте deque.
Если вам нужен быстрый случайный доступ, используйте list
Задача: создайте простой список (list) и очередь (deque).
Выполните различные операции с каждым из объектов.
Сделайте замеры и оцените, насколько информация в документации
соответствует дейстивтельности.
1) сравнить операции
append, pop, extend списка и дека и сделать выводы что и где быстрее
2) сравнить операции
appendleft, popleft, extendleft дека и соответствующих им операций списка
и сделать выводы что и где быстрее
3) сравнить операции получения элемента списка и дека
и сделать выводы что и где быстрее
Подсказка:
для того, чтобы снизить погрешность, желательно операции по каждой ф-ции
(append, pop и т.д.) проводить в циклах. Для замеров используйте timeit.
"""

from timeit import timeit
from collections import deque


std_list = [i for i in range(10)]
deque_smt = deque(range(10))

#  1)  append, pop, extend


def append_list():
    std_list.append(11)
    return std_list


def append_deque():
    deque_smt.append(11)
    return deque_smt


print(f'{timeit("append_list()", globals=globals(), number=10000)} - append_list',
      f'{timeit("append_deque()", globals=globals(), number=10000)} - append_deque', sep='\n')

"""
0.001760799999999993 - append_list
0.0019358000000000014 - append_deque
"""


def pop_list():
    std_list.pop()
    return std_list


def pop_deque():
    deque_smt.pop()
    return deque_smt


print(f'{timeit("pop_list()", globals=globals(), number=10000)} - pop_list',
      f'{timeit("pop_deque()", globals=globals(), number=10000)} - pop_deque', sep='\n')

"""
0.0023624000000000006 - pop_list
0.0022254000000000024 - pop_deque
"""


def extend_list():
    std_list.extend([11, 12, 13])
    return std_list


def extend_deque():
    deque_smt.extend([11, 12, 13])
    return deque_smt


print(f'{timeit("extend_list()", globals=globals(), number=10000)} - extend_list',
      f'{timeit("extend_deque()", globals=globals(), number=10000)} - extend_deque', sep='\n')

"""
0.004687700000000003 - extend_list
0.003157999999999994 - extend_deque
"""


#  2)  appendleft, popleft, extendleft


def append_left_deque():
    deque_smt.appendleft(-3)
    return deque_smt


def insert_in_list():
    std_list.insert(0, -3)
    return std_list


print(f'{timeit("append_left_deque()", globals=globals(), number=10000)} - append_left',
      f'{timeit("insert_in_list()", globals=globals(), number=10000)} - insert', sep='\n')
"""
0.0019964000000001203 - append_left
0.02831310000000009 - insert
"""


def pop_left_deque():
    deque_smt.popleft()
    return deque_smt


def pop_left_list():
    std_list.pop(0)
    return std_list


print(f'{timeit("pop_left_deque()", globals=globals(), number=10000)} - pop_left_deque',
      f'{timeit("pop_left_list()", globals=globals(), number=10000)} - pop_left_list', sep='\n')

"""
0.0017367999999999828 - pop_left_deque
0.018432899999999863 - pop_left_list
"""


def extend_left_deque():
    deque_smt.extendleft(range(11, 14))
    return deque_smt


def extend_left_list():
    for i in reversed(range(11, 14)):
        std_list.insert(0, i)
        return std_list


print(f'{timeit("extend_left_deque()", globals=globals(), number=10000)} - extend_left_deque',
      f'{timeit("extend_left_list()", globals=globals(), number=10000)} - extend_left_list', sep='\n')

"""
0.006971599999999967 - extend_left_deque
0.03766859999999994 - extend_left_list
"""


#  3)  получения элемента


def elem_list():
    return std_list[0]


def elem_deque():
    return deque_smt[0]


print(f'{timeit("elem_list()", globals=globals(), number=10000)} - elem_list',
      f'{timeit("elem_deque()", globals=globals(), number=10000)} - elem_deque', sep='\n')


"""
0.0016420000000000323 - elem_list
0.0011297000000000113 - elem_deque
"""

#  На основе замеров операции: append, pop, extend с deque и list по скорости примерно равны.
#  А операции appendleft, popleft, extendleft с deque гораздо быстрее аналогичных операций для list

