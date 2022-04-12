class Cell:
    def __init__(self, units):
        self.units = int(units)

    def __str__(self):
        return f'В клетке {self.units} ячеек'

    def __add__(self, other):
        return Cell(self.units + other.units)

    def __sub__(self, other):
        if (self.units - other.units) <= 0:
            raise ValueError('разность ячеек меньше 0')
        return self.units - other.units

    def __mul__(self, other):
        return Cell(self.units * other.units)

    def __floordiv__(self, other):
        if self.units > other.units:
            return Cell(self.units // other.units)
        return Cell(other.units // self.units)

    def make_order(self, row):
        return ("*" * row + '\n') * (self.units // row)+('*' * (self.units % row))


one = Cell(2)
two = Cell(5)
print(one - two)
print(Cell.make_order(one * two, int(input('how many units in the row? '))))
