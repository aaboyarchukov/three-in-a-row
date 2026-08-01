from board.generator.generator import Generator
from any import Any
from board.cell import Cell
from board.matrix import Matrix

class Board(Any):
    # constructor
    def __init__(self, generator: Generator):
        self.generator = generator
        self.board_matrix = Matrix()

        self.BOARD_FILL_STATE = False
        self.BOARD_GENERATED_STATE = False

        # 0 - init
        # 1 - sucess
        # -1 - failed
        self.__IS_MOVING_STATE = 0

        self.IS_EMPTY_CELLS_STATE = False
        
    
    # commands
    
    # pre-cond:
    #   - board_matrix is not empty 
    #   - on board exists valid sequence
    #   - coordinates of components in move are in range of matrix
    # post-cond: components have moved at board
    def move(self, first_cell: Cell, second_cell: Cell):
        valid_sequence = self.__valid_sequence(first_cell, second_cell)
        if valid_sequence == []:
            self.__IS_MOVING_STATE = -1
            return

        # push to suscribe that we are get points for move
        self.board_matrix.move(first_cell, second_cell)
        self.__IS_MOVING_STATE = 1

        self.delete_sequence(valid_sequence)
        self.shift_down()

        

    # заполняет опустевшие клетки, если комбинации собираются
    # pre-cond:
    #   - board_matrix is not empty 
    #   - on board exists valid sequence
    # post-cond: empty cells are filling
    def shift_down(self):
        not_empty_cells = self.IS_EMPTY_CELLS_STATE == False
        if not_empty_cells:
            return
        # processing
        self.board_matrix.collapse_grid()

        self.IS_EMPTY_CELLS_STATE = False
    
    # pre-cond: 
    #   - board_matrix is not empty
    #   - player has moved
    # post-cond:
    #   - amount of components on board decreased
    #   - amount of players moves increased
    #   - amount of total points increased
    #   - there are empty cells
    def delete_sequence(self, sequence: list[Cell]):
        is_empty = self.BOARD_FILL_STATE == False
        if is_empty:
            return
        
        # after move -> delete sequence
        self.board_matrix.remove_sequence(sequence)
        self.IS_EMPTY_CELLS_STATE = True

    # pre-cond: board_matrix is empty
    # post-cond: board_matrix is not empty
    def fill(self):
        is_board_filled = self.BOARD_FILL_STATE == True
        if is_board_filled:
            return

        sequence = self.generator.generate()
        self.board_matrix.fill_all(sequence)

        self.BOARD_FILL_STATE = True

    # requests
    
    # pre-cond: board_matrix is not empty
    # post-cond: move has been checked for validation    
    def __valid_sequence(self, first_cell: Cell, second_cell: Cell) -> list[Cell]:
        return self.board_matrix.valid_sequence(first_cell, second_cell)
    
    # pre-cond: board_matrix is not generated 
    # post-cond: board_matrix is generated
    def generate(self):
        is_generated = self.BOARD_GENERATED_STATE == True
        if is_generated:
            return
        
        sequence = self.generator.generate()
        self.fill(sequence)

        self.BOARD_GENERATED_STATE = True

    # pre-cond: board_matrix is not empty
    # post-cond: moving state reset to init (0)
    def reset_moving_state(self):
        self.__IS_MOVING_STATE = 0

    def get_moving_state(self) -> int:
        # 0 - init
        # 1 - sucess
        # -1 - failed
        return self.__IS_MOVING_STATE

    def get_matrix(self) -> Matrix:
        return self.board_matrix