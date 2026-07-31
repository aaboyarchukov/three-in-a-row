from any import Any

class Component(Any):
    # constructor
    def __init__(self, value: str):
        self.__value = value
    
    # commands
    
    # requests

    def get_value(self) -> str:
        return self.__value
    
    # define this class object is null
    def is_component_null(self):
        return False
    