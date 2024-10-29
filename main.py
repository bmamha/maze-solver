from graphics import Window
from maze import Maze


win = Window(800, 600)
maze = Maze(100, 200, 10, 10, 50, 50, win)
maze._break_entrance_and_exit()
win.wait_for_close()
