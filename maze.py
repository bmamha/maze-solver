from graphics import Cell
import time
import random


class Maze:
    def __init__(
        self, x1, y1, num_rows, num_cols, cell_size_x, cell_size_y, win=None, seed=None
    ):
        self.x1 = x1
        self.y1 = y1
        self.num_rows = num_rows
        self.num_cols = num_cols
        self.cell_size_x = cell_size_x
        self.cell_size_y = cell_size_y
        self.win = win
        self.seed = seed
        self._cells = []
        if self.seed is not None:
            random.seed(self.seed)
        self._create_cells()

    def _create_cells(self):
        for i in range(self.num_cols):
            self._cells.append([])
            for _ in range(self.num_rows):
                self._cells[i].append(Cell())

        self._draw_cells(self.num_cols, self.num_rows)
        self._break_entrance_and_exit()
        self._break_walls_r(0, 0)
        self._reset_cells_visited()

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
            time.sleep(0.0005)

    def _break_entrance_and_exit(self):
        # create entrance at top of maze
        self._cells[0][0].has_top_wall = False
        # create entrance at bottom of maze
        self._cells[self.num_cols - 1][self.num_rows - 1].has_bottom_wall = False
        self._draw_cells(self.num_cols, self.num_rows)

    def _break_walls_r(self, i, j):
        current_cell = self._cells[i][j]
        current_cell.visited = True
        while True:
            to_visit = []

            if j - 1 >= 0:
                if not self._cells[i][j - 1].visited:
                    to_visit.append((i, j - 1))

            if j + 1 < self.num_rows:
                if not self._cells[i][j + 1].visited:
                    to_visit.append((i, j + 1))

            if i - 1 >= 0:
                if not self._cells[i - 1][j].visited:
                    to_visit.append((i - 1, j))

            if i + 1 < self.num_cols:
                if not self._cells[i + 1][j].visited:
                    to_visit.append((i + 1, j))

            if len(to_visit) == 0:
                self._draw_cells(self.num_cols, self.num_rows)
                return

            selected_cell = random.choice(to_visit)

            # top_cell
            if selected_cell[1] == j - 1:
                self._cells[i][j - 1].has_bottom_wall = False
                current_cell.has_top_wall = False

            # left_cell
            if selected_cell[0] == i - 1:
                self._cells[i - 1][j].has_right_wall = False
                current_cell.has_left_wall = False

            # right_cell
            if selected_cell[0] == i + 1:
                self._cells[i + 1][j].has_left_wall = False
                current_cell.has_right_wall = False

            # bottom_cell
            if selected_cell[1] == j + 1:
                self._cells[i][j + 1].has_top_wall = False
                current_cell.has_bottom_wall = False

            self._break_walls_r(selected_cell[0], selected_cell[1])

    def _reset_cells_visited(self):
        for c in range(self.num_cols):
            for r in range(self.num_rows):
                self._cells[c][r].visited = False

    def solve(self):
        return self._solve_r(0, 0)

    def _solve_r(self, i, j):
        self._animate()
        self._cells[i][j].visited = True
        if i == self.num_cols - 1 and j == self.num_rows - 1:
            return True

        # top
        if (
            j - 1 >= 0
            and not self._cells[i][j - 1].visited
            and not self._cells[i][j].has_top_wall
        ):
            print("moving to the top")
            self._cells[i][j].draw_move(self._cells[i][j - 1])
            next = self._solve_r(i, j - 1)
            if next:
                return True
            else:
                print("wrong path reached")
                self._cells[i][j].draw_move(self._cells[i][j - 1], True)

        # bottom
        if (
            j + 1 < self.num_rows
            and not self._cells[i][j + 1].visited
            and not self._cells[i][j].has_bottom_wall
        ):
            print("moving to the bottom")
            self._cells[i][j].draw_move(self._cells[i][j + 1])
            next = self._solve_r(i, j + 1)
            if next:
                return True
            else:
                print("wrong path reached, redraw")
                self._cells[i][j].draw_move(self._cells[i][j + 1], True)

        # left
        if (
            i - 1 >= 0
            and not self._cells[i - 1][j].visited
            and not self._cells[i][j].has_left_wall
        ):
            print("moving to the left")
            self._cells[i][j].draw_move(self._cells[i - 1][j])
            next = self._solve_r(i - 1, j)
            if next:
                return True
            else:
                print("wrong path reached")
                self._cells[i][j].draw_move(self._cells[i - 1][j], True)

        # right
        if (
            i + 1 < self.num_cols
            and not self._cells[i + 1][j].visited
            and not self._cells[i][j].has_right_wall
        ):
            print("moving to the right")
            self._cells[i][j].draw_move(self._cells[i + 1][j])
            next = self._solve_r(i + 1, j)
            if next:
                return True
            else:
                print("wrong path reached")
                self._cells[i][j].draw_move(self._cells[i + 1][j], True)

        return False
