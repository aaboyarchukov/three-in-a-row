from component.component import Component

class NullComponent(Component):
    # constructor
    def __init__(self, value):
        super().__init__(value)

    # define this class object is null
    def is_component_null(self):
        return True