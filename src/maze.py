import time

from cell import Cell
from point import Point
from window import Window


class Maze:
    def __init__(
            self,
            x1,
            y1,
            num_rows,
            num_cols,
            cell_size_x,
            cell_size_y,
            win: Window = None,
    ):
        self._x1 = x1
        self._y1 = y1
        self._num_rows = num_rows
        self._num_cols = num_cols
        self._cell_size_x = cell_size_x
        self._cell_size_y = cell_size_y
        self.win = win
        self._create_cells()

    def _create_cells(self):
        self._cells = [[Cell(self.win) for i in range(self._num_rows)] for _ in range(self._num_cols)]
        for col in range(len(self._cells)):
            for row in range(len(self._cells[col])):
                self._draw_cell(col, row)

    def _draw_cell(self, i, j):
        self._break_entrance_and_exit()
        cell = self._cells[i][j]
        top_left = Point(self._x1 + (self._cell_size_x * (i + 1)), self._y1 + (self._cell_size_y * (j + 1)))
        bottom_right = Point(top_left.x + self._cell_size_x, top_left.y + self._cell_size_y)
        if self.win:
            cell.draw(top_left, bottom_right)

    def _animate(self):
        if self.win:
            self.win.redraw()
        time.sleep(0.05)

    def _break_entrance_and_exit(self):
        self._cells[0][0].has_top_wall = False
        self._cells[-1][-1].has_bottom_wall = False

