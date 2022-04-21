class Worker:
    def __init__(self, name, surname, position, income: dict = {'wage': 0, 'bonus': 0}):
        self.name = name
        self.surname = surname
        self.position = position
        self._income = income


class Position(Worker):
    def __init__(self, name, surname, position, income: dict = {'wage': 0, 'bonus': 0}):
        super().__init__(name, surname, position, income)

    def get_full_name(self):
        full_name = self.name + ' ' + self.surname
        print(f'Полное имя сотрудника: {full_name}.\nДолжность: {self.position}')

    def get_total_income(self):
        total_income = self._income['wage'] + self._income['bonus']
        print(f'Заработная плата с учетом бонусов: {total_income} рублей')


if __name__ == "__main__":
    staffer = Position('Sergey', 'Temiraliev', 'Operator-programmer CNC', {'wage': 50000, 'bonus': 10000})
    staffer.get_full_name()
    staffer.get_total_income()

# Полное имя сотрудника: Sergey Temiraliev.
# Должность: Operator-programmer CNC
# Заработная плата с учетом бонусов: 60000
