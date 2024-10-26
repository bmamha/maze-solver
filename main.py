from window import Window, Line, Point


win = Window(800, 600)
point1 = Point(100, 150)
point2 = Point(300, 450)
line = Line(point1, point2)
win.draw_line(line, "red")
win.wait_for_close()
