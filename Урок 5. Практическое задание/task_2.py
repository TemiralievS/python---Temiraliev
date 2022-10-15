"""
Задание 2.
Написать программу сложения и умножения двух шестнадцатеричных чисел.
При этом каждое число представляется как массив,
элементы которого это цифры числа.
Например, пользователь ввёл A2 и C4F.
Сохранить их как [‘A’, ‘2’] и [‘C’, ‘4’, ‘F’] соответственно.
Сумма чисел из примера: [‘C’, ‘F’, ‘1’],
произведение - [‘7’, ‘C’, ‘9’, ‘F’, ‘E’].
Подсказка:
Попытайтесь решить это задание в двух вариантах
1) через collections
defaultdict(list)
int(, 16)
reduce
2) через ООП
вспомните про перегрузку методов
__mul__
__add__
"""
#  1) Способ
from collections import defaultdict
from functools import reduce


nums_default_dict = defaultdict(list)
for i in range(1, 3):
    num = input(f'Введите {i} шестнадцатеричное число: ').upper()
    nums_default_dict[num] = list(num)

nums = [int(''.join(val), 16) for val in nums_default_dict.values()]
sum_nums = reduce(lambda x, y: x + y, nums)
mul_nums = reduce(lambda x, y: x * y, nums)
hexed_sum_nums = list(str(hex(sum_nums)).split('x')[1].upper())
hexed_mul_nums = list(str(hex(mul_nums)).split('x')[1].upper())

print(f'Введенные числа {nums_default_dict}')
print(f'Сумма чисел {hexed_sum_nums}')
print(f'Произведение чисел {hexed_mul_nums}')


#  2) Способ

class CalcForHex:
    def __init__(self, hex_number: str):
        self.number = int(hex_number, 16)
        self.hex_number = list(hex_number)

    def __add__(self, other):
        sum_numbers = self.number + other.number
        return f'Сумма чисел {self.hex_number} и {other.hex_number} =' \
               f'{list(str(hex(sum_numbers)).split("x")[1].upper())}'

    def __mul__(self, other):
        mul_numbers = self.number * other.number
        return f'Произведение чисел {self.hex_number} и {other.hex_number} =' \
               f' {list(str(hex(mul_numbers)).split("x")[1].upper())}'


hex_num_1 = CalcForHex('a2')
hex_num_2 = CalcForHex('c4f')
print(hex_num_1 + hex_num_2)

