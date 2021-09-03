from Game.board import Board
from UserInterface.console import ConsoleUI
from Game.swipe import LeftSwipe, RightSwipe, UpSwipe, DownSwipe


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
                swipe = LeftSwipe(self.board)
            elif move == '1':
                swipe = RightSwipe(self.board)
            elif move == '2':
                swipe = UpSwipe(self.board)
            elif move == '3':
                swipe = DownSwipe(self.board)
            swipe.perform_swipe()


game = Game()
game.play_game()