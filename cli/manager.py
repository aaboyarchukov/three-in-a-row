from any import Any
from board.board import Board
import os
from board.matrix import Matrix
from board.cell import Cell

class CLI_Manager(Any):
    def __init__(self):
        pass

    # commands
    def show_board(self, board: Board):
        self.__clear_screen()
        matrix = board.get_matrix()
        print(matrix)

    def __clear_screen(self):
        os.system('cls' if os.name == 'nt' else 'clear')

    # requests
    def get_player_move(self, board: Board) -> list[Cell]:
        matrix = board.get_matrix()
        size = matrix.get_size()

        first_cell = self.__request_cell(matrix, size, "Введите первую ячейку (например A6): ")
        second_cell = self.__request_cell(matrix, size, "Введите вторую ячейку (например B6): ")

        return [first_cell, second_cell]

    def __request_cell(self, matrix: Matrix, size: int, prompt: str) -> Cell:
        while True:
            raw = input(prompt).strip()
            coords = self.parsing_coordinates(raw, size)

            if not coords:
                print("Некорректный ввод, попробуйте снова.")
                continue

            return matrix.get_cell(coords[0], coords[1])

    # pre-cond: cell is str with two elements
    # post-cond: returns [x, y] or [] if invalid
    def parsing_coordinates(self, cell: str, size: int) -> list[int]:
        if len(cell) != 2:
            return []

        col_symbol, row_symbol = cell[0].upper(), cell[1]

        if col_symbol not in Matrix.COLS[:size]:
            return []

        if not row_symbol.isdigit():
            return []

        x = Matrix.COLS.index(col_symbol)
        y = int(row_symbol) - 1

        if y < 0 or y >= size:
            return []

        return [x, y]