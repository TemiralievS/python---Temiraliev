duration = int(input('Введите промежуток времени в секундах: '))
if 0 < duration < 60:
    time_sec = duration
    print('Введеный промежуток времени составляет: ', time_sec, 'сек')
elif 60 <= duration < 3600:
    time_min = duration // 60
    time_sec = duration % 60
    print('Введеный промежуток времени составляет: ', time_min, 'мин', time_sec, 'сек')
elif 3600 <= duration < 86400:
    time_hours = duration // 3600
    time_min = (duration % 3600) // 60
    time_sec = (duration % 3600) % 60
    print('Введеный промежуток времени составляет: ', time_hours, 'час', time_min, 'мин', time_sec, 'сек')
elif 86400 < duration:
    time_days = duration // 86400
    time_hours = (duration % 86400) // 3600
    time_min = ((duration % 86400) % 3600) // 60
    time_sec = ((duration % 86400) % 3600) % 60
    print('Введеный промежуток времени составляет: ', time_days, 'дн', time_hours, 'час', time_min, 'мин', time_sec,
          'сек')
