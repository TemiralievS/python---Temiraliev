""" *(вместо 1) Решить задачу генерации нечётных чисел от 1 до n (включительно), не используя ключевое слово yield. """

nums = int(input('Введите число: '))

nums_gen = (num for num in range(1, nums + 1, 2))
next(nums_gen)
# или print(next(nums_gen)) для вывода в консоль