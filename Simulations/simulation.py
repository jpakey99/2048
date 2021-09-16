from Game.board import Board
from Game.swipe import *
import random
from Game.check_game import CheckRightSwipe, CheckLeftSwipe, CheckDownSwipe, CheckUpSwipe


class RandomSimulation:
    def __init__(self, board):
        self.board: Board = board

    def make_move(self):
        swipe = None
        swipe_rand = random.randint(0,4)
        if swipe_rand == 0:
            print(CheckLeftSwipe(self.board).check_situation(), 'left')
            if CheckLeftSwipe(self.board).check_situation():
                swipe = LeftSwipe(self.board)
        elif swipe_rand == 1:
            print(CheckRightSwipe(self.board).check_situation(), 'right')
            if CheckRightSwipe(self.board).check_situation():
                swipe = RightSwipe(self.board)
        elif swipe_rand == 2:
            print(CheckUpSwipe(self.board).check_situation(), 'up')
            if CheckUpSwipe(self.board).check_situation():
                swipe = UpSwipe(self.board)
        elif swipe_rand == 3:
            print(CheckDownSwipe(self.board).check_situation(), 'down')
            if CheckDownSwipe(self.board).check_situation():
                swipe = DownSwipe(self.board)

        if swipe is not None:
            swipe.perform_swipe()
            return True
        return False
