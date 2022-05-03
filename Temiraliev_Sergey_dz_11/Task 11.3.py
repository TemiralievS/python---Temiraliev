class MyError(Exception):
    def __init__(self, text):
        self.text = text


if __name__ == '__main__':
    num_input_list = []

    while True:

        try:
            num = input('Введите число: ')
            if num == 'stop':
                print('Введение данных завершено')
                break
            if not num.isdigit():
                raise MyError('')
            else:
                num_int = int(num)
                num_input_list.append(num_int)
                print('Для завершения ввода данных введите "stop"')
        except MyError:
            print('Вводите только числа')

    print(num_input_list)
