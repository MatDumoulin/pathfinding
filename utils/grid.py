from pprint import pprint
from utils.cells import Cells

class Grid:
    cells = []

    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.cells = self.createGrid(width, height, Cells.empty.value)
    
    # Factory method to create a 2d array.
    def createGrid(self, width, height, defaultValue):
        return [[defaultValue for i in range(width)] for j in range(height)]

    def isWalkable(self, row, col):
        return row >= 0 and row < self.height and col >= 0 and col < self.width and self.cells[row][col] is not Cells.wall.value

    def print(self):
        for row in self.cells:
            print(' '.join([str(x) for x in row]))