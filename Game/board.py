import random
from Game.check_game import Checks, CheckSwipeVertical, CheckSwipeHorizontal

class Board:
    def __init__(self):
        self.row1 = [0, 0, 0, 0]
        self.row2 = [0, 0, 0, 0]
        self.row3 = [0, 0, 0, 0]
        self.row4 = [0, 0, 0, 0]
        self.rows = [self.row1, self.row2, self.row3, self.row4]

    def is_game_over(self) -> bool:
        checks  = Checks(self)
        return not checks.check_situation()

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
        random_value = random.randint(0,100)
        if random_value <= 89:
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

    def __eq__(self, other):
        if isinstance(other, Board):
            for row_index in range(0, len(self.rows)):
                for cell_index in range(0, len(self.rows[row_index])):
                    if self.rows[row_index][cell_index] != other.rows[row_index][cell_index]:
                        return False
            return True
        return False

    def __copy__(self):
        board_copy: Board = Board()
        for row in range(0,4):
            for cell in range(0,4):
                board_copy.rows[row][cell] = self.rows[row][cell]
        return board_copy

    def get_value(self):
        zero_cells = 0
        total_value = 0
        values_found = []
        duplicated = 0
        same_value_next = 0

        for row in range(len(self.rows)):
            for cell in range(len(self.rows)):
                if self.rows[row][cell] == 0:
                    zero_cells += 1
                elif self.rows[row][cell] in values_found:
                    duplicated += 1
                elif self.rows[row][cell] not in values_found:
                    values_found.append(self.rows[row][cell])
                if cell < 3 and self.rows[row][cell+1] == self.rows[row][cell]:
                    same_value_next += self.rows[row][cell]*2
                elif row < 3 and self.rows[row+1][cell] == self.rows[row][cell]:
                    same_value_next += self.rows[row][cell]*2

                total_value += self.rows[row][cell]
        return (total_value) / (duplicated + 1) + len(values_found)
