from any import Any
from component.component import Component
class Cell(Any):

    # constructor
    def __init__(self, x, y, component: Component):
        self.x = x
        self.y = y
        self.component = component
        self.TO_DELETE_STATE = False

    # commands
    def set_to_delete(self):
        pass
    # requests
    def get_delete_state(self) -> bool:
        return self.TO_DELETE_STATE
    