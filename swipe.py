from Game.board import Board

class Swipe:
    def __init__(self, board: Board):
        self.board = board

    def perform_swipe(self):
        pass


class LeftSwipe(Swipe):
    def __init__(self, board: Board):
        super().__init__(board)

    def perform_swipe(self):
        pass


class RightSwipe(Swipe):
    def __init__(self, board: Board):
        super().__init__(board)

    def perform_swipe(self):
        pass


class UpSwipe(Swipe):
    def __init__(self, board: Board):
        super().__init__(board)

    def perform_swipe(self):
        pass


class DownSwipe(Swipe):
    def __init__(self, board: Board):
        super().__init__(board)

    def perform_swipe(self):
        pass