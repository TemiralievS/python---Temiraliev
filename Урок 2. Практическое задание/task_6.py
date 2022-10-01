"""
Задание 6.	В программе генерируется случайное целое число от 0 до 100.
Пользователь должен его отгадать не более чем за 10 попыток. После каждой
неудачной попытки должно сообщаться больше или меньше введенное пользователем
число, чем то, что загадано. Если за 10 попыток число не отгадано,
то вывести загаданное число.
Решите через рекурсию. В задании нельзя применять циклы.
"""
import random


def guess_recursion(n, try_count=0):

    user_num = int(input(f'Количество попыток {10-try_count}\n'
                         f'Угадайте число (0-100):  '))
    if user_num < 0:
        print('Число должно быть больше нуля!')
        return guess_recursion(n, try_count + 1)
    else:
        if n == user_num:
            print(f'Вы угадали. Загаданное число {n}')
        elif try_count == 10:
            print(f'У Вас закончились попытки. Загаданное число {n}')
        else:
            if user_num > n:
                print('Загаданное число меньше вашего')
                return guess_recursion(n, try_count + 1)
            elif user_num < n:
                print('Загаданное число больше вашего')
                return guess_recursion(n, try_count + 1)


guess_recursion(random.randint(0, 100))