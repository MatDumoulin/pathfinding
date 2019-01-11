from enum import Enum

class Cells(Enum):
    empty = '0'
    wall = "#"

class Position:
    row = -1
    col = -1
    
    def __init__(self, row, col):
        self.row = row
        self.col = col

    def __hash__(self):
        return hash((self.row, self.col))

    def __str__(self):
        return str(self.row) + "-" + str(self.col)

    def __eq__(self, other):
        return self.row == other.row and self.col == other.col

    def __ne__(self, other):
        # Not strictly necessary, but to avoid having both x==y and x!=y
        # True at the same time
        return not(self == other)