from time import perf_counter

""" Старый способ """
start = perf_counter()
src = [2, 2, 2, 7, 23, 1, 13, 13, 44, 3, 2, 10, 7, 4, 11]
unique_nums = []
for num in src:
    if src.count(num) == 1:
        unique_nums.append(num)
finish = perf_counter()
print(unique_nums, f'time 1: {finish - start}')

""" List Comprehensions """
start = perf_counter()
src = [2, 2, 2, 7, 23, 1, 13, 13, 44, 3, 2, 10, 7, 4, 11]
unique_nums = [num for num in src if src.count(num) == 1]
finish = perf_counter()
print(unique_nums, f'time 2: {finish - start}')
