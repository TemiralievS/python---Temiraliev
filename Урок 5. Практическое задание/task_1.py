"""
Задание 1.
Пользователь вводит данные о количестве предприятий,
их наименования и прибыль за 4 квартала
(т.е. 4 отдельных числа) для каждого предприятия.
Программа должна определить среднюю прибыль (за год для всех предприятий)
и вывести наименования предприятий, чья прибыль выше среднего и отдельно
вывести наименования предприятий, чья прибыль ниже среднего
Подсказка:
Для решения задачи обязательно примените коллекцию из модуля collections
Для лучшего освоения материала можете сделать
несколько варианто решения этого задания,
применив несколько коллекций из модуля collections
Пример:
Введите количество предприятий для расчета прибыли: 2
Введите название предприятия: Рога
через пробел введите прибыль данного предприятия
за каждый квартал(Всего 4 квартала): 235 345634 55 235
Введите название предприятия: Копыта
через пробел введите прибыль данного предприятия
за каждый квартал(Всего 4 квартала): 345 34 543 34
Средняя годовая прибыль всех предприятий: 173557.5
Предприятия, с прибылью выше среднего значения: Рога
Предприятия, с прибылью ниже среднего значения: Копыта
"""

from collections import defaultdict


num_firms = int(input('Введите количество предприятий для расчета прибыли: '))
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
average = [firm for firm in firms_total_profit.keys() if firms_total_profit[firm] == middle_profit]


print(f'Годовая прибыль предприятий: {firms_total_profit}')
print(f'Средняя годовая прибыль всех предприятий: {middle_profit}')
print(f'Предприятия, с прибылью выше среднего значения: {above_average}\n'
      f'Предприятия, с прибылью ниже среднего значения: {below_average}\n'
      f'Предприятия, с прибылью равной среднему значению: {average}')

