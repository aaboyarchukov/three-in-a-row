from any import Any
from component.set.component_set import ComponentSet

class Component(Any):
    # constructor
    def __init__(self, component_set: ComponentSet):
        self.component_set = component_set
    
    # commands
    
    # после генерации компоненты добавляются в очередь, оттуда на доску
    # pre-cond: queue is init
    # post-cond: size of queue increase
    def add_to_queue(self):
        pass
    
    # requests
    
    # генерирует последовательность из компонентов
    # pre-cond: component set is set
    # post-cond: generate sequence of component with certain size
    def generate_sequence(self, size: int = 3) -> None:
        pass
    