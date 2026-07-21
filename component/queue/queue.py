from any import Any

class ComponentQueue(Any):
    # constructor
    def __init__(self):
        self.queue = []
    
    # commands
    # pre-cond: queue is init
    # post-cond: size of queue increased
    def add(self):
        pass
    
    # requests
    # pre-cond: queue is not empty
    # post-cond: size of queue decreased and we get head of list
    def pop(self) -> None:
        pass