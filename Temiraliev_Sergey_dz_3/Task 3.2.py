def num_translate(num):
    if num.istitle():
        num = num.lower()
        a = dictionary_translate.get(num)
        if a == None:
            print('None')
        else:
            print(a.capitalize())

    else:
        print(dictionary_translate.get(num, None))


dictionary_translate = {
    'zero': 'ноль',
    'one': 'один',
    'two': 'два',
    'three': 'три',
    'four': 'четыре',
    'five': 'пять',
    'six': 'шесть',
    'seven': 'семь',
    'eight': 'восемь',
    'nine': 'девять',
    'ten': 'десять'
}

number = input('Введите число на английском языке от 0 до 10: ')
num_translate(number)
