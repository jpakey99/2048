import unittest
from Game.board import Board
from Game.swipe import LeftSwipe, RightSwipe, UpSwipe, DownSwipe


class LeftSwipeTest(unittest.TestCase):
    def test_one_cell_moves_left(self):
        start_board = Board()
        start_board.rows = [
            [0, 0, 0, 0],
            [0, 0, 0, 0],
            [0, 0, 2, 0],
            [0, 0, 0, 0]
        ]
        end_board = Board()
        end_board.rows = [
            [0, 0, 0, 0],
            [0, 0, 0, 0],
            [2, 0, 0, 0],
            [0, 0, 0, 0]
        ]
        CuT = LeftSwipe(start_board)
        CuT.perform_swipe()
        self.assertEqual(CuT.board, end_board, 'Swipe was not performed correctly')

    def test_already_on_far_left(self):
        start_board = Board()
        start_board.rows = [
            [0, 0, 0, 0],
            [0, 0, 0, 0],
            [2, 0, 0, 0],
            [0, 0, 0, 0]
        ]
        end_board = Board()
        end_board.rows = [
            [0, 0, 0, 0],
            [0, 0, 0, 0],
            [2, 0, 0, 0],
            [0, 0, 0, 0]
        ]
        CuT = LeftSwipe(start_board)
        CuT.perform_swipe()
        self.assertEqual(CuT.board, end_board, 'Swipe was not performed correctly')

    def test_standard_combine(self):
        start_board = Board()
        start_board.rows = [
            [0, 0, 0, 0],
            [0, 0, 0, 0],
            [2, 2, 0, 0],
            [0, 0, 0, 0]
        ]
        end_board = Board()
        end_board.rows = [
            [0, 0, 0, 0],
            [0, 0, 0, 0],
            [4, 0, 0, 0],
            [0, 0, 0, 0]
        ]
        CuT = LeftSwipe(start_board)
        CuT.perform_swipe()
        self.assertEqual(CuT.board, end_board, 'Swipe was not performed correctly')

    def test_combine_and_push_over(self):
        start_board = Board()
        start_board.rows = [
            [0, 0, 0, 0],
            [0, 0, 0, 0],
            [0, 2, 2, 0],
            [0, 0, 0, 0]
        ]
        end_board = Board()
        end_board.rows = [
            [0, 0, 0, 0],
            [0, 0, 0, 0],
            [4, 0, 0, 0],
            [0, 0, 0, 0]
        ]
        CuT = LeftSwipe(start_board)
        CuT.perform_swipe()
        self.assertEqual(CuT.board, end_board, 'Swipe was not performed correctly')

    def test_space_between_combines(self):
        start_board = Board()
        start_board.rows = [
            [0, 0, 0, 0],
            [0, 0, 0, 0],
            [2, 0, 2, 0],
            [0, 0, 0, 0]
        ]
        end_board = Board()
        end_board.rows = [
            [0, 0, 0, 0],
            [0, 0, 0, 0],
            [4, 0, 0, 0],
            [0, 0, 0, 0]
        ]
        CuT = LeftSwipe(start_board)
        CuT.perform_swipe()
        self.assertEqual(CuT.board, end_board, 'Swipe was not performed correctly')

    def test_cell_multi_combines(self):
        start_board = Board()
        start_board.rows = [
            [0, 0, 0, 0],
            [0, 0, 0, 0],
            [2, 2, 4, 0],
            [0, 0, 0, 0]
        ]
        end_board = Board()
        end_board.rows = [
            [0, 0, 0, 0],
            [0, 0, 0, 0],
            [4, 4, 0, 0],
            [0, 0, 0, 0]
        ]
        CuT = LeftSwipe(start_board)
        CuT.perform_swipe()
        self.assertEqual(CuT.board, end_board, 'Swipe was not performed correctly')

    def test_mulitple_cells_combine(self):
        start_board = Board()
        start_board.rows = [
            [0, 2, 2, 0],
            [0, 0, 0, 0],
            [2, 2, 4, 4],
            [0, 0, 0, 0]
        ]
        end_board = Board()
        end_board.rows = [
            [4, 0, 0, 0],
            [0, 0, 0, 0],
            [4, 8, 0, 0],
            [0, 0, 0, 0]
        ]
        CuT = LeftSwipe(start_board)
        CuT.perform_swipe()
        start_board.print_board()
        self.assertEqual(CuT.board, end_board, 'Swipe was not performed correctly')


if __name__ == '__main__':
    unittest.main()