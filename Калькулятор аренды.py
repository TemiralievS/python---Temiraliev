voltage_new = int(input('Введите нынешние показания электросчетчика: '))
voltage_old = int(input('Введите прошлые показания электросчетчика: '))
voltage_coast = 5.92
summ_voltage = (voltage_new - voltage_old) * voltage_coast

cold_water_new = int(input('Введите нынешние показания прибора учета холодной воды:  '))
cold_water_old = int(input('Введите прошлые показания прибора учета холодной воды:  '))
cold_water_coast = 43.57
sum_cold_water = (cold_water_new - cold_water_old) * cold_water_coast

hot_water_new = int(input('Введите нынешние показания прибора учета горячей воды:  '))
hot_water_old = int(input('Введите прошлые показания прибора учета горячей воды:  '))
hot_water_coast = 211.67
sum_hot_water = (hot_water_new - hot_water_old) * hot_water_coast

water_move_coast = 32.02
water_move = ((cold_water_new - cold_water_old) + (hot_water_new - hot_water_old)) * water_move_coast


summ_rent = 29000 + sum_cold_water + sum_hot_water + summ_voltage + water_move

print(f'В этом месяце потрачено - электроэнергии: {voltage_new - voltage_old}, на сумму {summ_voltage},\n'
      f'                        - холодной воды: {cold_water_new - cold_water_old}, на сумму {sum_cold_water},\n'
      f'                        - горячей воды: {hot_water_new - hot_water_old}, на сумму {sum_hot_water},\n')
print(f'Водоотведение в объеме: {(cold_water_new - cold_water_old) + (hot_water_new - hot_water_old)}, '
      f'на сумму: {water_move}')
print(f'Суммарная арендная плата за месяц: {summ_rent :.0f}')

stop = input()


