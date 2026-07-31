from any import Any
from component.set.component_set import ComponentSet
from component.component import Component
from component.null_component import NullComponent

class ComponentQueue(Any):
    # constructor
    def __init__(self):
        self.queue: list[Component] = []

        # 0 - failed
        # 1 - success
        self.ADD_STATE = 0
    
    # commands
    # pre-cond: queue is init
    # post-cond: size of queue increased
    def add(self, component: Component):
        self.queue.append(component)
        self.ADD_STATE = 1
    
    # requests
    # pre-cond: 
    #   - queue is not empty
    #   - success add component
    # post-cond: size of queue decreased and we get head of list
    def pop(self) -> Component:
        unsuccess_add = self.ADD_STATE != 1
        if unsuccess_add:
            return NullComponent(value="")

        empty_queue = self.len() == 0
        if empty_queue:
            return NullComponent(value="")
        
        return self.queue.pop(0)

    # return queue len
    def len(self):
        return len(self.queue)
    
    # returns add state
    def get_add_state(self):
        return self.ADD_STATE
    
    # define this class object is not null
    def is_component_null(self) -> bool:
        return False