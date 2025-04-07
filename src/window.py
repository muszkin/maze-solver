from tkinter import Tk, BOTH, Canvas
from line import Line


class Window:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.__root_widget = Tk()
        self.__canvas = Canvas()
        self.__canvas.pack()
        self.__is_window_running = False
        self.__root_widget.protocol("WM_DELETE_WINDOW", self.close)

    def redraw(self):
        self.__root_widget.update_idletasks()
        self.__root_widget.update()

    def wait_for_close(self):
        self.__is_window_running = True
        while self.__is_window_running:
            self.redraw()

    def close(self):
        self.__is_window_running = False

    def draw_line(self, line: Line, fill_color: str= "black"):
        line.draw(self.__canvas, fill_color)

