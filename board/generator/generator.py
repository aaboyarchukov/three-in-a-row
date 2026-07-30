from any import Any
from component.set.component_set import ComponentSet
from matrix import Matrix
class Generator(Any):
    # constructor
    # default size = 8x8
    def __init__(self, component_set: ComponentSet, size: int = 8):
        self.M, self.N = size, size
        self.component_set = component_set
        self.matrix = Matrix(size)
    
    # commands

    # requests

    # pre-cond: 
    #   - size is set
    #   - component_set is not empty
    # post-cond: matrix of component are generated
    def generate(self) -> Matrix:
        # generate components and fill
        self.matrix.fill_all()
        new_matrix = self.matrix

        return new_matrix