class Stationery:
    def __init__(self, title):
        self.title = title

    def draw(self):
        print('Запуск отрисовки\n')


class Pen(Stationery):
    def __init__(self, title):
        super().__init__(title)

    def draw(self):
        print(f'Для записи текста необходима {self.title}\n')


class Pencil(Stationery):
    def __init__(self, title):
        super().__init__(title)

    def draw(self):
        print(f'Для создания наброска нужен {self.title}\n')


class Handle(Stationery):
    def __init__(self, title):
        super().__init__(title)

    def draw(self):
        print(f'Для выделения текста необходим {self.title}\n')


if __name__ == '__main__':
    stationery = Stationery('')
    stationery.draw()
    # Запуск отрисовки

    pen = Pen('Ручка')
    pen.draw()  # Для записи текста необходима Ручка
    pencil = Pencil('Карандаш')
    pencil.draw()
    # Для создания наброска нужен Карандаш

    handle = Handle('Маркер')
    handle.draw()
    # Для выделения текста необходим Маркер
