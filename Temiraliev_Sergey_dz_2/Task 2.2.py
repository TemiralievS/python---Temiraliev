phrase_lst = ['в', '5', 'часов', '17', 'минут', 'температура', 'воздуха', 'была', '+5', 'градусов']
phrase_lst[1] = '05'
phrase_lst[8] = '+05'
phrase_lst.insert(1, '"')
phrase_lst.insert(3, '"')
phrase_lst.insert(5, '"')
phrase_lst.insert(7, '"')
phrase_lst.insert(12, '"')
phrase_lst.insert(14, '"')
print(f'Измененный список с добавленными кавычками и числами дополненными до двух разрядов:\n{phrase_lst}')
phrase_lst_str = ' '.join(phrase_lst)
print(f'Строка, сформированная из списка:\n{phrase_lst_str}')
