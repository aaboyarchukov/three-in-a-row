import unittest
from component.set.component_set import ComponentSet
from component.null_component import NullComponent

import random

class TestComponentQueue(unittest.TestCase):

    def test_generate_component(self):
        component_set = ComponentSet()

        cases = random.randint(1, 10)
        null_component = NullComponent("")

        for _ in range(cases):
            random_component = component_set.random_component()

            self.assertNotEqual(random_component.is_component_null(), null_component.is_component_null(), "Ошибка при генерации компонента, компонент не должен быть пустым")
            self.assertNotEqual(random_component.get_value(), null_component.get_value(), "Ошибка при генерации компонента, значения должны быть не равны")

    def test_generate_sequence(self):
        component_set = ComponentSet()
        
        cases = random.randint(1, 10)
        null_components = [NullComponent("") for _ in range(cases)]

        sequence = component_set.generate_sequence(cases)

        self.assertNotEqual(null_components, sequence, "Ошибка при генерации последовательности, компоненты не должен быть пустым")