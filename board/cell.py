from any import Any
from component.component import Component
class Cell(Any):

    # constructor
    def __init__(self, x, y, component: Component):
        self.x = x
        self.y = y
        self.component = component
        self.to_delete_state = False
    