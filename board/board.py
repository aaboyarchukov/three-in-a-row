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
        not_valid_move = self.__is_valid_move(first_cell, second_cell)
        if not_valid_move:
            self.__IS_MOVING_STATE = -1
            return

        

        # push to suscribe that we are get points for move

        self.__IS_MOVING_STATE = 1

    # заполняет опустевшие клетки, если комбинации собираются
    # pre-cond:
    #   - board_matrix is not empty 
    #   - on board exists valid sequence
    # post-cond: empty cells are filling
    def shift_down(self):
        not_empty_cells = self.IS_EMPTY_CELLS_STATE == False
        if not_empty_cells:
            return
        # if scan_on_valid_sequence is true
            # then fill
        # processing
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
        self.IS_EMPTY_CELLS_STATE = True

    # pre-cond: board_matrix is empty
    # post-cond: board_matrix is not empty
    def fill(self):
        is_board_filled = self.BOARD_FILL_STATE == True
        if is_board_filled:
            return

        self.board_matrix.fill_all()

        self.BOARD_FILL_STATE = True

    # requests
    
    # pre-cond: board_matrix is not empty
    # post-cond: move has been checked for validation    
    def __is_valid_move(self, first_cell, second_cell) -> bool:
        pass

    # pre-cond: board_matrix is not empty 
    # post-cond: has found at least one valid sequence OR hasn't found either
    def scan_on_valid_sequence(self) -> bool:
        pass

    # pre-cond: 
    #   - board_matrix is not empty
    #   - sequence is not empty
    # post-cond: sequence has scaned and it's valid or not valid
    def is_valid_sequence(self, sequence: list[Cell]) -> bool:
        pass

    # pre-cond: board_matrix is not generated 
    # post-cond: board_matrix is generated
    def generate(self):
        is_generated = self.BOARD_GENERATED_STATE == True
        if is_generated:
            return
        
        sequence = self.generator.generate()
        self.fill(sequence)

        self.BOARD_GENERATED_STATE = True

    def get_moving_state(self) -> int:
        # 0 - init
        # 1 - sucess
        # -1 - failed
        return self.__IS_MOVING_STATE