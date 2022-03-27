phrase_lst = ['инженер-конструктор Игорь', 'главный бухгалтер МАРИНА', 'токарь высшего разряда нИКОЛАй',
              'директор аэлита']
word_lst = []
name_lst = []

for element in phrase_lst:
    small_lst = element.split()
    word_lst.append(small_lst)
print(f'Элементы первоначального списка преобразованные во вложенные списки:\n{word_lst}')

for word in word_lst:
    word[-1] = word[-1].title()
    print(f'Привет, {word[-1]}')
    name_lst.append(word[-1])
print(f'Список имен из элементов первоначального списка:{name_lst}')
