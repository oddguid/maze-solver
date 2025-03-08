import unittest
from maze import Maze

class Tests(unittest.TestCase):
    def test_maze_create_cells(self):
        num_cols = 12
        num_rows = 10
        maze = Maze(0, 0, num_rows, num_cols, 10, 10)

        self.assertEqual(len(maze._Maze__cells), num_rows)
        self.assertEqual(len(maze._Maze__cells[0]), num_cols)

    def test_maze_create_single_cell(self):
        num_cols = 1
        num_rows = 1
        cell_size_x = 1
        cell_size_y = 1

        maze = Maze(0, 0, num_rows, num_cols, cell_size_x, cell_size_y)

        self.assertEqual(len(maze._Maze__cells), num_rows)
        self.assertEqual(len(maze._Maze__cells[0]), num_cols)

        # check cell
        cell = maze._Maze__cells[0][0]
        self.assertEqual(cell._Cell__x_left, 0)
        self.assertEqual(cell._Cell__x_right, cell_size_x)
        self.assertEqual(cell._Cell__y_bottom, cell_size_y)
        self.assertEqual(cell._Cell__y_top, 0)

if __name__ == "__main__":
    unittest.main()
