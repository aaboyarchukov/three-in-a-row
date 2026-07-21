from any import Any

class Component(Any):
    def __init__(self):
        pass
    
    # commands
    
    # после генерации компоненты добавляются в очередь, оттуда на доску
    # pre-cond: components
    # post-cond:
    def add_to_queue():
        pass
    
    # requests
    
    # генерирует последовательность из компонентов
    # pre-cond:
    # post-cond:
    def generate_sequence():
        pass
    