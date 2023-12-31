from tkinter import Tk, BOTH, Canvas

class Window:
    def __init__(self, width, height, colors=None):
        if colors is None:
            colors = {
                "bg": "white",
                "wall": "black",
                "path": "red",
                "path_undo": "grey"
            }
        self._bg_color = colors["bg"]
        self._wall_color = colors["wall"]
        self._path_color = colors["path"]
        self._path_undo_color = colors["path_undo"]

        self.__root = Tk()
        self.__root.title("My maze solver")
        self.__canvas = Canvas(self.__root, width=width, height=height, bg=self._bg_color)
        self.__canvas.pack()
        self.__running = False
        self.__root.protocol("WM_DELETE_WINDOW", self.close)

    def redraw(self):
        self.__root.update_idletasks()
        self.__root.update()

    def wait_for_close(self):
        self.__running = True
        while self.__running:
            self.redraw()
    
    def close(self):
        self.__running = False
    
    def draw_line(self, line, fill_color):
        line.draw(self.__canvas, fill_color)


class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y


class Line:
    def __init__(self, point_1, point_2):
        self.p1 = point_1
        self.p2 = point_2

    def draw(self, canvas, fill_color):
        canvas.create_line(
            self.p1.x, self.p1.y, self.p2.x, self.p2.y, fill=fill_color, width=2
        )
        canvas.pack()


