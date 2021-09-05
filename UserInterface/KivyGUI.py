import kivy, math, time
from kivy.app import App
from kivy.uix.gridlayout import GridLayout
# UI Elements
from kivy.uix.button import Button
from kivy.clock import Clock
from Game.board import Board
from Game.swipe import LeftSwipe, RightSwipe, UpSwipe, DownSwipe
from kivy.graphics import Color, Rectangle

C0, C2, C4, C8, C16, C32, C64, C128, C256, C512, C1024, C2048, C4096 = (.836,.901,.766),(.922,.891,.852),(.922,.875,.781),(.945,177,.473),(.957,.582,.387),(.957,.484,.371),(.961,.262,.691),(.926,.805,.441),(.926,.805,.441),(.922,.781,.313),(.926,.77,.246),(.93,.758,.18),(0,0,0),


class Cell(Button):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        if self.text == '0':
            self.background_color = C0
        elif self.text == '2':
            self.background_color = C2
        elif self.text == '4':
            self.background_color = C4
        elif self.text == '8':
            self.background_color = C8
        elif self.text == '16':
            self.background_color = C16
        elif self.text == '32':
            self.background_color = C32
        elif self.text == '64':
            self.background_color = C64
        elif self.text == '128':
            self.background_color = C128
        elif self.text == '256':
            self.background_color = C256
        elif self.text == '512':
            self.background_color = C512
        elif self.text == '1024':
            self.background_color = C1024
        elif self.text == '2048':
            self.background_color = C2048
        else:
            self.background_color = C4096

        if self.text in ['2', '4']:
            self.color = (0,0,0)
        else:
            self.color = (1,1,1)


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
                self.add_widget(Cell(text=str(cell)))

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