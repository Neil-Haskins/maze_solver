from graphics import Window, Line, Point


class Cell:
    def __init__(self, x1, y1, x2, y2, wall_t, wall_r, wall_b, wall_l, window):
        self.has_top_wall = wall_t
        self.has_right_wall = wall_r
        self.has_bottom_wall = wall_b
        self.has_left_wall = wall_l
        self._x1 = x1
        self._x2 = x2
        self._y1 = y1
        self._y2 = y2
        self._win = window

    def draw(self, x1, y1, x2, y2):
        points = [
            Point(x1, y1),
            Point(x2, y1),
            Point(x2, y2),
            Point(x1, y2)
        ]
        color = "black"
        if self.has_top_wall:
            self._win.draw_line(Line(points[0], points[1]), color)
        if self.has_right_wall:
            self._win.draw_line(Line(points[1], points[2]), color)
        if self.has_bottom_wall:
            self._win.draw_line(Line(points[2], points[3]), color)
        if self.has_left_wall:
            self._win.draw_line(Line(points[3], points[0]), color)







def main():
    win = Window(800,600)
    p1 = Point(20, 80)
    p2 = Point(150, 100)
    line = Line(p1, p2)
    win.draw_line(line, "red")

    cell_1 = Cell(0, 0, 30, 30, True, True, True, False, win)
    cell_1.draw(0, 0, 30, 30)

    cell_2 = Cell(25, 25, 85, 85, True, False, True, True, win)
    cell_2.draw(25, 25, 85, 85)

    win.wait_for_close()





main()

print("End of file")