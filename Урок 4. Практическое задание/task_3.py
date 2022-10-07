"""
Задание 3.
Приведен код, формирующий из введенного числа
обратное по порядку входящих в него
цифр и вывести на экран.
Сделайте профилировку каждого алгоритма через timeit
Обязательно предложите еще свой вариант решения!
Сделайте вывод, какая из четырех реализаций эффективнее и почему!
"""

from timeit import timeit


def revers(enter_num, revers_num=0):
    if enter_num == 0:
        return revers_num #!!!!!! в коде задания стоит просто return, по смыслу добавил revers_num
    else:
        num = enter_num % 10
        revers_num = (revers_num + num / 10) * 10
        enter_num //= 10
        revers(enter_num, revers_num)


def revers_2(enter_num, revers_num=0):
    while enter_num != 0:
        num = enter_num % 10
        revers_num = (revers_num + num / 10) * 10
        enter_num //= 10
    return revers_num


def revers_3(enter_num):
    enter_num = str(enter_num)
    revers_num = enter_num[::-1]
    return revers_num


def revers_4(enter_num):
    num_revers = int(''.join(reversed(str(enter_num))))
    return num_revers


print(
    timeit("revers(12344455)", globals=globals(), number=10000),
    timeit("revers_2(12344455)", globals=globals(), number=10000),
    timeit("revers_3(12344455)", globals=globals(), number=10000),
    timeit("revers_4(12344455)", globals=globals(), number=10000)
)

"""
0.0491192 - время выполнения revers
0.0242048 - время выполнения revers_2
0.005100999999999994 - время выполнения revers_3
0.011591300000000013 - время выполнения revers_4 (свой вариант решения)

Как видно из приведенных результатов замеров, самыми эффективными 
являются варианты: 1 и 4. Т.к. они используют встроенные функции Python.
Самым быстрым способом оказалось использование среза, вторым по скорости - reversed()

"""