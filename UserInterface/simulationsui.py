# from UserInterface.KivyGUI import Cell
from Simulations.simulation import RandomSimulation
from kivy.app import App
from kivy.uix.gridlayout import GridLayout
# UI Elements
from kivy.uix.button import Button
from kivy.clock import Clock
from Game.board import Board
from kivy.graphics import Color, Rectangle
from kivy.core.window import Window


C0, C2, C4, C8, C16, C32, C64, C128, C256, C512, C1024, C2048, C4096 = (214/255,205/255,196/255,1),(238/255,228/255,218/255,1),(237/255,224/255,200/255,1),(242/255,177/255,121/255,1),\
                                                                       (245/255,149/255,99/255,1),(246/255,124/255,95/255,1),(246/255,94/255,56/255,1),(237/255,207/255,114/255,1),\
                                                                       (237/255,204/255,97/255,1),(237/255,200/255,80/255,1),(237/255,197/255,63/255,1),(237/255,194/255,46/255,1),(0,0,0,1)


class Cell(Button):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.background_normal = 'backgrounds/black.png'
        self.background_down = 'backgrounds/black.png'
        self.border = (30, 30, 30, 30)

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

        if self.text in ['2', '4', '0']:
            self.color = (0,0,0)
        else:
            self.color = (1,1,1)


class SimulationUI(GridLayout):
    def __init__(self, board: Board, simulation:RandomSimulation, **kwargs):
        super().__init__(**kwargs)
        self.simulation = simulation
        self.cols, self.rows = 4,4
        self.board = board
        self.update_board()
        self.touch = None
        self.latest_move = None
        self.padding = (15, 15, 15, 15)
        self.spacing = (10, 10)
        self.game_over = False

    def update_board(self):
        self.board.new_cell()
        self.clear_widgets()
        for row in self.board.rows:
            for cell in row:
                self.add_widget(Cell(text=str(cell)))
        with self.canvas.before:
            Color(187/255, 173/255, 160/255, 1)
            Rectangle(pos=self.pos, size=Window.size)

    def run_simulation(self, _):
        if self.board.is_game_over():
            self.clear_widgets()
            self.game_over = True
        else:
            move_made = False
            while not move_made:
                move_made = self.simulation.make_move()
            self.update_board()


class GameApp(App):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        board = Board()
        self.gui = SimulationUI(board, RandomSimulation(board))

    def build(self):
        clock = Clock.schedule_interval(self.gui.run_simulation, 1)
        if self.gui.game_over:
            Clock.unschedule(self.gui.run_simulation)
        return self.gui


if __name__ == '__main__':
    GameApp().run()
