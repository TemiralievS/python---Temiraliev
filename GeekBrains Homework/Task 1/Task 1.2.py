new_lst = list(range(1, 1001))
cube_lst = []
total_lst = []

i = 0

while i < len(new_lst):
    cube_num = new_lst[i] ** 3
    cube_lst.append(cube_num)
    i += 2
print('Список состоящий из кубов нечётных чисел от 1 до 1000: ', cube_lst)

# a) Вычислить сумму тех чисел из этого списка, сумма цифр которых делится нацело на 7.
# Например, число «19 ^ 3 = 6859» будем включать в сумму, так как 6 + 8 + 5 + 9 = 28 – делится нацело
# на 7. Внимание: использовать только арифметические операции!

for num in cube_lst:
    figure_sum = 0
    z_num = num  # создание новой переменной, что бы переменная num не перезаписывалась каждый проход цикла
    while z_num != 0:
        figure_sum = figure_sum + z_num % 10
        z_num = z_num // 10
    if figure_sum % 7 == 0:
        total_lst.append(num)
print('a) Сумма чисел из списка, состоящего из кубов,\nсумма цифр которых делится нацело на 7: ', sum(total_lst))
# b) К каждому элементу списка добавить 17 и заново вычислить сумму тех чисел из этого списка,
# сумма цифр которых делится нацело на 7.
add_17_list = []
total_17_lst = []
for num in cube_lst:
    num += 17
    add_17_list.append(num)
print()
for num in add_17_list:
    figure_sum = 0
    z_num = num  # создание новой переменной, что бы переменная num не перезаписывалась каждый проход цикла
    while z_num != 0:
        figure_sum = figure_sum + z_num % 10
        z_num = z_num // 10
    if figure_sum % 7 == 0:
        total_17_lst.append(num)
print('b) Список, получившийся после прибавки к каждому элементу 17: ', add_17_list)
print('Сумма чисел из списка, состоящего из кубов с прибавкой 17,'
      '\nсумма цифр которых делится нацело на 7: ', sum(total_17_lst))
