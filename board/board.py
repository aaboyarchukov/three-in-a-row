from generator.generator import Generator
from any import Any

class Board(Any):
    # constructor
    def __init__(self, generator: Generator):
        self.board_matrix = None
        self.generator = generator
    
    # commands
    
    # заполняет опустевшие клетки, если комбинации собираются
    # pre-cond:
    #   - board_matrix is not empty 
    #   - on board exists valid sequence
    # post-cond: empty cells are filling
    def fill(self):
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

    # requests

    # pre-cond: board_matrix is empty 
    # post-cond: board_matrix is not empty
    def generate(self) -> None:
        # self.generate.generate()
        pass
    
    # pre-cond: board_matrix is not empty 
    # post-cond: has found at least one valid sequence OR hasn't found either
    def scan_on_valid_sequence(self) -> bool:
        pass