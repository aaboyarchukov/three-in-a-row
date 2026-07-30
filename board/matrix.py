# closed class

from any import Any
from cell import Cell

class Matrix(Any):
    # construstor
    def __init__(self, size):
        self.array = [Cell] * size

    # commands
    
    # pre-cond: base array not null
    # post-cond: base array has been filling
    def fill_all(self, arrange_component: list[Cell]):
        pass

    def fill_empty_cell(self, arrange_component: list[Cell]):
        pass

    # requests
    