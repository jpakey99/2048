import random


class Board:
    def __init__(self):
        self.row1 = [0, 0, 0, 0]
        self.row2 = [0, 0, 0, 0]
        self.row3 = [0, 0, 0, 0]
        self.row4 = [0, 0, 0, 0]
        self.rows = [self.row1, self.row2, self.row3, self.row4]

    def is_game_over(self) -> bool:
        # first check to see if all places are empty
        # then check to see if any places can be combined
        return False

    def check_empty_cell(self) -> bool:
        return False

    def check_swipe_right(self) -> bool:
        return False

    def check_swipe_left(self) -> bool:
        return False

    def check_swipe_up(self) -> bool:
        return False

    def check_swipe_down(self) -> bool:
        return False

    def get_point_total(self) -> int:
        score = 0
        for row in self.rows:
            for cell in row:
                score += cell
        return score

    def new_cell(self):
        # must be called after is game_over to ensure empty cell is present
        # get indexes of empty cells and put into a list
        empty_cells = []
        for x, row in enumerate(self.rows):
            for y, cell in enumerate(row):
                if cell == 0:
                    empty_cells.append((x, y))
        # randomize what index in that list gets the new cell
        random_index = random.randint(0, len(empty_cells)-1)
        index = empty_cells[random_index]
        # randomize between 2 and 4 for the value of that cell
        random_value = random.randint(0,1)
        if random_value == 0:
            self.rows[index[0]][index[1]] = 2
        else:
            self.rows[index[0]][index[1]] = 4

    def print_board(self):
        output_string = ''
        for row in self.rows:
            for cell in row:
                output_string += str(cell) + '\t'
            output_string += '\n'
        print(output_string)
