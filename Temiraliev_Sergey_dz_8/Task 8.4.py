def val_checker(func):
    def wrapper(*args):
        func(*args)
        for num in args:
            if num > 0:
                return num
            raise ValueError(f'Wrong value: {num}')

    return wrapper


@val_checker
def cube(*args):
    z = None
    for number in args:
        if number > 0:
            z = number ** 3
        print(z)


if __name__ == '__main__':
    num = cube(-55)
# Traceback (most recent call last):
#   File "C:/Users/...
#   File "C:/Users/..., line 7, in wrapper
#     raise ValueError(f'Wrong value: {num}')
# ValueError: Wrong value: -55
