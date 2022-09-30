"""
Задание 2.
Реализуйте два алгоритма.
Оба должны обеспечивать поиск минимального значения для списка.
Сложность первого алгоритма должна быть O(n^2) - квадратичная.
Сложность второго алгоритма должна быть O(n) - линейная.
Примечание: ПРОШУ ВАС ВНИМАТЕЛЬНО ЧИТАТЬ ЗАДАНИЕ!
-- нельзя использовать встроенные функции min() и sort()
-- каждый из двух алгоритмов нужно оформить в виде отдельной ф-ции
-- проставьте сложности каждого выражения в двух ваших алгоритмах
"""

def min_list_square_complexity(some_list): # O(N^2)

    for i in range(len(some_list)):
        min_some_list = some_list[i]
        for j in range(len(some_list)):
            if min_some_list > some_list[j]:
                min_some_list = some_list[j]
        return min_some_list

# для проверки
list_1 = [15, 1, 0, -78, 2, 3]

print(min_list_square_complexity(list_1))

def min_list_linear_complexity(some_list): #O(N)

    min_some_list = some_list[0]
    for i in range(len(some_list)):
        if min_some_list > some_list[i]:
            min_some_list = some_list[i]
    return min_some_list

print((min_list_linear_complexity(list_1)))