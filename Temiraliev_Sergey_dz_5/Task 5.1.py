""" Написать генератор нечётных чисел от 1 до n (включительно), используя ключевое слово yield """


def odd_nums(nums):
    for num in range(1, nums + 1, 2):
        yield num


odd_to_15 = odd_nums(15)
next(odd_to_15)
# или print(next(odd_to_15)) для вывода в консоль
