from any import Any
import random
from component.component import Component

class ComponentSet(Any):

    def __init__(self):
        pass

    # льготный класс содержит набор из доступных компонентов
    # чем меньше набор, тем чаще будут попадаться повторы
    components = ["😀", "🎉", "🚀", "🌸", "🐱", "🍕", "⚡", "🌙"]
    delete_component = "⛔"

    # pre-cond: components are not empty
    # post-cond: return on of components
    def random_component(self) -> Component:
        value = random.choice(self.components)

        return Component(value)

    # request

    # генерирует последовательность из компонентов
    # pre-cond: component set is set
    # post-cond: generate sequence of component with certain size
    def generate_sequence(self, size: int = 8) -> list[Component]:
        sequence: list[Component] = []

        for _ in range(size):
            value = self.random_component()
            sequence.append(Component(value))

        return  sequence