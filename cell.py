from graphics import Window, Line, Point

class Cell:
    def __init__(self, window=None):
        self.has_top_wall = True
        self.has_right_wall = True
        self.has_bottom_wall = True
        self.has_left_wall = True
        self.visited = False
        self._x1 = None
        self._x2 = None
        self._y1 = None
        self._y2 = None
        self._win = window

    def draw(self, x1, y1, x2, y2):
        if self._win is None:
            return
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
        wall_color = self._win._wall_color
        blank_color = self._win._bg_color
        top_color = wall_color if self.has_top_wall else blank_color
        right_color = wall_color if self.has_right_wall else blank_color
        bottom_color = wall_color if self.has_bottom_wall else blank_color
        left_color = wall_color if self.has_left_wall else blank_color
        self._win.draw_line(Line(points[0], points[1]), top_color)
        self._win.draw_line(Line(points[1], points[2]), right_color)
        self._win.draw_line(Line(points[2], points[3]), bottom_color)
        self._win.draw_line(Line(points[3], points[0]), left_color)
    
    def draw_move(self, to_cell, undo=False):
        if self._win is None:
            return
        x1 = (self._x1 + self._x2) / 2
        y1 = (self._y1 + self._y2) / 2
        x2 = (to_cell._x1 + to_cell._x2) / 2
        y2 = (to_cell._y1 + to_cell._y2) / 2
        line = Line(Point(x1, y1), Point(x2, y2))
        if undo:
            self._win.draw_line(line, self._win._path_undo_color)
        else:
            self._win.draw_line(line, self._win._path_color)

    def break_wall(self, wall):
        if self._win is None:
            return
        lines = [
            Line(Point(self._x1, self._y1), Point(self._x2, self._y1)),
            Line(Point(self._x2, self._y1), Point(self._x2, self._y2)),
            Line(Point(self._x2, self._y2), Point(self._x1, self._y2)),
            Line(Point(self._x1, self._y2), Point(self._x1, self._y1))
        ]
        color = self._win._bg_color
        if wall == "top":
            self.has_top_wall == False
            self._win.draw_line(lines[0], color)
        elif wall == "right":
            self.has_right_wall == False
            self._win.draw_line(lines[1], color)
        elif wall == "bottom":
            self.has_bottom_wall == False
            self._win.draw_line(lines[2], color)
        elif wall == "left":
            self.has_left_wall == False
            self._win.draw_line(lines[3], color)
        else:
            raise Exception("Invalid value for wall, must be one of top, right, bottom, or left.")
