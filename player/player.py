from any import Any
from board.cell import Cell
from board.board import Board
class Player(Any):
    # constructor
    def __init__(self, board: Board):
        self.board = board
    
    # commands

    # pre-cond:
    #   - board is not empty
    #   - coordinates of components in move are in range of matrix
    # post-cond: components have moved at board
    def move(self, first_cell: Cell, second_cell: Cell):
        self.board.move(first_cell, second_cell)

    def end_game(self):
        pass


    # requests
    
    def get_board(self) -> Board:
        return self.board