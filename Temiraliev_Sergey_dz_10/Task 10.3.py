class Cell:

    def __init__(self, cells):
        self.cells = int(cells)

    def __str__(self):
        return f'{self.cells * "*"}'

    def __add__(self, other):
        cell = Cell(self.cells + other.cells)
        return cell

    def __sub__(self, other):
        cell = Cell(self.cells - other.cells)
        if (self.cells - other.cells) < 0:
            raise ValueError("cells can't be < 0")
        return cell

    def __mul__(self, other):
        cell = Cell(self.cells * other.cells)
        return cell

    def __floordiv__(self, other):
        cell = Cell(self.cells // other.cells)
        return cell

    def make_order(self, param):
        cell_str = ''
        for i in range(self.cells // param):
            cell_str += '*' * param + r"\n"
        cell_str += '*' * (self.cells % param)
        return cell_str


if __name__ == "__main__":
    cell_1 = Cell(5)
    cell_2 = Cell(8)
    cell_new = cell_2 * cell_1
    print(cell_new.make_order(12))
    # ************\n************\n************\n****
    print(cell_2 - cell_1)
    # ***
    print((cell_2 - cell_1).make_order(2))
    # **\n*
    print(cell_1 - cell_2)
    # Traceback (most recent call last):
    # ...
    #   raise ValueError("cells can't be < 0")
    #ValueError: cells can't be < 0
