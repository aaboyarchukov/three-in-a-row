import unittest
from board.generator.generator import Generator
from component.set.component_set import ComponentSet
from board.board import Board
from cli.manager import CLI_Manager
import random

class TestCLIManager(unittest.TestCase):

    def test_show_board(self):
        cli_manager = CLI_Manager()
        generator = Generator(
            component_set=ComponentSet()
        )
        board = Board(generator)

        board.fill()

        cli_manager.show_board(board)

        