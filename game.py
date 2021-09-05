from Game.board import Board
from UserInterface.console import ConsoleUI
from Game.swipe import LeftSwipe, RightSwipe, UpSwipe, DownSwipe



class Game:
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.board = Board()
        self.ui = ConsoleUI(self.board)

    def play_game(self):
        while not self.board.is_game_over():
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


g = Game()
g.play_game()