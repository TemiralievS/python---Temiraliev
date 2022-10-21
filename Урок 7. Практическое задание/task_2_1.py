"""
Задание 2. Массив размером 2m + 1, где m – натуральное число,
заполнен случайным образом. Найдите в массиве медиану.
Медианой называется элемент ряда, делящий его на
две равные по длине части:
в одной находятся элементы,
которые не меньше медианы,
в другой – не больше медианы.

Решите задачу тремя способами:

1) с помощью сортировки, которую мы не рассматривали на уроке (Гномья, Шелла,
Кучей)

сделайте замеры на массивах длиной 10, 100, 1000 элементов
"""
from random import randint
from timeit import timeit

list_11 = [randint(-100, 100) for _ in range(11)]
list_101 = [randint(-100, 100) for _ in range(101)]
list_1001 = [randint(-100, 100) for _ in range(1001)]


def median_gnome_sort(some_list):
    size, i = len(some_list), 0

    while True:
        if i+1 == size:
            break
        if some_list[i] <= some_list[i+1]:
            i += 1
        else:
            some_list[i], some_list[i+1] = some_list[i+1], some_list[i]
            if i > 0:
                i -= 1
            else:
                i += 1
    median = some_list[int((size - 1) / 2)]
    return median


print(f'Медиана первого массива: {median_gnome_sort(list_11[:])}\n'
      f'Время выполнения:{timeit("median_gnome_sort(list_11[:])",globals=globals(),number=1000)}')

print(f'Медиана второго массива: {median_gnome_sort(list_101[:])}\n'
      f'Время выполнения:{timeit("median_gnome_sort(list_101[:])",globals=globals(),number=1000)}')

print(f'Медиана третьего массива: {median_gnome_sort(list_1001[:])}\n'
      f'Время выполнения:{timeit("median_gnome_sort(list_1001[:])",globals=globals(),number=1000)}')

"""
Медиана первого массива: -1
Время выполнения:0.021578399999999998
Медиана первого массива: -7
Время выполнения:2.3342087
Медиана первого массива: 6
Время выполнения:199.14496259999999
"""

