"""
Задание 1.
Вам нужно взять 5 любых скриптов, написанных ВАМИ в рамках работы над ДЗ
курсов Алгоритмы и Основы Python
На каждый скрипт нужно два решения - исходное и оптимизированное.
Вы берете исходное, пишете что это за задание и с какого оно курса.
Далее выполняете профилирование скрипта средствами memory_profiler
Вы оптимизируете исходное решение.
Далее выполняете профилирование скрипта средствами memory_profiler
Вам нужно написать аналитику, что вы сделали для оптимизации памяти и
чего добились.
ВНИМАНИЕ:
1) скрипты для оптимизации нужно брать только из сделанных вами ДЗ
курсов Алгоритмы и Основы
2) нельзя дублировать, коды, показанные на уроке
3) для каждого из 5 скриптов у вас отдельный файл, в нем должна быть версия до
и версия после оптимизации
4) желательно выбрать те скрипты, где есть что оптимизировать и не брать те,
где с памятью и так все в порядке
5) не нужно писать преподавателю '''я не могу найти что оптимизировать''', это
отговорки. Примеров оптимизации мы перечислили много: переход с массивов на
генераторы, numpy, использование слотов, применение del, сериализация и т.д.
"""

# Алгоритмы. 5 урок. Задание 1.

from memory_profiler import memory_usage, profile
from collections import defaultdict
import json


def decor_memory(func):
    def wrapper(*args):
        m1 = memory_usage()
        func(*args)
        m2 = memory_usage()
        print(f'memory - {m2[0] - m1[0]}')
    return wrapper



# До оптимизации

@decor_memory
def firms_profits():
    num_firms = 2
    firms_monthly_profit = defaultdict(list)
    firms_total_profit = defaultdict(int)

    i = 1
    while i <= num_firms:
        firms = input(f'Введите название предприятия {i}: ')
        profit_str = input('через пробел введите прибыль данного предприятия за каждый квартал(Всего 4 квартала): ').split()
        profit_int = [int(val) for val in profit_str]  # перевел значения из str в int
        firms_monthly_profit[firms] = profit_int
        firms_total_profit[firms] = sum(profit_int)
        i += 1

    total_profit = [val for val in firms_total_profit.values()]  # список со всеми годовыми доходами
    middle_profit = sum(total_profit)/num_firms  # среднее годовое значение

    above_average = [firm for firm in firms_total_profit.keys() if firms_total_profit[firm] > middle_profit]
    below_average = [firm for firm in firms_total_profit.keys() if firms_total_profit[firm] < middle_profit]


    print(f'Годовая прибыль предприятий: {firms_total_profit}')
    print(f'Средняя годовая прибыль всех предприятий: {middle_profit}')
    print(f'Предприятия, с прибылью выше среднего значения: {above_average}\n'
          f'Предприятия, с прибылью ниже среднего значения: {below_average}')


firms_profits()

# После оптимизации


@decor_memory
def json_firms_profits():
    num_firms = 2
    firms_monthly_profit = defaultdict(list)
    firms_total_profit = defaultdict(int)

    i = 1
    while i <= num_firms:
        firms = input(f'Введите название предприятия {i}: ')
        profit_str = input('через пробел введите прибыль данного предприятия за каждый квартал(Всего 4 квартала): ').split()
        profit_int = [int(val) for val in profit_str]  # перевел значения из str в int
        firms_monthly_profit[firms] = profit_int
        firms_total_profit[firms] = sum(profit_int)
        i += 1

    total_profit = [val for val in firms_total_profit.values()]  # список со всеми годовыми доходами
    middle_profit = sum(total_profit) / num_firms  # среднее годовое значение

    above_average = [firm for firm in firms_total_profit.keys() if firms_total_profit[firm] > middle_profit]
    below_average = [firm for firm in firms_total_profit.keys() if firms_total_profit[firm] < middle_profit]
    dumped_total = json.dumps(total_profit)
    dumped_middle = json.dumps(middle_profit)
    dumped_above = json.dumps(above_average)
    dumped_below = json.dumps(below_average)

    print(f'Годовая прибыль предприятий: {json.loads(dumped_total)}')
    print(f'Средняя годовая прибыль всех предприятий: {json.loads(dumped_middle)}')
    print(f'Предприятия, с прибылью выше среднего значения: {json.loads(dumped_above)}\n'
          f'Предприятия, с прибылью ниже среднего значения: {json.loads(dumped_below)}')


json_firms_profits()


"""
Занимаемая память - 0.046875 без использования json
Занимаемая память - 0.0234375 при использовании json

Согласно замерам с использованием json
объем занимаемой памяти уменьшился в 2 раза 
"""

