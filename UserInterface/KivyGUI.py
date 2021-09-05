import kivy, math, time
from kivy.app import App
from kivy.uix.gridlayout import GridLayout
# UI Elements
from kivy.uix.label import Label
from kivy.clock import Clock
from Game.board import Board
from Game.swipe import LeftSwipe, RightSwipe, UpSwipe, DownSwipe


class GameGUI(GridLayout):
    def __init__(self, board: Board, **kwargs):
        super().__init__(**kwargs)
        self.cols, self.rows = 4,4
        self.board = board
        self.update_board()
        self.touch = None
        self.latest_move = None

    def update_board(self):
        self.board.new_cell()
        self.clear_widgets()
        for row in self.board.rows:
            for cell in row:
                self.add_widget(Label(text=str(cell)))

    def play_game(self, _):
        if self.board.is_game_over():
            self.clear_widgets()

    def on_touch_down(self, touch):
        self.touch = (touch.x, touch.y)

    def on_touch_up(self, touch):
        if abs(touch.x - self.touch[0]) > abs(touch.y - self.touch[1]):
            if touch.x - self.touch[0] < 0:
                print('left swipe')
                move = LeftSwipe(self.board)
            else:
                print('right swipe')
                move = RightSwipe(self.board)
        else:
            if touch.y - self.touch[1] > 0:
                print('up swipe')
                move = UpSwipe(self.board)
            else:
                print('down swipe')
                move = DownSwipe(self.board)
        move.perform_swipe()
        self.update_board()


class GameApp(App):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        board = Board()
        self.gui = GameGUI(board)

    def build(self):
        Clock.schedule_interval(self.gui.play_game, 1/60)
        return self.gui


if __name__ == '__main__':
    GameApp().run()