price_lst = [155.5, 15.05, 64, 95.51, 98.7, 57.1, 46.51, 82, 10.55, 100, 11.58, 87.5, 56.4, 99.91, 32.2]

print('Пункты A, B:')
print(f'Список до сортировки:{price_lst}')
print(f'id списка до сортировки:{id(price_lst)}')

price_lst.sort()

print(f'Список после сортировки: {price_lst}')
print(f'id списка после сортировки:{id(price_lst)}')

for num in price_lst:
    integer_num = int(num)
    fractional_part = int(100 * (num - integer_num))
    print(f'{integer_num} руб', '{0:02d} коп'.format(fractional_part))

print('Пункт C:')
reversed_price_lst = price_lst[::-1]
print(f'Список цен, отсортированный по убыванию: {reversed_price_lst}')

print('Пункт D:')
print(f'Список пяти самых дорогих товаров, отсортированный по возрастанию: {price_lst[-5:]}')
