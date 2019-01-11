from utils.moves import Move
from utils.cells import Position
from utils.queue import Queue

class Dikjstra: 

    def __init__(self):
        pass

    # The first element of the path will be the start. The last element is the end. 
    # It returns None if no path is valid.
    def shortestPath(self, grid, start, end):
        # Contains all the cells that were visited, such that we are not visiting them again.
        # The key is the visited cell, and the value is the cell used to get to this cell.
        visited = { self.getPositionAsKey(start): None }
        # Contains the cells to visit, in order.
        queue = self.getUnvisitedNeighbors(grid, visited, start)
        # The shortest path found from 'start' to 'end' in the grid.
        shortestPath = Queue()
        # If we have reached the destination
        hasReachedDestination = False

        # Going all the way to the end
        while len(queue) > 0 and not hasReachedDestination:
            cell = queue.pop()
            visited[ self.getPositionAsKey(cell["value"]) ] = cell["previous"]
            # If current points to the same position as end
            if cell["value"] == end:
                hasReachedDestination = True
                shortestPath = self.reconstructPath(cell, visited)
            else:
                queue.appendQueue( self.getUnvisitedNeighbors(grid, visited, cell["value"]) )


        return shortestPath


    def getUnvisitedNeighbors(self, grid, visited, cell):
        unvisited = Queue()

        for move in Move.asIterable():
            neighbor = Position(cell.row + move['row'], cell.col + move['col'])

            if self.getPositionAsKey(neighbor) not in visited and grid.isWalkable(neighbor.row, neighbor.col):
                unvisited.append( {"value":neighbor, "previous":cell} )

        return unvisited


    def reconstructPath(self, lastCellOfPath, cellHistory):
        path = Queue()
        cell = lastCellOfPath["value"]

        while cell is not None:
            path.append(cell)
            cell = cellHistory[ self.getPositionAsKey( cell ) ]
        # To start the path from its beginning
        path.reverse()

        return path


    def getPositionAsKey(self, position):
        return str(position)


