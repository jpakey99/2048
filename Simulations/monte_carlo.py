from Game.board import Board
from Game.swipe import *
import random
from Game.check_game import *

import numpy


class MonteCarlo:
    def __init__(self, board):
        self.board: Board = board
        self.search_length = 40

    def find_move(self):
        first_move = [LeftSwipe, RightSwipe, UpSwipe, DownSwipe]
        moves = [self.left_move, self.right_move, self.up_move, self.down_move]
        valid_moves = [CheckLeftSwipe, CheckRightSwipe, CheckUpSwipe, CheckDownSwipe]
        scores = numpy.zeros(4)

        for first_index in range(4):
            first_move_class = first_move[first_index]
            board_copy = self.board.__copy__()
            checker = valid_moves[first_index]
            if checker(board_copy).check_situation():
                move = first_move_class(board_copy)
                score_before_first_move = board_copy.get_point_total()
                move.perform_swipe()
                board_after_move:Board = move.board.__copy__()
                score_after_move = move.score

                scores[first_index] = score_after_move
                if Checks(board_after_move).check_situation():
                    board_after_move.new_cell()

                    for i in range(self.search_length):
                        search_board:Board = board_after_move.__copy__()
                        for j in range(self.search_length):
                            if Checks(search_board).check_situation():
                                s = self.random_move(search_board)
                                scores[first_index] += s
                                if CheckEmptyCells(search_board).check_situation():
                                    search_board.new_cell()
            else:
                scores[first_index] = 0

        best_move_index = numpy.argmax(scores)
        best_move = first_move[best_move_index]
        return best_move

    def left_move(self, board:Board):
        if CheckLeftSwipe(board).check_situation():
            swipe = LeftSwipe(board)
            swipe.perform_swipe()
            return swipe.score
        return 0

    def right_move(self, board:Board):
        if CheckRightSwipe(board).check_situation():
            swipe = RightSwipe(board)
            swipe.perform_swipe()
            return swipe.score
        return 0

    def up_move(self, board:Board):
        if CheckUpSwipe(board).check_situation():
            swipe = UpSwipe(board)
            swipe.perform_swipe()
            return swipe.score
        return 0

    def down_move(self, board:Board):
        if CheckDownSwipe(board).check_situation():
            swipe = DownSwipe(board)
            swipe.perform_swipe()
            return swipe.score
        return 0


    def random_move(self, board):
        swipe = None
        while swipe is None:
            swipe_rand = random.randint(0, 4)
            if swipe_rand == 0:
                if CheckLeftSwipe(board).check_situation():
                    swipe = LeftSwipe(board)
            elif swipe_rand == 1:
                if CheckRightSwipe(board).check_situation():
                    swipe = RightSwipe(board)
            elif swipe_rand == 2:
                if CheckUpSwipe(board).check_situation():
                    swipe = UpSwipe(board)
            elif swipe_rand == 3:
                if CheckDownSwipe(board).check_situation():
                    swipe = DownSwipe(board)
        swipe.perform_swipe()
        return swipe.score

    def make_move(self):
        move = self.find_move()
        swipe = move(self.board)

        swipe.perform_swipe()
        return True
