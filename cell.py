from graphics import Window, Line, Point

class Cell:
    def __init__(self, window):
        self.has_top_wall = True
        self.has_right_wall = True
        self.has_bottom_wall = True
        self.has_left_wall = True
        self._x1 = None
        self._x2 = None
        self._y1 = None
        self._y2 = None
        self._win = window

    def draw(self, x1, y1, x2, y2):
        self._x1 = x1
        self._x2 = x2
        self._y1 = y1
        self._y2 = y2
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
    
    def draw_move(self, to_cell, undo=False):
        x1 = (self._x1 + self._x2) / 2
        y1 = (self._y1 + self._y2) / 2
        x2 = (to_cell._x1 + to_cell._x2) / 2
        y2 = (to_cell._y1 + to_cell._y2) / 2
        line = Line(Point(x1, y1), Point(x2, y2))
        if undo:
            self._win.draw_line(line, "grey")
        else:
            self._win.draw_line(line, "red")