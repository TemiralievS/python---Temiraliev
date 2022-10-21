"""
Задание 2. Массив размером 2m + 1, где m – натуральное число,
заполнен случайным образом. Найдите в массиве медиану.
Медианой называется элемент ряда, делящий его на
две равные по длине части:
в одной находятся элементы,
которые не меньше медианы,
в другой – не больше медианы.
Решите задачу тремя способами:
3) с помощью встроенной функции поиска медианы
сделайте замеры на массивах длиной 10, 100, 1000 элементов
В конце сделайте аналитику какой трех из способов оказался эффективнее
"""

from random import randint
from timeit import timeit
from statistics import median


list_11 = [randint(-100, 100) for _ in range(11)]
list_101 = [randint(-100, 100) for _ in range(101)]
list_1001 = [randint(-100, 100) for _ in range(1001)]


def statistics_median(some_list: list):
    return median(some_list)


print(f'Медиана первого массива: {statistics_median(list_11[:])}\n'
      f'Время выполнения:{timeit("statistics_median(list_11[:])",globals=globals(),number=1000)}')

print(f'Медиана второго массива: {statistics_median(list_101[:])} \n'
      f'Время выполнения:{timeit("statistics_median(list_101[:])",globals=globals(),number=1000)}')

print(f'Медиана третьего массива: {statistics_median(list_1001[:])}\n'
      f'Время выполнения:{timeit("statistics_median(list_1001[:])",globals=globals(),number=1000)}')

"""
Медиана первого массива: -6
Время выполнения:0.0010040999999999939
Медиана второго массива: 13 
Время выполнения:0.005958199999999997
Медиана третьего массива: 0
Время выполнения:0.13333399999999998

На основании произведенных замеров трех разных способов поиска медианы, 
самым эффективным оказался способ №3: с помощью встроенной функции поиска медианы median()

Наименее эффективным оказался способ №1 с помощью Гномьей сортировки, с последующим получением медианы.
"""