class Matrix:
    def __init__(self, lists):
        self.rows = []
        for row in lists:
            self.rows.append(row)

    def __str__(self):
        output_matrix_repr = ''
        for row in self.rows:
            row_str = [str(number) for number in row]
            output_matrix_repr += ' '.join(row_str) + "\n"
        return output_matrix_repr

    def __add__(self, matrix):
        output_matrix = []
        for i in range(len(self.rows)):
            # собираем i-ю строку сумм чере list comprehensions
            row = [matrix.rows[i][j] + self.rows[i][j]
                   for j in range(len(self.rows[i]))]
            # добавляем i-ю строку в матрицу
            output_matrix.append(row)
        return Matrix(output_matrix)


if __name__ == '__main__':
    matr1 = Matrix([[1, 2, 3], [4, 5, 6]])
    matr2 = Matrix([[1, 2, 3], [4, 5, 6]])
    matr3 = matr1 + matr2
    print(matr1, matr2, matr3)
