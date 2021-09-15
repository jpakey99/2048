import unittest
from Game.board import Board
from Game.check_game import *


class CheckEmptyCellTest(unittest.TestCase):
    def test_empty_board(self):
        board = Board()
        board.rows = [
            [0, 0, 0, 0],
            [0, 0, 0, 0],
            [0, 0, 0, 0],
            [0, 0, 0, 0]
        ]
        CuT = CheckEmptyCells(board)
        self.assertTrue(CuT.check_situation(), 'There is at least 1 empty cell, should return True to continue game')

    def test_full_board(self):
        board = Board()
        board.rows = [
            [2, 2, 2, 2],
            [2, 2, 2, 2],
            [2, 2, 2, 2],
            [2, 2, 2, 2]
        ]
        CuT = CheckEmptyCells(board)
        self.assertFalse(CuT.check_situation(), 'There are no empty cells, should return False and have game end')

    def test_singular_empty_cell_at_end(self):
        board = Board()
        board.rows = [
            [2, 2, 2, 2],
            [2, 2, 2, 2],
            [2, 2, 2, 2],
            [2, 2, 2, 0]
        ]
        CuT = CheckEmptyCells(board)
        self.assertTrue(CuT.check_situation(), 'There is at least 1 empty cell, should return True to continue game')


class CheckSwipeHorizontalTest(unittest.TestCase):
    def test_if_horizontal_swipe(self):
        board = Board()
        board.rows = [
            [2, 2, 2, 2],
            [4, 4, 4, 4],
            [2, 2, 2, 2],
            [4, 4, 4, 4]
        ]
        CuT = CheckSwipeHorizontal(board)
        self.assertTrue(CuT.check_situation(), 'Horizontal Swipe may occur, game should continue')

    def test_horizontal_swipe_available_zeros(self):
        board = Board()
        board.rows = [
            [2, 4, 2, 4],
            [4, 2, 4, 2],
            [2, 0, 0, 4],
            [4, 2, 4, 2]
        ]
        CuT = CheckSwipeHorizontal(board)
        self.assertTrue(CuT.check_situation(), 'Horizontal Swipe cannot occur, game should not continue')

    def test_no_horizontal_swipe_available(self):
        board = Board()
        board.rows = [
            [2, 4, 2, 4],
            [4, 2, 4, 2],
            [2, 4, 8, 4],
            [4, 2, 4, 2]
        ]
        CuT = CheckSwipeHorizontal(board)
        self.assertFalse(CuT.check_situation(), 'Horizontal Swipe cannot occur, game should not continue')

    def test_not_vertical_swipe(self):
        board = Board()
        board.rows = [
            [2, 4, 2, 4],
            [4, 2, 4, 2],
            [2, 0, 4, 8],
            [4, 2, 4, 2]
        ]
        CuT = CheckSwipeHorizontal(board)
        self.assertFalse(CuT.check_situation(), 'Horizontal Swipe cannot occur, game should not continue')


class CheckSwipeVerticalTest(unittest.TestCase):
    def test_if_vertical_swipe(self):
        board = Board()
        board.rows = [
            [2, 4, 2, 4],
            [2, 4, 2, 4],
            [2, 4, 2, 4],
            [2, 4, 2, 4]
        ]
        CuT = CheckSwipeVertical(board)
        self.assertTrue(CuT.check_situation(), 'Horizontal Swipe may occur, game should continue')

    def test_vertical_swipe_available_zeros(self):
        board = Board()
        board.rows = [
            [2, 4, 2, 4],
            [4, 0, 4, 0],
            [2, 0, 2, 4],
            [8, 4, 8, 2]
        ]
        CuT = CheckSwipeVertical(board)
        self.assertTrue(CuT.check_situation(), 'Horizontal Swipe cannot occur, game should not continue')

    def test_no_vertical_swipe_available(self):
        board = Board()
        board.rows = [
            [2, 4, 2, 4],
            [4, 2, 4, 2],
            [2, 8, 2, 4],
            [8, 4, 8, 2]
        ]
        CuT = CheckSwipeVertical(board)
        self.assertFalse(CuT.check_situation(), 'Horizontal Swipe cannot occur, game should not continue')

    def test_no_horizontal_swipe(self):
        board = Board()
        board.rows = [
            [2, 4, 2, 4],
            [4, 0, 4, 0],
            [2, 2, 2, 4],
            [8, 4, 8, 2]
        ]
        CuT = CheckSwipeVertical(board)
        self.assertFalse(CuT.check_situation(), 'Horizontal Swipe cannot occur, game should not continue')


class ChecksTest(unittest.TestCase):
    def test_empty_cells(self):
        board = Board()
        board.rows = [
            [2, 4, 2, 4],
            [4, 0, 4, 0],
            [2, 2, 2, 4],
            [8, 4, 8, 2]
        ]
        CuT = Checks(board)
        self.assertTrue(CuT.check_situation(), 'Empty Cell, game should continue')

    def test_vertical_swipe(self):
        board = Board()
        board.rows = [
            [2, 4, 2, 4],
            [4, 2, 4, 8],
            [8, 2, 8, 4],
            [8, 4, 8, 2]
        ]
        CuT = Checks(board)
        self.assertTrue(CuT.check_situation(), 'Vertical Swipe, game should continue')

    def test_horizontal_swipe(self):
        board = Board()
        board.rows = [
            [2, 4, 2, 4],
            [4, 8, 4, 8],
            [2, 2, 8, 4],
            [8, 4, 4, 2]
        ]
        CuT = Checks(board)
        self.assertTrue(CuT.check_situation(), 'Horizontal Swipe, game should continue')

    def test_no_empty_cells_vertical_swipe(self):
        board = Board()
        board.rows = [
            [2, 4, 2, 4],
            [4, 2, 4, 2],
            [8, 2, 8, 4],
            [2, 4, 2, 8]
        ]
        CuT = Checks(board)
        self.assertTrue(CuT.check_situation(), 'Vertical Swipe, game should continue')

    def test_no_empty_cells_horizontal_swipe(self):
        board = Board()
        board.rows = [
            [2, 4, 2, 4],
            [4, 8, 4, 2],
            [8, 2, 2, 4],
            [2, 4, 8, 2]
        ]
        CuT = Checks(board)
        self.assertTrue(CuT.check_situation(), 'Horizontal Swipe, game should continue')

    def test_empty_cells_no_swipes(self):
        board = Board()
        board.rows = [
            [0, 4, 2, 4],
            [4, 2, 4, 2],
            [8, 4, 8, 4],
            [2, 8, 2, 8]
        ]
        CuT = Checks(board)
        self.assertTrue(CuT.check_situation(), 'Empty Cells, game should continue')

    def test_no_empty_cells_no_swipes(self):
        board = Board()
        board.rows = [
            [2, 4, 2, 4],
            [4, 2, 4, 2],
            [8, 4, 8, 4],
            [2, 8, 2, 8]
        ]
        CuT = Checks(board)
        self.assertFalse(CuT.check_situation(), 'No Empty Cells or swipes, game should not continue')


class CheckLeftSwipeTest(unittest.TestCase):
    def test_left_swipe_standard(self):
        board = Board()
        board.rows = [
            [0, 0, 0, 0],
            [0, 0, 0, 0],
            [0, 0, 8, 0],
            [0, 0, 0, 0]
        ]
        CuT = CheckLeftSwipe(board)
        self.assertTrue(CuT.check_situation(), 'No Empty Cells or swipes, game should not continue')

    def test_no_left_swipe_single(self):
        board = Board()
        board.rows = [
            [0, 0, 0, 0],
            [0, 0, 0, 0],
            [2, 0, 0, 0],
            [0, 0, 0, 0]
        ]
        CuT = CheckLeftSwipe(board)
        self.assertFalse(CuT.check_situation(), 'No Empty Cells or swipes, game should not continue')

    def test_combine_left(self):
        board = Board()
        board.rows = [
            [0, 0, 0, 0],
            [0, 0, 0, 0],
            [2, 2, 8, 0],
            [0, 0, 0, 0]
        ]
        CuT = CheckLeftSwipe(board)
        self.assertTrue(CuT.check_situation(), 'No Empty Cells or swipes, game should not continue')

    def test_no_combine_left(self):
        board = Board()
        board.rows = [
            [0, 0, 0, 0],
            [0, 0, 0, 0],
            [2, 4, 8, 0],
            [0, 0, 0, 0]
        ]
        CuT = CheckLeftSwipe(board)
        self.assertFalse(CuT.check_situation(), 'No Empty Cells or swipes, game should not continue')

    def test_zero_in_middle(self):
        board = Board()
        board.rows = [
            [0, 0, 0, 0],
            [0, 0, 0, 0],
            [2, 0, 8, 4],
            [0, 0, 0, 0]
        ]
        CuT = CheckLeftSwipe(board)
        self.assertTrue(CuT.check_situation(), 'No Empty Cells or swipes, game should not continue')


class CheckRightSwipeTest(unittest.TestCase):
    def test_right_swipe_standard(self):
        board = Board()
        board.rows = [
            [0, 0, 0, 0],
            [0, 0, 0, 0],
            [0, 0, 8, 0],
            [0, 0, 0, 0]
        ]
        CuT = CheckRightSwipe(board)
        self.assertTrue(CuT.check_situation(), 'No Empty Cells or swipes, game should not continue')

    def test_no_right_swipe_single(self):
        board = Board()
        board.rows = [
            [0, 0, 0, 0],
            [0, 0, 0, 0],
            [0, 0, 0, 2],
            [0, 0, 0, 0]
        ]
        CuT = CheckRightSwipe(board)
        self.assertFalse(CuT.check_situation(), 'No Empty Cells or swipes, game should not continue')

    def test_combine_right(self):
        board = Board()
        board.rows = [
            [0, 0, 0, 0],
            [0, 0, 0, 0],
            [0, 2, 8, 8],
            [0, 0, 0, 0]
        ]
        CuT = CheckRightSwipe(board)
        self.assertTrue(CuT.check_situation(), 'No Empty Cells or swipes, game should not continue')

    def test_no_combine_right(self):
        board = Board()
        board.rows = [
            [0, 0, 0, 0],
            [0, 0, 0, 0],
            [2, 4, 8, 2],
            [0, 0, 0, 0]
        ]
        CuT = CheckRightSwipe(board)
        self.assertFalse(CuT.check_situation(), 'No Empty Cells or swipes, game should not continue')

    def test_zero_in_middle(self):
        board = Board()
        board.rows = [
            [0, 0, 0, 0],
            [0, 0, 0, 0],
            [2, 0, 8, 4],
            [0, 0, 0, 0]
        ]
        CuT = CheckRightSwipe(board)
        self.assertTrue(CuT.check_situation(), 'No Empty Cells or swipes, game should not continue')


class CheckUpSwipeTest(unittest.TestCase):
    def test_up_swipe_standard(self):
        board = Board()
        board.rows = [
            [0, 0, 0, 0],
            [0, 0, 0, 0],
            [0, 0, 8, 0],
            [0, 0, 0, 0]
        ]
        CuT = CheckUpSwipe(board)
        self.assertTrue(CuT.check_situation(), 'No Empty Cells or swipes, game should not continue')

    def test_no_up_swipe_single(self):
        board = Board()
        board.rows = [
            [0, 0, 0, 2],
            [0, 0, 0, 0],
            [0, 0, 0, 0],
            [0, 0, 0, 0]
        ]
        CuT = CheckUpSwipe(board)
        self.assertFalse(CuT.check_situation(), 'No Empty Cells or swipes, game should not continue')

    def test_no_combine_up(self):
        board = Board()
        board.rows = [
            [0, 0, 4, 0],
            [0, 0, 2, 0],
            [0, 0, 8, 0],
            [0, 0, 2, 0]
        ]
        CuT = CheckUpSwipe(board)
        self.assertFalse(CuT.check_situation(), 'No Empty Cells or swipes, game should not continue')

    def test_combine_up(self):
        board = Board()
        board.rows = [
            [0, 0, 8, 0],
            [0, 0, 8, 0],
            [0, 0, 4, 0],
            [0, 0, 0, 0]
        ]
        CuT = CheckUpSwipe(board)
        self.assertTrue(CuT.check_situation(), 'No Empty Cells or swipes, game should not continue')

    def test_zero_in_middle(self):
        board = Board()
        board.rows = [
            [0, 0, 4, 0],
            [0, 0, 2, 0],
            [0, 0, 0, 0],
            [0, 0, 4, 0]
        ]
        CuT = CheckRightSwipe(board)
        self.assertTrue(CuT.check_situation(), 'No Empty Cells or swipes, game should not continue')


if __name__ == '__main__':
    unittest.main()