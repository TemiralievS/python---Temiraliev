"""
Задание 2. Массив размером 2m + 1, где m – натуральное число,
заполнен случайным образом. Найдите в массиве медиану.
Медианой называется элемент ряда, делящий его на
две равные по длине части:
в одной находятся элементы,
которые не меньше медианы,
в другой – не больше медианы.

Решите задачу тремя способами:

2) без сортировки

сделайте замеры на массивах длиной 10, 100, 1000 элементов
"""
from random import randint
from timeit import timeit
from copy import deepcopy


list_11 = [randint(-100, 100) for _ in range(11)]
list_101 = [randint(-100, 100) for _ in range(101)]
list_1001 = [randint(-100, 100) for _ in range(1001)]


def median_non_sort(some_list: list):
    some_list_copy = deepcopy(some_list)
    for i in range(int((len(some_list_copy)-1)/2)):
        some_list.pop(some_list.index(max(some_list)))
    return max(some_list)


print(f'Медиана первого массива: {median_non_sort(list_11[:])}\n'
      f'Время выполнения:{timeit("median_non_sort(list_11[:])",globals=globals(),number=1000)}')

print(f'Медиана второго массива: {median_non_sort(list_101[:])} \n'
      f'Время выполнения:{timeit("median_non_sort(list_101[:])",globals=globals(),number=1000)}')

print(f'Медиана третьего массива: {median_non_sort(list_1001[:])}\n'
      f'Время выполнения:{timeit("median_non_sort(list_1001[:])",globals=globals(),number=1000)}')

"""
Медиана первого массива: 10
Время выполнения:0.0173528
Медиана второго массива: 6 
Время выполнения:0.2995734
Медиана третьего массива: 1
Время выполнения:15.733149000000001
"""

