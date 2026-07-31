import unittest
from board.generator.generator import Generator
from board.board import Board
from component.set.component_set import ComponentSet
import random
from cli.manager import CLI_Manager

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

    def test_move(self):
        cli_manager = CLI_Manager()
        generator = Generator(
            component_set=ComponentSet()
        )
        board = Board(generator)

        board.fill()

        cli_manager.show_board(board)

        board_matrix = board.get_matrix()

        amount = 10

        for _ in range(amount):
            indx = random.randint(1, 63)

            first_cell, second_cell = board_matrix.array[indx], board_matrix.array[indx-1]

            first_component_before = first_cell.get_component()
            second_component_before = second_cell.get_component()

            board.move(first_cell, second_cell)

            self.assertIs(board_matrix.array[indx], first_cell)
            self.assertIs(board_matrix.array[indx - 1], second_cell)

            # а вот содержимое (component) должно поменяться местами
            self.assertEqual(first_cell.get_component(), second_component_before, "Компонент не переехал в first_cell")
            self.assertEqual(second_cell.get_component(), first_component_before, "Компонент не переехал в second_cell")

            cli_manager.show_board(board)

    def test_remove(self):
        cli_manager = CLI_Manager()
        generator = Generator(
            component_set=ComponentSet()
        )
        board = Board(generator)

        board.fill()

        cli_manager.show_board(board)

        board_matrix = board.get_matrix()

        amount = 10

        for _ in range(amount):
            indx = random.randint(2, 63)
            sequence = [board_matrix.array[indx], board_matrix.array[indx-1], board_matrix.array[indx-2]]

            board_matrix.remove_sequence(sequence)

            cli_manager.show_board(board)

            for cell  in sequence:
                self.assertTrue(cell.get_delete_state(), f"Ячейка {cell.get_x()}, {cell.get_y()} не помечена на удаление")
                self.assertEqual(cell.get_component(), ComponentSet.delete_component, f"Компонент ячейки {cell.get_x()}, {cell.get_y()} не заменился на delete_component")
        