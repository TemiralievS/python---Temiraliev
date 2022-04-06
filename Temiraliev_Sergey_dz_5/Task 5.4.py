from time import perf_counter
from sys import getsizeof
"""Решение старым способом"""
start = perf_counter()
nums = [100, 300, 2, 12, 500, 1, 666, 4, 10, 7, 1, 78, 123, 550]
result_1 = []

for i in range(len(nums) - 1):
    if nums[i + 1] > nums[i]:
        result_1.append(nums[i + 1])

finish = perf_counter()
print(f'1 способ:\n'
      f'Получившийся список: {result_1}\n'
      f'time: {finish - start}\n'
      f'memory: {getsizeof(result_1)}')


"""Решение с использованием List Comprehensions"""
start = perf_counter()
nums = [100, 300, 2, 12, 500, 1, 666, 4, 10, 7, 1, 78, 123, 550]
result_2 = [nums[i+1] for i in range(len(nums)-1) if nums[i + 1] > nums[i]]
finish = perf_counter()
print(f'2 способ:\n'
      f'Получившийся список: {result_2}\n'
      f'time: {finish - start}\n'
      f'memory: {getsizeof(result_2)}')
