from Game.board import Board
from UserInterface.console import ConsoleUI


class Game:
    def __init__(self):
        self.board = Board()
        self.ui = ConsoleUI(self.board) # maybe a parameter in the future?

    def play_game(self):
        while self.board.is_game_over():
            self.board.new_cell()
            self.ui.display()
            move = self.ui.make_move()
            if move == '0':
                pass
            elif move == '1':
                pass
            elif move == '2':
                pass
            elif move == '3':
                pass


game = Game()
game.play_game()