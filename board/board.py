from generator.generator import Generator
from any import Any
from cell import Cell
from matrix import Matrix

class Board(Any):
    # constructor
    def __init__(self, generator: Generator):
        self.generator = generator
        self.board_matrix = Matrix()

        self.BOARD_FILL_STATE = False
    
    # commands
    
    # pre-cond:
    #   - board_matrix is not empty 
    #   - on board exists valid sequence
    #   - coordinates of components in move are in range of matrix
    # post-cond: components have moved at board
    def move(self, first_cell: Cell, second_cell: Cell):
        pass

    # заполняет опустевшие клетки, если комбинации собираются
    # pre-cond:
    #   - board_matrix is not empty 
    #   - on board exists valid sequence
    # post-cond: empty cells are filling
    def fill(self):
        # if scan_on_valid_sequence is true
            # then fill
        pass

    def shift_down(self):
        # if scan_on_valid_sequence is true
            # then fill
        pass
    
    # pre-cond: 
    #   - board_matrix is not empty
    #   - player has moved
    # post-cond:
    #   - amount of components on board decreased
    #   - amount of players moves increased
    #   - amount of total points increased
    def delete_sequence(self):
        # after move -> delete sequence
        pass

    # pre-cond: board_matrix is empty
    # post-cond: board_matrix is not empty
    def fill(self, matrix: Matrix):
        is_board_filled = self.BOARD_FILL_STATE == True
        if is_board_filled:
            return
        
        self.board_matrix = matrix
        self.BOARD_FILL_STATE = True

    # requests
    
    # pre-cond: board_matrix is not empty 
    # post-cond: has found at least one valid sequence OR hasn't found either
    def scan_on_valid_sequence(self) -> bool:
        pass

    # pre-cond: board_matrix is not generated 
    # post-cond: board_matrix is generated
    def generate(self) -> Matrix:
        return self.generator.generate()