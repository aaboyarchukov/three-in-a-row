from any import Any
from player.player import Player
from board.board import Board
from statistic.statistics import Statistics
from cli.manager import CLI_Manager

class Game(Any):
    # constructor
    def __init__(self, player: Player, board: Board):
        self.statistics = Statistics()
        self.cli_manager = CLI_Manager()

        self.player = player
        self.board = board

        self.GAME_ENDING_STATE = False
    
    # commands
    # pre-cond: game is not ending yet
    # post-cond: game ending
    def end_game(self):
        # show statistics
        self.statistics.get_final_result()
    
    # pre-cond: 
    #   - game is not ending yet
    #   - dependecies are init
    # post-cond: game ending
    def start_game(self):
        while True:
            first_cell, second_cell = self.cli_manager.get_player_move()

            # valid player moves

            self.player.move(first_cell, second_cell)

            is_game_ending = self.get_game_ending_state() == True

            if is_game_ending:
                self.end_game()
            
    # requests
    def get_game_ending_state(self) -> bool:
        return self.GAME_ENDING_STATE