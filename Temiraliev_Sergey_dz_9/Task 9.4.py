class Car:
    def __init__(self, speed, color, name, is_police):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = is_police

    def go(self):
        print('Машина поехала')

    def stop(self):
        print('Машина остановилась')

    def turn(self, direction):
        print(f'Машина поехала {direction}')

    def show_speed(self):
        print(f'Скорость автомобиля: {self.speed}')


class TownCar(Car):
    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)

    def show_speed(self):
        max_speed_town = 60
        if self.speed > max_speed_town:
            print(f'Ваша скорость: {self.speed}')
            print(f'Превышение допустимой скорости. Снизьте скорость до {max_speed_town} км/ч\n')


class SportCar(Car):
    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)

    def show_speed(self):
        print(f'Скорость автомобиля: {self.speed}')


class WorkCar(Car):
    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)

    def show_speed(self):
        max_speed_work = 40
        if self.speed > max_speed_work:
            print(f'Ваша скорость: {self.speed}')
            print(f'Превышение допустимой скорости. Снизьте скорость до {max_speed_work} км/ч\n')


class PoliceCar(Car):
    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)

    def show_speed(self):
        print(f'Скорость автомобиля: {self.speed}')


if __name__ == "__main__":
    car = Car('speed', 'color', 'name', 'is_police')

    town_car = TownCar(100, 'Красный', 'mitsu', False)
    work_car = WorkCar(150, 'Зелёный', 'ЗИЛ', False)

    town_car.show_speed()
    #  Ваша скорость: 100
    # Превышение допустимой скорости. Снизьте скорость до 60 км/ч

    work_car.show_speed()
    # Ваша скорость: 150
    # Превышение допустимой скорости. Снизьте скорость до 40 км/ч
