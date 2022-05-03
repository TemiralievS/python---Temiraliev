class Date:

    @classmethod
    def day_month_year(cls, date: str):
        date_list_str = date.split('-')
        try:
            date_list_int = [int(elem) for elem in date_list_str]
            for elem in date_list_int:
                date_int_list.append(elem)
            return date_list_int

        except ValueError:
            return 'There are not only numbers in the date'

    @staticmethod
    def date_valid():
        day = date_int_list[0]
        month = date_int_list[1]
        year = date_int_list[2]
        while True:
            if len(str(year)) != 4:
                return 'Year is not correct. Should be: len(year) = 4'
            if month in range(1, 13):

                if month in [1, 3, 5, 7, 8, 10, 12]:
                    if day in range(1, 32):
                        print('')
                    else:
                        return 'Day is not correct! Day not in (1-31)!'

                elif month in [4, 6, 9, 11]:
                    if day in range(1, 31):
                        print('')
                    else:
                        return 'Day is not correct!Day not in (1-30)!'

                elif month == 2 and year % 4 == 0:
                    if day in range(1, 30):
                        print('')
                    else:
                        return 'Day is not correct!Day not in (1-29)!'

                elif month == 2 and year % 4 != 0:
                    if day in range(1, 29):
                        print('')
                    else:
                        return 'Day is not correct! The year is not a leap year!'

            else:
                return 'Month not in (1-12)!'

            return f'Date is correct {day}:{month:02d}:{year}'


date_int_list = []



Date.day_month_year('11-05-2022')
print(Date.date_valid())
# Date is correct
# _______________________
"""
Date.day_month_year('29-02-2021')
print(Date.date_valid())
# Day is not correct! The year is not a leap year!
# _______________________
Date.day_month_year('01-02-21')
print(Date.date_valid())
# Year is not correct. Should be: len(year) = 4 <-- если условие, что год должен быть четырёхзначным,
# не указано в задании.
Вводить по очереди.
"""
