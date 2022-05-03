class Warehouse:
    def __init__(self, tech_type, name, num):
        self.tech_type = tech_type
        self.name = name
        self.num = num

    def __str__(self):
        return f'{self.tech_type}: [{self.name}: {self.num}]'

    def add_to_dict(self):

        """Добавление товаров на склад"""

        if self.tech_type in warehouse_dict.keys():
            tech_type = self.tech_type
            for i in range(len(warehouse_dict[tech_type])):
                if self.name == warehouse_dict[tech_type][i][0]:
                    warehouse_dict[tech_type][i][1] = self.num + warehouse_dict[tech_type][i][1]
                    return warehouse_dict
            else:
                warehouse_dict[tech_type].append([self.name, self.num])
                return warehouse_dict
        else:
            warehouse_dict[self.tech_type] = [[self.name, self.num]]
            return warehouse_dict

    def remove_from_dict(self):

        """уменьшение количества товаров на складе"""
        if self.tech_type in warehouse_dict.keys():
            tech_type = self.tech_type
            for i in range(len(warehouse_dict[tech_type])):
                if self.name == warehouse_dict[tech_type][i][0]:
                    if self.num < warehouse_dict[tech_type][i][1]:
                        direction_remove = input('Введите куда отправляется оборудование: ')
                        warehouse_dict[tech_type][i][1] = warehouse_dict[tech_type][i][1] - self.num
                        print(f'Оборудование {self.tech_type} {self.name} в количестве {self.num} '
                              f'отпралено: {direction_remove}')
                    else:
                        print(f'Вводимое количество {self.num} превышает количество на складе!')
                        return warehouse_dict
        else:
            print(f'Вводимый тип оргтехники "{self.tech_type}" отсутствует на складе!')
            return warehouse_dict


class Printer(Warehouse):
    def __init__(self, name, num):
        super().__init__(self, name, num)

    def add_from_dict(self):
        for i in warehouse_dict['Принтер']:
            keys = i[0]
            values = i[1]
            printer_dict[keys] = values
        return printer_dict


class Scaner(Warehouse):
    def __init__(self, name, num):
        super().__init__(self, name, num)

    def add_from_dict(self):
        for i in warehouse_dict['Сканер']:
            keys = i[0]
            values = i[1]
            scanner_dict[keys] = values
        return scanner_dict


class Xerox(Warehouse):
    def __init__(self, name, num):
        super().__init__(self, name, num)

    def add_from_dict(self):
        for i in warehouse_dict['Ксерокс']:
            keys = i[0]
            values = i[1]
            xerox_dict[keys] = values
        return xerox_dict


warehouse_dict = {}
printer_dict = {}
scanner_dict = {}
xerox_dict = {}

if __name__ == '__main__':
    wh_0 = Warehouse('Принтер', 'OfficeTech', 5)
    wh_1 = Warehouse('Ксерокс', 'Sony', 1)
    wh_2 = Warehouse('Принтер', 'OfficeTech', 1)  # проверка изменения количества одного товара
    wh_3 = Warehouse('Ксерокс', 'Sony', 3)
    wh_4 = Warehouse('Принтер', 'Kayocera', 3)
    wh_5 = Warehouse('Принтер', 'Kayocera', 1)  # проверка изменения количества одного товара
    wh_6 = Warehouse('Сканер', 'Kayocera', 6)
    wh_7 = Warehouse('Сканерf', 'Kayocera', 1)  # проверка на корректность вводимого типа оргтехники
    wh_8 = Warehouse('Сканер', 'Kayocera', 150)

    wh_0.add_to_dict()
    wh_1.add_to_dict()
    wh_2.add_to_dict()
    wh_3.add_to_dict()
    wh_4.add_to_dict()
    wh_5.add_to_dict()
    wh_6.add_to_dict()
    print(warehouse_dict)
    # {'Принтер': [['OfficeTech', 6], ['Kayocera', 4]], 'Ксерокс': [['Python', 4]], 'Сканер': [['Kayocera', 6]]}
    wh_5.remove_from_dict()
    print(warehouse_dict)
    # Введите куда отправляется оборудование: в канцелярию
    # Оборудование Принтер Kayocera в количестве 1 отпралено: в канцелярию
    wh_7.remove_from_dict()
    print(warehouse_dict)
    # Вводимый тип оргтехники "Сканерf" отсутствует на складе!
    wh_8.remove_from_dict()
    print(warehouse_dict)
    # Вводимое количество 150 превышает количество на складе!
    printers = Printer('', '')
    scanners = Scaner('', '')
    xeroxes = Xerox('', '')
    printers.add_from_dict()
    scanners.add_from_dict()
    xeroxes.add_from_dict()
    print(f'Принтеры: {printer_dict}\nКсероксы: {xerox_dict}\nСканеры: {scanner_dict}')
    # Принтеры: {'OfficeTech': 6, 'Kayocera': 3}
    # Ксероксы: {'Sony': 4}
    # Сканеры: {'Kayocera': 6}
