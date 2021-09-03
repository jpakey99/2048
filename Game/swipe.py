from Game.board import Board


class Swipe:
    def __init__(self, board):
        self.board = board

    def perform_swipe(self):
        pass


class LeftSwipe(Swipe):
    def __init__(self, board):
        super().__init__(board)

    def move_cell(self, row_index, cell_index):
        if cell_index == 0:
            pass
        else:
            if self.board.rows[row_index][cell_index-1] == self.board.rows[row_index][cell_index]:
                self.board.rows[row_index][cell_index - 1] = self.board.rows[row_index][cell_index-1] * 2
                self.board.rows[row_index][cell_index] = 0
            elif self.board.rows[row_index][cell_index-1] == 0:
                self.board.rows[row_index][cell_index - 1] = self.board.rows[row_index][cell_index]
                self.board.rows[row_index][cell_index] = 0
                self.move_cell(row_index, cell_index-1)

    def perform_swipe(self):
        row_index, cell_index = 0, 0
        for row in self.board.rows:
            for cell in row:
                self.move_cell(row_index, cell_index)
                cell_index += 1
            row_index += 1
            cell_index = 0



class RightSwipe(Swipe):
    def __init__(self, board):
        super().__init__(board)

    def move_cell(self, row_index, cell_index):
        if cell_index == 3:
            pass
        else:
            if self.board.rows[row_index][cell_index + 1] == self.board.rows[row_index][cell_index]:
                self.board.rows[row_index][cell_index + 1] = self.board.rows[row_index][cell_index + 1] * 2
                self.board.rows[row_index][cell_index] = 0
            elif self.board.rows[row_index][cell_index + 1] == 0:
                self.board.rows[row_index][cell_index + 1] = self.board.rows[row_index][cell_index]
                self.board.rows[row_index][cell_index] = 0
                self.move_cell(row_index, cell_index + 1)

    def perform_swipe(self):
        row_index, cell_index = 0, 0
        for row in self.board.rows:
            for cell in row:
                self.move_cell(row_index, cell_index)
                cell_index += 1
            row_index += 1
            cell_index = 0


class UpSwipe(Swipe):
    def __init__(self, board):
        super().__init__(board)

    def move_cell(self, row_index, cell_index):
        if row_index == 0:
            pass
        else:
            if self.board.rows[row_index-1][cell_index] == self.board.rows[row_index][cell_index]:
                self.board.rows[row_index-1][cell_index] = self.board.rows[row_index-1][cell_index] * 2
                self.board.rows[row_index][cell_index] = 0
            elif self.board.rows[row_index -1][cell_index] == 0:
                self.board.rows[row_index -1][cell_index] = self.board.rows[row_index][cell_index]
                self.board.rows[row_index][cell_index] = 0
                self.move_cell(row_index -1 , cell_index)

    def perform_swipe(self):
        row_index, cell_index = 0, 0
        for row in self.board.rows:
            for cell in row:
                self.move_cell(row_index, cell_index)
                cell_index += 1
            row_index += 1
            cell_index = 0


class DownSwipe(Swipe):
    def __init__(self, board):
        super().__init__(board)

    def move_cell(self, row_index, cell_index):
        if row_index == 3:
            pass
        else:
            if self.board.rows[row_index + 1][cell_index] == self.board.rows[row_index][cell_index]:
                self.board.rows[row_index + 1][cell_index] = self.board.rows[row_index + 1][cell_index] * 2
                self.board.rows[row_index][cell_index] = 0
            elif self.board.rows[row_index + 1][cell_index] == 0:
                self.board.rows[row_index + 1][cell_index] = self.board.rows[row_index][cell_index]
                self.board.rows[row_index][cell_index] = 0
                self.move_cell(row_index + 1, cell_index)

    def perform_swipe(self):
        row_index, cell_index = 0, 0
        for row in self.board.rows:
            for cell in row:
                self.move_cell(row_index, cell_index)
                cell_index += 1
            row_index += 1
            cell_index = 0