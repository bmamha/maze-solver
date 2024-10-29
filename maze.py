from graphics import Cell
import time


class Maze:
    def __init__(self, x1, y1, num_rows, num_cols, cell_size_x, cell_size_y, win=None):
        self.x1 = x1
        self.y1 = y1
        self.num_rows = num_rows
        self.num_cols = num_cols
        self.cell_size_x = cell_size_x
        self.cell_size_y = cell_size_y
        self.win = win
        self._cells = []
        self._create_cells()

    def _create_cells(self):
        for i in range(self.num_cols):
            self._cells.append([])
            for _ in range(self.num_rows):
                self._cells[i].append(Cell())

        self._draw_cells(self.num_cols, self.num_rows)

    def _draw_cells(self, i, j):
        if self.win:
            for c in range(i):
                for r in range(j):
                    self._cells[c][r].draw(
                        self.x1 + c * self.cell_size_x,
                        self.y1 + r * self.cell_size_y,
                        self.x1 + (c + 1) * self.cell_size_x,
                        self.y1 + (r + 1) * self.cell_size_y,
                        self.win,
                    )
                    self._animate()

    def _animate(self):
        if self.win:
            self.win.redraw()
            time.sleep(0.05)

    def _break_entrance_and_exit(self):
        # create entrance at top of maze
        self._cells[0][0].has_top_wall = False
        # create entrance at bottom of maze
        self._cells[self.num_cols - 1][self.num_rows - 1].has_bottom_wall = False
        self._draw_cells(self.num_cols, self.num_rows)
