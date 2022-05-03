class Complex:

    def __init__(self, real, non_real):
        self.real = real
        self.non_real = non_real

    def __add__(self, other):
        new_real = self.real + other.real
        new_non_real = self.non_real + other.non_real
        new_complex_num = complex(new_real, new_non_real)
        return f'Результат сложения двух комплексных чисел:' \
               f'{complex(self.real, self.non_real)} + {complex(other.real, other.non_real)} = {new_complex_num}'

    def __mul__(self, other):
        new_real = self.real * other.real + self.non_real * other.non_real * (-1)
        new_non_real = self.real * other.non_real + self.non_real * other.real
        new_complex_num = complex(new_real, new_non_real)
        return f'Результат умножения двух комплексных чисел: ' \
               f'{complex(self.real, self.non_real)} * {complex(other.real, other.non_real)} = {new_complex_num}'


if __name__ == '__main__':
    num_complex_1 = Complex(9, 2)
    num_complex_2 = Complex(6, -8)
    new_complex_add = num_complex_2 + num_complex_1
    new_complex_mul = num_complex_2 * num_complex_1
    print(new_complex_add)
    # Результат сложения двух комплексных чисел:(6-8j) + (9+2j) = (15-6j)
    print(new_complex_mul)
    # Результат умножения двух комплексных чисел: (6-8j) * (9+2j) = (70-60j)
