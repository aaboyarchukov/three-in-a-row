from any import Any

class CLI_Manager(Any):
    def __init__(self):
        pass

    # commands
    def show_board(self):
        pass

    # requests
    def get_player_move(self) -> list:
        pass

    # pre-cond: cell is str with two elements
    def parsing_coordinates(self, cell: str) -> list[int]:
        if len(cell) != 2:
            return []

        first_symbol, second_symbol = cell[0], cell[1]

        x = chr('H') - chr(first_symbol)
        y = chr(second_symbol)
