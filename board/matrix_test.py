import unittest
from board.generator.generator import Generator
from component.component import ComponentSet
import random

class TestMatrix(unittest.TestCase):

    def test_fill_all(self):
        component_set = ComponentSet()
        amount_tests = 2

        for i in range(1, amount_tests):
            size = i * random.randint(i, amount_tests+i)

            generator = Generator(component_set, size)
            matrix = generator.generate()

            
            self.assertNotEqual(len(matrix), 0, "Сгенирирована пустая матрица")
            self.assertEqual(len(matrix), size**2, "Длина матрицы некорректна")

            print(matrix)