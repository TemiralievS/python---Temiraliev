tutors = ['Иван', 'Анастасия', 'Пётр', 'Сергей', 'Дмитрий', 'Борис', 'Елена']
klasses = ['9А', '7В', '9Б', '9В', '8Б', '10А', '10Б', '9А', '1e']
lengt_tutors = len(tutors)

tutor_klass = ((tutors[i], klass) if i < lengt_tutors else (None, klass) for i, klass in enumerate(klasses))

# print(*tutor_klass) для вывода всех пар в одну строку

print(type(tutor_klass))  # класс генератор

print(next(tutor_klass))  # для поочередного вывода пары: ученик/класс.
print(next(tutor_klass))
print(next(tutor_klass))
print(next(tutor_klass))
print(next(tutor_klass))
print(next(tutor_klass))
print(next(tutor_klass))
print(next(tutor_klass))
print(next(tutor_klass))
# print(next(tutor_klass)) истощение генератора
