numbers_lst = list(range(0, 101))
for number in numbers_lst:
    if number == 0 or 5 <= number <= 20 or 25 <= number <= 30 or 35 <= number <= 40 or 45 <= number <= 50 \
            or 55 <= number <= 60 or 65 <= number <= 70 or 75 <= number <= 80 or 85 <= number <= 90 \
            or 95 <= number <= 100:
        print(number, 'процентов')
    elif 2 <= number <= 4 or 22 <= number <= 24 or 32 <= number <= 34 or 42 <= number <= 44 or 52 <= number <= 54 \
            or 62 <= number <= 64 or 72 <= number <= 74 or 82 <= number <= 84 or 92 <= number <= 94:
        print(number, 'процента')
    elif number == 1 or number == 21 or number == 31 or number == 41 or number == 51 or number == 61 or number == 71 \
            or number == 81 or number == 91:
        print(number, 'процент')
