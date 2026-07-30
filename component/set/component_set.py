from any import Any
import random

class ComponentSet(Any):

    def __init__(self):
        pass

    # льготный класс содержит набор из доступных компонентов
    components = ["😀", "🎉", "🚀", "🌸", "🐱", "🍕", "⚡", "🌙"]

    # pre-cond: components are not empty
    # post-cond: return on of components
    def random_component(self) -> str:
        return random.choice(self.components)