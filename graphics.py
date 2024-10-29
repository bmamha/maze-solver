from tkinter import Tk, BOTH, Canvas


class Window:
    def __init__(self, width, height):
        self.__root = Tk()
        self.__root.title("Maze Solver")
        self.canvas = Canvas(self.__root, width=width, height=height, bg="white")
        self.canvas.pack(fill=BOTH, expand=1)
        self.__running = False
        self.__root.protocol("WM_DELETE_WINDOW", self.close)

    def redraw(self):
        self.__root.update()
        self.__root.update_idletasks()

    def draw_line(self, line, fill_color):
        line.draw(self.canvas, fill_color)

    def wait_for_close(self):
        self.__running = True
        while self.__running:
            self.redraw()

    def after(self, delay_ms, callback):
        self.__root.after(delay_ms, callback)

    def close(self):
        self.__running = False


class Point:
    def __init__(self, x, y) -> None:
        self.x = x
        self.y = y


class Line:
    def __init__(self, point1, point2):
        self.__point1 = point1
        self.__point2 = point2

    def draw(self, canvas, fill_color):
        x1 = self.__point1.x
        y1 = self.__point1.y
        x2 = self.__point2.x
        y2 = self.__point2.y

        canvas.create_line(x1, y1, x2, y2, fill=fill_color, width=3)


class Cell:
    def __init__(self):
        self.__x1 = None
        self.__x2 = None
        self.__y1 = None
        self.__y2 = None
        self.has_left_wall = True
        self.has_right_wall = True
        self.has_top_wall = True
        self.has_bottom_wall = True
        self._win = None

    def draw(self, x1, y1, x2, y2, win):
        self.__x1 = x1
        self.__x2 = x2
        self.__y1 = y1
        self.__y2 = y2
        point1 = Point(self.__x1, self.__y1)
        point2 = Point(self.__x1, self.__y2)
        point3 = Point(self.__x2, self.__y1)
        point4 = Point(self.__x2, self.__y2)
        self._win = win

        if self._win is not None:
            if self.has_left_wall:
                line = Line(point1, point2)
                self._win.draw_line(line, "black")
            else:
                line = Line(point1, point2)
                self._win.draw_line(line, "white")

            if self.has_right_wall:
                line = Line(point3, point4)
                self._win.draw_line(line, "black")
            else:
                line = Line(point3, point4)
                self._win.draw_line(line, "white")

            if self.has_top_wall:
                line = Line(point1, point3)
                self._win.draw_line(line, "black")
            else:
                line = Line(point1, point3)
                self._win.draw_line(line, "white")

            if self.has_bottom_wall:
                line = Line(point2, point4)
                self._win.draw_line(line, "black")

            else:
                line = Line(point2, point4)
                self._win.draw_line(line, "white")

    def draw_move(self, to_cell, undo=False):
        if self._win and self.__x1 and self.__y1 and to_cell._win:
            center_x = (self.__x1 + self.__x2) // 2
            center_y = (self.__y1 + self.__y2) // 2
            center = Point(center_x, center_y)

            to_cell_center_x = abs(to_cell.__x1 + to_cell.__x2) // 2
            to_cell_center_y = abs(to_cell.__y1 + to_cell.__y2) // 2
            to_cell_center = Point(to_cell_center_x, to_cell_center_y)

            line = Line(center, to_cell_center)

            if not undo:
                self._win.draw_line(line, "red")
            else:
                self._win.draw_line(line, "gray")
