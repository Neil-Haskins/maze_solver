from tkinter import Tk, BOTH, Canvas
import time
from cell import Cell
import random

class Maze:
    def __init__(
        self,
        x1,
        y1,
        num_rows,
        num_cols,
        cell_size_x,
        cell_size_y,
        win=None,
        seed=None
    ):
        self.x1 = x1
        self.y1 = y1
        self.num_rows = num_rows
        self.num_cols = num_cols
        self.cell_size_x = cell_size_x
        self.cell_size_y = cell_size_y
        self.win = win
        self.seed = seed if seed is None else random.seed(seed)
        self._create_cells()
        self._break_entrance_and_exit()
        self._break_walls_r(0, 0)
        self._reset_cells_visited()

    def _create_cells(self):
        self._cells = []
        for i in range(self.num_cols):
            column = []
            for j in range(self.num_rows):
                column.append(Cell(self.win))
            self._cells.append(column)
        for i in range(self.num_cols):
            for j in range(self.num_rows):
                self._draw_cell(i, j)

    def _draw_cell(self, i, j):
        x1 = self.x1 + (self.cell_size_x * i)
        y1 = self.y1 + (self.cell_size_y * j)
        x2 = self.x1 + (self.cell_size_x * (i + 1))
        y2 = self.y1 + (self.cell_size_y * (j + 1))
        cell = self._cells[i][j]
        cell.draw(x1, y1, x2, y2)
        self._animate()

    def _animate(self, solving=False):
        if self.win is None:
            return
        num_cells = len(self._cells) * len(self._cells[0])
        self.win.redraw()
        if solving:
            time.sleep(0.05)
        else:
            time.sleep(min(0.05, 3 / num_cells))

    def _break_entrance_and_exit(self):
        self._cells[0][0].break_wall('top')
        self._cells[-1][-1].break_wall('bottom')

    def _get_valid_directions(self, i, j):
        directions = []
        if i >= 1:
            directions.append( (i-1,j) )
        if i <= len(self._cells) - 2:
            directions.append( (i+1, j) )
        if j >= 1:
            directions.append( (i, j-1) )
        if j <= len(self._cells[0]) - 2:
            directions.append( (i, j+1) )
        return directions

    def _break_walls_r(self, i, j):
        current = self._cells[i][j]
        current.visited = True
        while True:
            to_visit = []
            directions = self._get_valid_directions(i, j)
            for direction in directions:
                if self._cells[direction[0]][direction[1]].visited == False:
                    to_visit.append(direction)
            if len(to_visit) == 0:
                break

            direction = to_visit[random.randrange(len(to_visit))]
            next_cell = self._cells[direction[0]][direction[1]]

            if direction[0] == i-1:
                current.break_wall("left")
                next_cell.break_wall("right")
            elif direction[0] == i+1:
                current.break_wall("right")
                next_cell.break_wall("left")
            elif direction[1] == j-1:
                current.break_wall("top")
                next_cell.break_wall("bottom")
            elif direction[1] == j+1:
                current.break_wall("bottom")
                next_cell.break_wall("top")

            self._break_walls_r(direction[0], direction[1])

    def _reset_cells_visited(self):
        for col in self._cells:
            for cell in col:
                cell.visited = False

    def solve(self):
        return self._solve_r(0, 0)

    def _solve_r(self, i, j):
        self._animate(True)
        current = self._cells[i][j]
        current.visited = True
        if current == self._cells[-1][-1]:
            return True
        
        directions = self._get_valid_directions(i, j)
        for direction in directions:
            next_cell = self._cells[direction[0]][direction[1]]
            if next_cell.visited:
                continue
            if (
                    (direction[0] == i-1 and not current.has_left_wall and not next_cell.has_right_wall) or
                    (direction[0] == i+1 and not current.has_right_wall and not next_cell.has_left_wall) or
                    (direction[1] == j-1 and not current.has_top_wall and not next_cell.has_bottom_wall) or
                    (direction[1] == j+1 and not current.has_bottom_wall and not next_cell.has_top_wall)
                ):
                current.draw_move(next_cell)
                if self._solve_r(direction[0], direction[1]):
                    return True
                else:
                    current.draw_move(next_cell, True)

        return False

