"""
Задание 1.
Приведен код, который позволяет сохранить в
массиве индексы четных элементов другого массива
Сделайте замеры времени выполнения кода с помощью модуля timeit
Попробуйте оптимизировать код, чтобы снизить время выполнения
Проведите повторные замеры
ОБЯЗАТЕЛЬНО! Добавьте аналитику: что вы сделали и какой это принесло эффект
"""
from timeit import timeit

old_arr = [i for i in range(201)]


def func_1(nums):
    new_arr = []
    for i in range(len(nums)):
        if nums[i] % 2 == 0:
            new_arr.append(i)
    return new_arr


def new_func(nums: list):
    new_arr = [i for i in range(len(nums)) if nums[i] % 2 == 0]
    return new_arr


print(func_1(old_arr))
print(new_func(old_arr))

print(
    timeit('func_1(old_arr)', globals=globals(), setup='from __main__ import func_1', number=1000), '\n',
    timeit('new_func(old_arr)', globals=globals(), setup='from __main__ import new_func', number=1000)
)
"""
0.059902 - время выполнения старого кода, в котором используется итератор с функцией append
0.037570300000000015 - время выполнения нового кода с использованием спискового включения
Использование спискового включения (list comprehension) оказалось быстрее итератора 
с функцией append. 
"""

