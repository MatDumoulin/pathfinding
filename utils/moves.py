from enum import Enum

class Move:
    UP = {"row":-1, "col":0}
    DOWN = {"row":1, "col": 0}
    LEFT = {"row":0, "col": -1}
    RIGHT = {"row":0, "col": 1}

    @staticmethod
    def asIterable():
        return [Move.UP, Move.DOWN, Move.LEFT, Move.RIGHT]
    