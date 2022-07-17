import datetime
now = datetime.datetime.now()

voltage = int(input('Введите нынешние показания электросчетчика: '))
cold_water = int(input('Введите нынешние показания прибора учета холодной воды:  '))
hot_water = int(input('Введите нынешние показания прибора учета горячей воды:  '))

voltage_coast = 5.92
cold_water_coast = 43.57
hot_water_coast = 211.67

now_new = f'Показания от {now.day:02}:{now.month:02}:' \
          f'{now.year} электричество: {voltage}, холодная вода: {cold_water}, горячая вода: {hot_water}'
print(now_new)
text_f = open('показания.txt', 'r')
file_last = text_f.readlines()[-1]
print(file_last)

old_voltage = int(file_last.split('электричество: ')[1].split(',')[0])
print(old_voltage)

old_cold_water = int(file_last.split('холодная вода: ')[1].split(',')[0])
print(old_cold_water)

old_hot_water = int(file_last.split('горячая вода: ')[1].split('\n')[0])
print(old_hot_water)

"""досчитать + вывод в отдельный файл с суммой аренды и комм. услуг + добавление показаний в другой файл по дате"""

text_f.close()
text_f = open('показания.txt', 'a+')
"""text_f.write(f'{now_new} \n')"""
text_f.close()