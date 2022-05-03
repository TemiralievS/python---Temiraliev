class MyError(Exception):
    def __init__(self, error_text):
        self.error_text = error_text

    def text(self):
        print(self.error_text)


def input_data():
    num = input('Enter number != 0: ')
    n = int(num)
    if n == 0:
        raise MyError('MyError: Zero_Division_Error: Деление на ноль')

    return n


try:
    number = input_data()
    result = 1000 / number

except ValueError:
    print('Not number!')
    number = input_data()
    result = 1000 / number
    print(f'1000 / {number :.3f} = {result :.3f}')

except MyError as error:
    print(error)
    number = input_data()
    result = 1000 / number
    print(f'1000 / {number :.3f} = {result :.3f}')

else:
    print(f'1000 / {number :.3f} = {result :.3f}')
