from tkinter import Tk, BOTH, Canvas


class Window:
    def __init__(self, width, height, bg="white"):
        self.__root = Tk()
        self.__root.title("Maze Solver")
        self.__canvas = Canvas(self.__root, bg=bg, height=height, width=width)
        self.__canvas.pack(fill=BOTH, expand=1)
        self.__running = False
        self.__root.protocol("WM_DELETE_WINDOW", self.close)

        self.bg_color = bg

    def redraw(self):
        self.__root.update_idletasks()
        self.__root.update()

    def wait_for_close(self):
        self.__running = True
        while self.__running:
            self.redraw()
        print("Window Closed!")

    def close(self):
        self.__running = False

    def draw_line(self, line, fill_color, width=2):
        line.draw(self.__canvas, fill_color, width)