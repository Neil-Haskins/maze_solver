import unittest
from maze import Maze
from graphics import Window

class Tests(unittest.TestCase):
    def test_maze_create_cells(self):
        num_cols = 12
        num_rows = 10
        m1 = Maze(0, 0, num_rows, num_cols, 10, 10)
        self.assertEqual(
            len(m1._cells),
            num_cols,
        )
        self.assertEqual(
            len(m1._cells[0]),
            num_rows,
        )

    def test_maze_create_cells_b(self):
        num_cols = 3
        num_rows = 5
        m1 = Maze(0, 0, num_rows, num_cols, 10, 10)
        self.assertEqual(
            len(m1._cells),
            num_cols,
        )
        self.assertEqual(
            len(m1._cells[0]),
            num_rows,
        )

    def test_maze_break_entrance_exit(self):
        num_cols = 10
        num_rows = 12
        win = Window(800, 600)
        m1 = Maze(10, 10, num_rows, num_cols, 20, 20, win)
        m1._break_entrance_and_exit()
        tl_cell = m1._cells[0][0]
        br_cell = m1._cells[-1][-1]
        self.assertEqual(
            tl_cell.has_top_wall,
            False,
        )
        self.assertEqual(
            br_cell.has_bottom_wall,
            False,
        )

    def cells_visited_reset(self):
        num_cols = 3
        num_rows = 5
        m1 = Maze(0, 0, num_rows, num_cols, 10, 10)
        tl_cell = m1._cells[0][0]
        br_cell = m1._cells[-1][-1]
        for i in range(num_cols):
            for j in range(num_rows):
                cell = m1._cells[i][j]
            self.assertEqual(
                cell.visited,
                False,
            )


if __name__ == "__main__":
    unittest.main()
