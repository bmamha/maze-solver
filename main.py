from graphics import Window
from maze import Maze

win = Window(800, 600)
maze = Maze(100, 200, 10, 10, 25, 25, win)
maze.solve()

win.wait_for_close()
