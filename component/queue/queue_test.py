import unittest
from component.queue.queue import ComponentQueue
from board.generator.generator import Generator
from component.set.component_set import ComponentSet

import random

class TestComponentQueue(unittest.TestCase):

    def test_add(self):
        queue = ComponentQueue()
        component_set = ComponentSet()

        cases = random.randint(1, 10)

        for _ in range(cases):
            component = component_set.random_component()
            queue.add(component)

            add_state = queue.get_add_state()

            self.assertEqual(add_state, 1, "Ошибка при добавлении элемента")

        queue_len = queue.len()
        add_state = queue.get_add_state()

        self.assertEqual(add_state, 1, "Ошибка при добавлении элементов")
        self.assertEqual(queue_len, cases, "Ошибка при добавлении элементов, неверный размер")

    def test_pop(self):
        queue = ComponentQueue()
        component_set = ComponentSet()

        cases = random.randint(1, 10)

        for _ in range(cases):
            component = component_set.random_component()
            queue.add(component)

            top = queue.pop()

            self.assertEqual(top.value, component.value, "Pop сработал некорректно, значения неверны")
            self.assertEqual(queue.len(), 0, "Pop сработал некорректно, элемент не удален")

    def test_pop_many(self):
        queue = ComponentQueue()
        component_set = ComponentSet()

        components = component_set.generate_sequence()

        for component in components:
            queue.add(component)


        result_tops = [queue.pop() for _ in range(queue.len())]

        self.assertEqual(result_tops, components, "Pop сработал некорректно, получаем не первый элемень")