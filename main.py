from graphics import Window, Line, Point
from cell import Cell
from maze import Maze


def main():
    colors = {
        "bg": "white",
        "wall": "black",
        "path": "red",
        "path_undo": "grey"
    }
    win = Window(800, 600, colors)
    maze = Maze(10, 15, 19, 26, 30, 30, win)
    maze.solve()

    win.wait_for_close()



main()

print("End of file")