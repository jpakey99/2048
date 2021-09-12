from Game.board import Board


class Swipe:
    def __init__(self, board):
        self.board = board

    def perform_swipe(self):
        pass


class LeftSwipe(Swipe):
    def __init__(self, board):
        super().__init__(board)

    def move_cell(self, row_index, cell_index, combined=False):
        if cell_index - 1 <= -1 and combined:
            pass
        elif cell_index == 3:
            self.board.rows[row_index][cell_index- 1] = self.board.rows[row_index][cell_index]
            self.board.rows[row_index][cell_index] = 0
            self.move_cell(row_index, cell_index- 1, combined=True)
        elif combined and self.board.rows[row_index][cell_index- 1] == 0:
            self.board.rows[row_index][cell_index- 1] = self.board.rows[row_index][cell_index]
            self.board.rows[row_index][cell_index] = 0
            self.move_cell(row_index, cell_index- 1, combined=combined)
        elif combined and self.board.rows[row_index][cell_index- 1] != 0:
            pass
        else:
            current_piece, test_piece = self.board.rows[row_index][cell_index], self.board.rows[row_index][cell_index+ 1]
            if test_piece == current_piece and test_piece != 0 and not combined:
                self.board.rows[row_index][cell_index+ 1] = 0
                self.board.rows[row_index][cell_index] = current_piece * 2
                self.move_cell(row_index, cell_index, combined=True)
            elif test_piece == 0:
                self.board.rows[row_index][cell_index+ 1] = current_piece
                self.board.rows[row_index][cell_index] = 0
                self.move_cell(row_index, cell_index+ 1, combined=combined)
            else:
                # next cell down is non-zero but does not match current row
                pass

    def perform_swipe(self):
        for row in range(0, 4):
            for cell in range(0, len(self.board.rows)):
                self.move_cell(row, cell)



class RightSwipe(Swipe):
    def __init__(self, board):
        super().__init__(board)

    def move_cell(self, row_index, cell_index, combined=False):
        if cell_index + 1 >= 4 and combined:
            pass
        elif cell_index == 0:
            self.board.rows[row_index][cell_index+ 1] = self.board.rows[row_index][cell_index]
            self.board.rows[row_index][cell_index] = 0
            self.move_cell(row_index, cell_index+ 1, combined=True)
        elif combined and self.board.rows[row_index][cell_index+ 1] == 0:
            self.board.rows[row_index][cell_index+ 1] = self.board.rows[row_index][cell_index]
            self.board.rows[row_index][cell_index] = 0
            self.move_cell(row_index, cell_index+ 1, combined=combined)
        elif combined and self.board.rows[row_index][cell_index+ 1] != 0:
            pass
        else:
            current_piece, test_piece = self.board.rows[row_index][cell_index], self.board.rows[row_index][cell_index- 1]
            if test_piece == current_piece and test_piece != 0 and not combined:
                self.board.rows[row_index][cell_index- 1] = 0
                self.board.rows[row_index][cell_index] = current_piece * 2
                self.move_cell(row_index, cell_index, combined=True)
            elif test_piece == 0:
                self.board.rows[row_index][cell_index- 1] = current_piece
                self.board.rows[row_index][cell_index] = 0
                self.move_cell(row_index, cell_index- 1, combined=combined)
            else:
                # next cell down is non-zero but does not match current row
                pass

    def perform_swipe(self):
        for row in range(0, 4):
            for cell in range(len(self.board.rows) - 1, -1, -1):
                self.move_cell(row, cell)


class UpSwipe(Swipe):
    def __init__(self, board):
        super().__init__(board)

    def move_cell(self, row_index, cell_index, combined=False):
        if row_index-1 <= -1 and combined:
            pass
        elif row_index == 3:
            self.board.rows[row_index - 1][cell_index] = self.board.rows[row_index][cell_index]
            self.board.rows[row_index][cell_index] = 0
            self.move_cell(row_index - 1, cell_index, combined=True)
        elif combined and self.board.rows[row_index - 1][cell_index] == 0:
            self.board.rows[row_index - 1][cell_index] = self.board.rows[row_index][cell_index]
            self.board.rows[row_index][cell_index] = 0
            self.move_cell(row_index - 1, cell_index, combined=combined)
        elif combined and self.board.rows[row_index - 1][cell_index] != 0:
            pass
        else:
            current_piece, test_piece = self.board.rows[row_index][cell_index], self.board.rows[row_index + 1][cell_index]
            if test_piece == current_piece and test_piece != 0 and not combined:
                self.board.rows[row_index + 1][cell_index] = 0
                self.board.rows[row_index][cell_index] = current_piece * 2
                self.move_cell(row_index, cell_index, combined=True)
            elif test_piece == 0:
                self.board.rows[row_index + 1][cell_index] = current_piece
                self.board.rows[row_index][cell_index] = 0
                self.move_cell(row_index + 1, cell_index, combined=combined)
            else:
                # next cell down is non-zero but does not match current row
                pass

    def perform_swipe(self):
        for cell in range(0, 4):
            for row in range(0, len(self.board.rows)):
                self.move_cell(row, cell)


class DownSwipe(Swipe):
    def __init__(self, board):
        super().__init__(board)

    def move_cell(self, row_index, cell_index, combined=False):
        if row_index+1 >= 4 and combined:
            pass
        elif row_index == 0:
            self.board.rows[row_index + 1][cell_index] = self.board.rows[row_index][cell_index]
            self.board.rows[row_index][cell_index] = 0
            self.move_cell(row_index+1, cell_index, combined=True)
        elif combined and self.board.rows[row_index + 1][cell_index] == 0:
            self.board.rows[row_index + 1][cell_index] = self.board.rows[row_index][cell_index]
            self.board.rows[row_index][cell_index] = 0
            self.move_cell(row_index+1, cell_index, combined=combined)
        elif combined and self.board.rows[row_index + 1][cell_index] != 0:
            pass
        else:
            current_piece, test_piece = self.board.rows[row_index][cell_index], self.board.rows[row_index - 1][cell_index]
            if test_piece == current_piece and test_piece != 0 and not combined:
                self.board.rows[row_index - 1][cell_index] = 0
                self.board.rows[row_index][cell_index] = current_piece * 2
                self.move_cell(row_index, cell_index, combined=True)
            elif test_piece == 0:
                self.board.rows[row_index - 1][cell_index] = current_piece
                self.board.rows[row_index][cell_index] = 0
                self.move_cell(row_index-1, cell_index, combined=combined)
            else:
                # next cell down is non-zero but does not match current row
                pass

    def perform_swipe(self):
        for cell in range(0, 4):
            for row in range(len(self.board.rows)-1, -1, -1):
                self.move_cell(row, cell)
