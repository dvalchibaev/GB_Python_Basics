class Cell:
    def __init__(self, cells_number):
        self.cells_number = cells_number

    def __add__(self, other):
        output_cell = Cell(0)
        if type(output_cell) == type(other):
            output_cell.cells_number = self.cells_number + other.cells_number
            return output_cell

    def __sub__(self, other):
        output_cell = Cell(0)
        if type(output_cell) == type(other):
            output_cell.cells_number = self.cells_number - other.cells_number
            if output_cell.cells_number >= 0:
                return output_cell
            else:
                print('too many cells in second cell!')

    def __mul__(self, other):
        output_cell = Cell(0)
        if type(output_cell) == type(other):
            output_cell.cells_number = self.cells_number * other.cells_number
            return output_cell

    def __floordiv__(self, other):
        output_cell = Cell(0)
        if type(output_cell) == type(other):
            output_cell.cells_number = self.cells_number // other.cells_number
            return output_cell

    def make_order(self, cells_in_row):
        cells_counter = self.cells_number
        output_cells_repr = ''
        while cells_counter > cells_in_row:
            # добавляем * по килличеству символов в строке
            output_cells_repr += ''.join(['*' for _ in range(cells_in_row)])
            output_cells_repr += '\n'
            cells_counter -= cells_in_row
        # добавляем все, что осталось в последнюю строку
        output_cells_repr += ''.join(['*' for _ in range(cells_counter)])
        output_cells_repr += '\n'
        return output_cells_repr


if __name__ == '__main__':
    a = Cell(4)
    b = Cell(3)
    c = a + b
    d = c - b
    e = a * b
    f = c // b
    cells = (a, b, c, d, e, f)
    for cell in cells:
        print(cell.cells_number)
    print(e.make_order(3))
