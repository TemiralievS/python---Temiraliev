def num_translate(num):
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
