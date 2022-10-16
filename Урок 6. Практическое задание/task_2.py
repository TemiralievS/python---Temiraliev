"""
Задание 2.
Попытайтесь выполнить профилирование памяти в любом скрипте с рекурсией.
Вам нужно обнаружить проблему в процессе этого. Но проблема связана не с тем,
что рекурсия потребляет много памяти, а с самим процессом замеров.
Опищите эту проблему и найдите простой путь ее решения.
Опишите этот путь и покажите его применение
"""
"""
Ответ:
При профилировании рекурсивной функции происходит многократное профилирование
т.к рекурсивная функция вызывает сама себя. 
Таким образом замера рекурсии через profile, нужно рекурсию обернуть в другую функцию
Например:
"""

from memory_profiler import profile


@profile
def wrapper_recursion():
    def recursion():

        operator = input('Введите операцию (+, -, *, / или 0 для выхода):_')

        operator_list = ['+', '-', '*', '/', '0']

        if operator == '0':  # базовый случай
            print('ВЫХОД')

        elif operator not in operator_list:
            print('Вы ввели неверную операцию')
            return recursion()

        else:
            try:
                num_1 = float(input('Введите первое число: '))

            except ValueError:
                print('Вы ввели не число')
                return recursion()

            try:
                num_2 = float(input('Введите второе число: '))

            except ValueError:
                print('Вы ввели не число')
                return recursion()

            if operator == operator_list[0]:
                print(f'{num_1}+{num_2}={num_1 + num_2}')
                return recursion()

            if operator == operator_list[1]:
                print(f'{num_1}-{num_2}={num_1 - num_2}')
                return recursion()

            if operator == operator_list[2]:
                print(f'{num_1}*{num_2}={num_1 * num_2}')
                return recursion()

            if operator == operator_list[3]:
                if num_2 != 0:
                    print(f'{num_1}/{num_2}={num_1 / num_2}')
                    return recursion()
                else:
                    print('Деление на ноль невозможно')
                    return recursion()
    recursion()


wrapper_recursion()