from utils.grid import Grid
from utils.cells import Position, Cells
from dikjstra.forGrids import Dikjstra

# Map set up
gameMap = Grid(5, 10)

gameMap.cells[2][3] = Cells.wall.value
#gameMap.cells[3][4] = Cells.wall.value
gameMap.cells[4][3] = Cells.wall.value
gameMap.cells[3][2] = Cells.wall.value

gameMap.print()


# Dikjstra
dikjstra = Dikjstra()
start = Position(0, 0)
end = Position(3, 3)

path = dikjstra.shortestPath(gameMap, start, end)

i = 0
for cell in path.asList():
    gameMap.cells[cell.row][cell.col] = i
    i = i + 1

gameMap.print()

print("Path:", path)
