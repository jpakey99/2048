# import Game.board as board


class CheckGame:
    def __init__(self, board):
        self.board = board

    def check_situation(self) -> bool:
        """Returns True if situation means game can continue, False, if situation means game cannot continue"""
        return False


class Checks(CheckGame):
    def __init__(self, board):
        super().__init__(board)
        self.children = [CheckEmptyCells(board), CheckSwipeVertical(board), CheckSwipeHorizontal(board)]

    def check_situation(self) -> bool:
        # needs one situation to return True for game to continue
        for child in self.children:
            res = child.check_situation()
            if res:
                return True
        return False


class CheckEmptyCells(CheckGame):
    def __init__(self, board):
        super().__init__(board)

    def check_situation(self) -> bool:
        for row in self.board.rows:
            for cell in row:
                if cell == 0:
                    return True
        return False


class CheckSwipeHorizontal(CheckGame):
    def __init__(self, board):
        super().__init__(board)

    def check_situation(self) -> bool:
        for row in self.board.rows:
            prev_cell = -1
            for cell in row:
                if prev_cell != 0 and prev_cell == cell:
                    return True
                elif prev_cell == 0 and cell != 0:
                    return True
                elif prev_cell != cell:
                    prev_cell = cell
        return False


class CheckSwipeVertical(CheckGame):
    def __init__(self, board):
        super().__init__(board)

    def check_situation(self) -> bool:
        for index in range(0,4):
            prev_cell = -1
            for row in self.board.rows:
                if prev_cell != -1 and row[index] == prev_cell:
                    return True
                elif prev_cell == 0 and row[index] != 0:
                    return True
                elif prev_cell != row[index]:
                    prev_cell = row[index]
        return False


class CheckLeftSwipe(CheckGame):
    def __init__(self, board):
        super().__init__(board)

    def check_situation(self) -> bool:
        for row in self.board.rows:
            prev_cell = -1
            for cell in row:
                if prev_cell == -1:
                    prev_cell = cell
                elif prev_cell != 0 and prev_cell == cell:
                    return True
                elif prev_cell == 0 and cell != 0:
                    return True
                else:
                    prev_cell = cell
        return False


class CheckRightSwipe(CheckGame):
    def __init__(self, board):
        super().__init__(board)

    def check_situation(self) -> bool:
        for row in self.board.rows:
            prev_cell = -1
            for cell in reversed(row):
                if prev_cell == -1:
                    prev_cell = cell
                elif prev_cell != 0 and prev_cell == cell:
                    return True
                elif prev_cell == 0 and cell != 0:
                    return True
                else:
                    prev_cell = cell
        return False


class CheckUpSwipe(CheckGame):
    def __init__(self, board):
        super().__init__(board)

    def check_situation(self) -> bool:
        for index in range(0,4):
            prev_cell = -1
            for row in self.board.rows:
                if prev_cell == -1:
                    prev_cell = row[index]
                elif prev_cell != 0 and prev_cell == row[index]:
                    return True
                elif prev_cell == 0 and row[index] != 0:
                    return True
                else:
                    prev_cell = row[index]
        return False


class CheckDownSwipe(CheckGame):
    def __init__(self, board):
        super().__init__(board)

    def check_situation(self) -> bool:
        for index in range(0,4):
            prev_cell = -1
            for row in reversed(self.board.rows):
                if prev_cell == -1:
                    prev_cell = row[index]
                elif prev_cell != 0 and prev_cell == row[index]:
                    return True
                elif prev_cell == 0 and row[index] != 0:
                    return True
                else:
                    prev_cell = row[index]
        return False
