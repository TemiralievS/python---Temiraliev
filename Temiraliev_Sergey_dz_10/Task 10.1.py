import copy


class Matrix:
    def __init__(self, matrix: list):
        self.__matrix = matrix

    def __str__(self):
        matrix = copy.deepcopy(self.__matrix)  # копирование списка для того, что бы не изменялся первоначальный
        for i in range(len(matrix)):  # выравнивание по левому краю с длиной строки 5 символов
            for j in range(len(matrix[i])):
                matrix[i][j] = str(matrix[i][j]).ljust(5, ' ')
        matrix_str = '\n'.join(map(str, matrix))  # перевод элементов матрицы в str
        matrix_str = matrix_str.replace('[', '').replace(']', '').replace(',', '').replace("'", '')
        return matrix_str

    def __add__(self, other):
        sum = []
        matrix_sum = []
        for i in range(len(self.__matrix)):
            if len(self.__matrix) != len(other.__matrix) or len(self.__matrix[i]) != len(other.__matrix[i]):
                # Остановка работы если размеры матриц не равны:
                raise StopIteration('Неравные размеры матриц')
            for j in range(len(self.__matrix[i])):
                row = self.__matrix[i][j] + other.__matrix[i][j]
                sum.append(row)
        # Приводим полученный список к первоначальному виду: [ [], [], ..., [] ]
        for elem in self.__matrix:
            matrix_sum = [sum[i: i + len(elem)] for i in range(0, len(sum), len(elem))]
        # Выводим матрицу в привычном виде:
        matrix_sum_str = Matrix(matrix_sum)
        return matrix_sum_str


if __name__ == "__main__":
    matr_1 = Matrix([[3, 2, 3], [4, 5, 6], [7, 8, 20]])
    matr_2 = Matrix([[1, 1, 1], [1, 63, 7], [7, 4, 6]])
    print(matr_1, '\n')
"""
Вывод:
3     2     3    
4     5     6    
7     8     20 
"""

print(matr_2, '\n')
"""
1     1     1    
1     63    7    
7     4     6 
"""
z = matr_1 + matr_2
print(z)
"""
4     3     4    
5     68    13   
14    12    26  
"""
