# closed class

from any import Any
from cell import Cell

class Matrix(Any):
    # construstor
    def __init__(self, size):
        self.array = [Cell] * size
        self.EMPTY_METRIX_STATE = False
        self.EMPTY_MATRIX_CELLS_STATE = True

    # commands
    
    # pre-cond: 
    #   - base array not null
    #   - arrange components not null
    # post-cond: base array has been filling
    def fill_all(self, arrange_component: list[Cell]):
        if len(arrange_component) == 0:
            return
        
        not_empty = self.EMPTY_METRIX_STATE != True
        if not_empty:
            return
        
        for i in range(len(self.array)):
            self.array[i] = arrange_component[i]

        self.EMPTY_METRIX_STATE = False

    # pre-cond: there are in matrix empty cells
    # post-cond: there aren't in matrix empty cells
    def fill_empty_cell(self, arrange_component: list[Cell]):
        not_empty_cells = self.EMPTY_MATRIX_CELLS_STATE != True
        if not_empty_cells:
            return
        
        self.EMPTY_MATRIX_CELLS_STATE = False

    # requests
    