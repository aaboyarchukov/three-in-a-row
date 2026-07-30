from player.player import Player
from board.board import Board
from game.game import Game

def main():
    player = Player()
    board = Board()
    game = Game(player, board)

    game.start_game()


if __file__ == "__main__":
    main()