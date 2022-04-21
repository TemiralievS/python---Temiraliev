import time


class TrafficLight:
    def __init__(self, color):
        self.__color = ['Красный', 'Желтый', 'Зелёный']

    def running(self):
        for _ in range(10):
            for elem in self.__color:
                if elem == 'Красный':
                    print(elem)
                    time.sleep(7)
                if elem == 'Желтый':
                    print(elem)
                    time.sleep(2)
                if elem == 'Зелёный':
                    print(elem)
                    time.sleep(10)


if __name__ == "__main__":
    light = TrafficLight('')
    light.running()

# Красный
# Желтый
# Зелёный
# ... (циклы: 2 - 8)
# Красный
# Желтый
# Зелёный
