from Game.board import Board


class Swipe:
    def __init__(self, board):
        self.board = board

    def perform_swipe(self):
        # algorithm
        # start on extreme side of swipe (Down swipe: lowest edge)
        # move cell 1 increment at a time to far opposite extreme till it contacts a non 0 cell
        # if cell is the same value, combine them.  Otherwise, go on to next step
        # Move back towards extreme side till non-zero cell is reached, then exit
        pass


class LeftSwipe(Swipe):
    def __init__(self, board):
        super().__init__(board)

    def move_cell(self, row_index, cell_index, go_to_extreme=False):
        # self.board.print_board()
        # print(self.board.rows[row_index][cell_index])
        # print(row_index)
        if self.board.rows[row_index][cell_index] == 0:
            # print('0')
            pass
        elif go_to_extreme and cell_index == 0:
            # print('ends going to extreme')
            pass
        elif not go_to_extreme and cell_index > 2:
            # print('ran into nothing')
            self.move_cell(row_index, cell_index, True)
        elif not go_to_extreme:
            # print('finding something to run into')
            if self.board.rows[row_index][cell_index+ 1] == 0:
                # print('nothing here')
                self.board.rows[row_index][cell_index+ 1] = self.board.rows[row_index][cell_index]
                self.board.rows[row_index][cell_index] = 0
                self.move_cell(row_index, cell_index+ 1, go_to_extreme)
            elif self.board.rows[row_index][cell_index+ 1] == self.board.rows[row_index][cell_index]:
                self.board.rows[row_index][cell_index] = self.board.rows[row_index][cell_index] * 2
                self.board.rows[row_index][cell_index+ 1] = 0
                self.move_cell(row_index, cell_index, True)
            else:
                # print('some random number, heading back now')
                self.move_cell(row_index, cell_index, True)
        elif go_to_extreme:
            if self.board.rows[row_index][cell_index- 1] == 0:
                self.board.rows[row_index][cell_index- 1] = self.board.rows[row_index][cell_index]
                self.board.rows[row_index][cell_index] = 0
                # self.board.print_board()
                self.move_cell(row_index, cell_index- 1, True)
            else:
                pass

    def perform_swipe(self):
        for row in range(0, 4):
            for cell in range(0, len(self.board.rows)):
                self.move_cell(row, cell)



class RightSwipe(Swipe):
    def __init__(self, board):
        super().__init__(board)

    def move_cell(self, row_index, cell_index, go_to_extreme=False):
        # self.board.print_board()
        # print(self.board.rows[row_index][cell_index])
        # print(row_index)
        if self.board.rows[row_index][cell_index] == 0:
            # print('0')
            pass
        elif go_to_extreme and cell_index == 3:
            # print('ends going to extreme')
            pass
        elif not go_to_extreme and cell_index < 1:
            # print('ran into nothing')
            self.move_cell(row_index, cell_index, True)
        elif not go_to_extreme:
            # print('finding something to run into')
            if self.board.rows[row_index][cell_index - 1] == 0:
                # print('nothing here')
                self.board.rows[row_index][cell_index - 1] = self.board.rows[row_index][cell_index]
                self.board.rows[row_index][cell_index] = 0
                self.move_cell(row_index, cell_index - 1, go_to_extreme)
            elif self.board.rows[row_index][cell_index - 1] == self.board.rows[row_index][cell_index]:
                self.board.rows[row_index][cell_index] = self.board.rows[row_index][cell_index] * 2
                self.board.rows[row_index][cell_index - 1] = 0
                self.move_cell(row_index, cell_index, True)
            else:
                # print('some random number, heading back now')
                self.move_cell(row_index, cell_index, True)
        elif go_to_extreme:
            if self.board.rows[row_index][cell_index + 1] == 0:
                self.board.rows[row_index][cell_index + 1] = self.board.rows[row_index][cell_index]
                self.board.rows[row_index][cell_index] = 0
                # self.board.print_board()
                self.move_cell(row_index, cell_index + 1, True)
            else:
                pass

    def perform_swipe(self):
        for row in range(0, 4):
            for cell in range(len(self.board.rows) - 1, -1, -1):
                self.move_cell(row, cell)


class UpSwipe(Swipe):
    def __init__(self, board):
        super().__init__(board)

    def move_cell(self, row_index, cell_index, go_to_extreme=False):
        # self.board.print_board()
        # print(self.board.rows[row_index][cell_index])
        # print(row_index)
        if self.board.rows[row_index][cell_index] == 0:
            # print('0')
            pass
        elif go_to_extreme and row_index == 0:
            # print('ends going to extreme')
            pass
        elif not go_to_extreme and row_index > 2:
            # print('ran into nothing')
            self.move_cell(row_index, cell_index, True)
        elif not go_to_extreme:
            # print('finding something to run into')
            if self.board.rows[row_index + 1][cell_index] == 0:
                # print('nothing here')
                self.board.rows[row_index + 1][cell_index] = self.board.rows[row_index][cell_index]
                self.board.rows[row_index][cell_index] = 0
                self.move_cell(row_index + 1, cell_index, go_to_extreme)
            elif self.board.rows[row_index + 1][cell_index] == self.board.rows[row_index][cell_index]:
                self.board.rows[row_index][cell_index] = self.board.rows[row_index][cell_index] * 2
                self.board.rows[row_index + 1][cell_index] = 0
                self.move_cell(row_index, cell_index, True)
            else:
                # print('some random number, heading back now')
                self.move_cell(row_index, cell_index, True)
        elif go_to_extreme:
            if self.board.rows[row_index - 1][cell_index] == 0:
                self.board.rows[row_index - 1][cell_index] = self.board.rows[row_index][cell_index]
                self.board.rows[row_index][cell_index] = 0
                # self.board.print_board()
                self.move_cell(row_index - 1, cell_index, True)
            else:
                pass

    def perform_swipe(self):
        for cell in range(0, 4):
            for row in range(0, len(self.board.rows)):
                self.move_cell(row, cell)


class DownSwipe(Swipe):
    def __init__(self, board):
        super().__init__(board)

    def move_cell(self, row_index, cell_index, go_to_extreme=False):
        # self.board.print_board()
        # print(self.board.rows[row_index][cell_index])
        if self.board.rows[row_index][cell_index] == 0:
            # print('0')
            pass
        elif go_to_extreme and row_index == 3:
            # print('ends going to extreme')
            pass
        elif not go_to_extreme and row_index < 1:
            # print('ran into nothing')
            self.move_cell(row_index, cell_index, True)
        elif not go_to_extreme:
            # print('finding something to run into')
            if self.board.rows[row_index-1][cell_index] == 0:
                # print('nothing here')
                self.board.rows[row_index - 1][cell_index] = self.board.rows[row_index][cell_index]
                self.board.rows[row_index][cell_index] = 0
                self.move_cell(row_index-1, cell_index, go_to_extreme)
            elif self.board.rows[row_index-1][cell_index] == self.board.rows[row_index][cell_index]:
                self.board.rows[row_index][cell_index] = self.board.rows[row_index][cell_index] * 2
                self.board.rows[row_index - 1][cell_index] = 0
                self.move_cell(row_index, cell_index, True)
            else:
                # print('some random number, heading back now')
                self.move_cell(row_index, cell_index, True)
        elif go_to_extreme:
            if self.board.rows[row_index+1][cell_index] == 0:
                self.board.rows[row_index + 1][cell_index] = self.board.rows[row_index][cell_index]
                self.board.rows[row_index][cell_index] = 0
                # self.board.print_board()
                self.move_cell(row_index + 1, cell_index, True)
            else:
                pass

    def perform_swipe(self):
        for cell in range(0, 4):
            for row in range(len(self.board.rows)-1, -1, -1):
                self.move_cell(row, cell, False)
