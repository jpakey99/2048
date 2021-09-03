class CheckGame:
    def __init__(self, board):
        self.board = board

    def check_situation(self) -> bool:
        """Returns True if situation means game can continue, False, if situation means game cannot continue"""
        return False


class Checks(CheckGame):
    def __init__(self, board):
        super().__init__(board)
        self.children = [CheckEmptyCells(board), CheckSwipeUp(board), CheckSwipeLeft(board), CheckSwipeDown(board), CheckSwipeRight(board)]

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
                    return False
        return True


class CheckSwipeLeft(CheckGame):
    def __init__(self, board):
        super().__init__(board)

    def check_situation(self) -> bool:
        return False


class CheckSwipeRight(CheckGame):
    def __init__(self, board):
        super().__init__(board)

    def check_situation(self) -> bool:
        return False


class CheckSwipeUp(CheckGame):
    def __init__(self, board):
        super().__init__(board)

    def check_situation(self) -> bool:
        return False


class CheckSwipeDown(CheckGame):
    def __init__(self, board):
        super().__init__(board)

    def check_situation(self) -> bool:
        return False