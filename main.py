from graphics import Window, Line, Point
from cell import Cell
from maze import Maze


def main():
    win = Window(800,600)
    p1 = Point(20, 80)
    p2 = Point(150, 100)
    line = Line(p1, p2)
    win.draw_line(line, "red")

    # cell_1 = Cell(win)
    # cell_1.has_right_wall = False
    # cell_1.draw(5, 5, 35, 35)

    # cell_2 = Cell(win)
    # cell_2.has_left_wall = False
    # cell_2.has_bottom_wall = False
    # cell_2.draw(35, 5, 65, 35)

    # cell_3 = Cell(win)
    # cell_3.has_left_wall = False
    # cell_3.has_top_wall = False
    # cell_3.draw(35, 35, 65, 65)

    # cell_1.draw_move(cell_2)
    # cell_2.draw_move(cell_3)
    # cell_3.draw_move(cell_2, True)

    maze = Maze(10, 15, 19, 26, 30, 30, win)

    win.wait_for_close()



main()

print("End of file")