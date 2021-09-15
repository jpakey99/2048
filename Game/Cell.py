class Cell:
    def __init__(self, value, left, right, top, bottom):
        self.value: int = value
        self.left: Cell = left
        self.right: Cell = right
        self.top: Cell = top
        self.bottom: Cell = bottom

    def get_left_value(self):
        return self.left.value

    def get_right_value(self):
        return self.right.value

    def get_top_value(self):
        return self.top.value

    def get_bottom_value(self):
        return self.bottom.value