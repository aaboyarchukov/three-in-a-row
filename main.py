from player.player import Player
from board.board import Board
from game.game import Game
from board.generator.generator import Generator
from component.set.component_set import ComponentSet

def main():
    points_to_win = 15

    generator = Generator(
        component_set=ComponentSet()
    )
    board = Board(generator)

    player = Player(board)

    game = Game(player, points_to_win)

    game.start_game()


if __file__ == "__main__":
    main()