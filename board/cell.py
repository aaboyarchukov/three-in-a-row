from any import Any
from component.component import Component
from component.set.component_set import ComponentSet
class Cell(Any):

    # constructor
    def __init__(self, x, y, component: Component):
        self.__x = x
        self.__y = y
        self.component = component
        self.__TO_DELETE_STATE = False

    # commands
    # pre-cond: cell is not ready to deleted yet
    # post-cond: cell is ready to deleted
    def set_to_delete(self):
        deleted = self.__TO_DELETE_STATE == True
        if deleted:
            return
        
        self.component = ComponentSet.delete_component
        self.__TO_DELETE_STATE = True

    def reset_delete_state(self):
        self.__TO_DELETE_STATE = False

    # requests
    def get_delete_state(self) -> bool:
        return self.__TO_DELETE_STATE

    def get_component(self) -> Component:
        return self.component

    def get_x(self):
        return self.__x
        
    def get_y(self):
        return self.__y
    