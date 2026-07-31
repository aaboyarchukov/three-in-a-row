from any import Any
from component.set.component_set import ComponentSet
from component.component import Component
from board.cell import Cell

class Generator(Any):
    # constructor
    # default size = 8x8
    def __init__(self, component_set: ComponentSet, size: int = 8):
        self.size = size
        self.component_set = component_set
        
    
    # commands

    # requests

    # pre-cond: 
    #   - size is set
    #   - component_set is not empty
    # post-cond: matrix of component are generated
    def generate(self) -> list[Cell]:
        # generate components
        result: list[Cell] = []

        for i in range(self.size):
            for j in range(self.size):
                random_component = self.component_set.random_component()

                result.append(Cell(i, j, random_component))

        return result