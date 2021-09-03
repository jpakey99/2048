class Board:
    def __init__(self):
        self.row1 = [0, 0, 0, 0]
        self.row2 = [0, 0, 0, 0]
        self.row3 = [0, 0, 0, 0]
        self.row4 = [0, 0, 0, 0]

    def is_game_over(self)->bool:
        # first check to see if all places are empty
        # then check to see if any places can be combined
        pass

    def check_empty_cell(self)->bool:
        pass

    def check_swipe_right(self)->bool:
        pass

    def check_swipe_left(self)->bool:
        pass

    def check_swipe_up(self)->bool:
        pass

    def check_swipe_down(self)->bool:
        pass

    def get_point_total(self)->int:
        pass

    def new_cell(self):
        pass