def thesaurus(*args):
    """
    Функция принимает в качестве аргументов имена сотрудников и возвращающую словарь,
    в котором ключи — первые буквы имён, а значения — списки, содержащие имена, начинающиеся с соответствующей буквы.
    Добавлена сортировка словаря по ключам.
    """
    name_dictionary = {}
    for arg in args:
        first_letter = arg[0].upper()
        name_dictionary[first_letter] = name_dictionary.setdefault(first_letter, []) + [arg.capitalize()]
    print(f'Первоначальный словарь {name_dictionary}')
    sorted_tuple = sorted(name_dictionary.items(), key=lambda x: x[0])
    sorted_dictionary = dict(sorted_tuple)
    print(f'Отсортированный словарь {sorted_dictionary}')


thesaurus('Марина', 'Игорь', 'Лена', 'Лиза', 'иван', 'Антон', 'Сергей', 'андрей', 'Борис')
