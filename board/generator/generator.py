from any import Any
from component.set.component_set import ComponentSet

class Generator(Any):
    # constructor
    # default size = 8x8
    def __init__(self, component_set: ComponentSet, size: int = 8):
        self.M, self.N = size, size
        self.component_set = component_set
    
    # commands

    # requests

    # pre-cond: 
    #   - size is set
    #   - component_set is not empty
    # post-cond: matrix of component are generated
    def generate(self) -> None:
        pass