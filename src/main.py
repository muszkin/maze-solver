from window import Window
from point import Point
from cell import Cell
from maze import Maze


def main():
    win = Window(800, 600)
    # cell_1 = Cell(win)
    # cell_1.has_right_wall = False
    # cell_1.draw(Point(10, 10), Point(20, 20))
    # cell_2 = Cell(win)
    # cell_2.has_left_wall = False
    # cell_2.draw(Point(21,10), Point(31, 20))
    # cell_1.draw_move(cell_2, True)
    maze = Maze(0, 0, 10, 10, 10, 10, win)

    win.wait_for_close()


if __name__ == "__main__":
    main()
