def type_logger(any_func):
    def wrapper(*args):
        any_func(*args)
        for nums in args:
            print(any_func.__name__, f'({nums}:{type(nums)})')

    return wrapper


@type_logger
def cube(*args):
    z = 1
    for number in args:
        z = number ** 3
        print(f'Result = {z}')


if __name__ == '__main__':
    num = cube(6, 5)

# Result = 216
# Result = 125
# cube (6:<class 'int'>)
# cube (5:<class 'int'>)
