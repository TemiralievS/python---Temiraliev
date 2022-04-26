from abc import ABC, abstractmethod


class Clothes(ABC):
    def __init__(self, name):
        self.name = name

    def clothes_name(self):
        return self.name

    @abstractmethod
    def cloth_amount(self):
        pass
        """ Вывод количества материала для одной единицы продукции """


class Coat(Clothes):
    def __init__(self, size):
        super().__init__(self)
        self.size = size

    @property
    def size(self):
        return self.__size

    # если размер введен не правильно (слишком маленький или большой) происходит обнуление расчета ткани
    @size.setter
    def size(self, size):
        if size < 19 or size > 100:
            self.__size = -3.25
        else:
            self.__size = size

    def cloth_amount(self):
        amount = self.size / 6.5 + 0.5
        cloth_sum.append(amount)
        return f'Для пошива пальто необходимо {amount :.1f} метров ткани'


class Costume(Clothes):
    def __init__(self, height):
        super().__init__(self)
        self.height = height

    @property
    def height(self):
        return self.__height

    # если рост введен не правильно (очень маленький или большой) происходит обнуление расчета ткани
    @height.setter
    def height(self, height):
        if height < 40 or height > 280:
            self.__height = -0.15
        else:
            self.__height = height

    def cloth_amount(self):
        amount = self.height * 2 + 0.3
        cloth_sum.append(amount)
        return f'Для пошива костюма необходимо {amount :.1f} метров ткани'


cloth_sum = []

if __name__ == "__main__":
    coat = Coat(36)
    costume = Costume(150)
    coat.cloth_amount()  # +1 пальто размера 36
    coat = Coat(50)
    coat.cloth_amount()  # +1 пальто размера 50
    costume.cloth_amount()  # +1 костюм для роста 150
    costume = Costume(176)
    costume.cloth_amount()  # +1 костюм для роста 176
    print(f'Суммарное количество ткани: {sum(cloth_sum) :.1f}')
    print(cloth_sum)
    # Суммарное количество ткани: 666.8
    # [6.038461538461538, 8.192307692307693, 300.3, 352.3] в список попадают значения количества
    # ткани для каждого пальто или костюма (36, 50, 150, 176 соответственно)
