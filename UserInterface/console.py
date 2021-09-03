class ConsoleUI:
    def __init__(self, board):
        self.board = board

    def display(self):
        output_string = ''
        for row in self.board.rows:
            for cell in row:
                output_string += str(cell) + '\t'
            output_string += '\n'
        print(output_string)
        print(self.board.get_point_total())

    def make_move(self):
        user = input("0: swipe left; 1: swipe right, 2: swipe up, 3: swipe down")
        if user in ['0', '1', '2', '3']:
            return user
