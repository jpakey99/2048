import unittest
from Game.board import Board
from Game.check_game import Checks


class BoardTest(unittest.TestCase):
    def test_point_total(self):
        CuT = Board()
        CuT.rows = [
            [2, 0, 0, 0],
            [0, 0, 0, 0],
            [0, 0, 0, 0],
            [0, 0, 0, 0]
        ]
        self.assertEqual(CuT.get_point_total(), 2, 'Addition is wrong')

        CuT.rows = [
            [2, 0, 0, 0],
            [0, 0, 0, 8],
            [0, 0, 2, 0],
            [4, 0, 0, 0]
        ]
        self.assertEqual(CuT.get_point_total(), 16, 'Addition is wrong')

    def test_new_cell(self):
        pass

    def test_is_game_over(self):
        pass

    def test_eq(self):
        CuT = Board()
        CuT.rows = [
            [2, 0, 0, 0],
            [0, 0, 0, 0],
            [0, 0, 0, 0],
            [0, 0, 0, 0]
        ]
        other = Board()
        other.rows = [
            [2, 0, 0, 0],
            [0, 0, 0, 0],
            [0, 0, 0, 0],
            [0, 0, 0, 0]
        ]
        self.assertEqual(CuT, other, 'Board are the same, should return True')

        CuT.rows = [
            [2, 0, 0, 0],
            [0, 0, 0, 0],
            [0, 0, 0, 0],
            [0, 0, 0, 0]
        ]

        other.rows = [
            [2, 0, 0, 0],
            [0, 0, 0, 0],
            [0, 0, 0, 0],
            [0, 0, 0, 2]
        ]
        self.assertNotEqual(CuT, other, 'The boards are not the same and should return False')

        self.assertNotEqual(CuT, 2, 'Compared object is not a board and thus not equal and should return False')

if __name__ == '__main__':
    unittest.main()