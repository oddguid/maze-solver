import random
import time
from cell import Cell

class Maze:
    def __init__(
        self,
        x_left,
        y_top,
        num_rows,
        num_cols,
        cell_size_x,
        cell_size_y,
        window=None,
        seed=None):
        self.__x_left = x_left
        self.__y_top = y_top
        self.__num_rows = num_rows
        self.__num_cols = num_cols
        self.__cell_size_x = cell_size_x
        self.__cell_size_y = cell_size_y
        self.__window = window
        self.__cells = []

        if seed:
            random.seed(a=seed)

        self.__create_cells()
        self.__break_entrance_and_exit()
        self.__break_walls_r(0, 0)

    def __create_cells(self):
        for y in range(self.__num_rows):
            cell_row = []

            y_top = self.__y_top + y * self.__cell_size_y
            y_bottom = y_top + self.__cell_size_y

            for x in range(self.__num_cols):
                x_left = self.__x_left + x * self.__cell_size_x
                x_right = x_left + self.__cell_size_x

                cell = Cell(x_left, x_right, y_bottom, y_top, self.__window)
                cell_row.append(cell)

            self.__cells.append(cell_row)

        for y in range(self.__num_rows):
            for x in range(self.__num_cols):
                self.__draw_cell(y, x)

    def __draw_cell(self, i, j):
        self.__cells[i][j].draw()
        self.__animate()

    def __animate(self):
        if self.__window:
            self.__window.redraw()
            
        time.sleep(0.05)

    def __break_entrance_and_exit(self):
        self.__cells[0][0].has_top_wall = False
        self.__draw_cell(0, 0)
        self.__cells[self.__num_rows - 1][self.__num_cols - 1].has_bottom_wall = False
        self.__draw_cell(self.__num_rows - 1, self.__num_cols - 1)

    def __break_walls_r(self, i, j):
        self.__cells[i][j].visited = True

        while True:
            to_visit = []

            # top
            if (i > 0
                and self.__cells[i - 1][j].visited == False):
                to_visit.append((i - 1, j, "top"))

            # bottom
            if (i < self.__num_rows - 1
                and self.__cells[i + 1][j].visited == False):
                to_visit.append((i + 1, j, "bottom"))
            
            # left
            if (j > 0
                and self.__cells[i][j - 1].visited == False):
                to_visit.append((i, j - 1, "left"))
            
            # right
            if (j < self.__num_cols - 1
                and self.__cells[i][j + 1].visited == False):
                to_visit.append((i, j + 1, "right"))
            
            if len(to_visit) == 0:
                self.__draw_cell(i, j)
                break
            
            # choose random neighbor
            index = random.randrange(len(to_visit))

            # break down walls
            n_i, n_j, n_dir = to_visit[index]

            if n_dir == "left":
                self.__cells[i][j].has_left_wall = False
                self.__cells[n_i][n_j].has_right_wall = False
            elif n_dir == "right":
                self.__cells[i][j].has_right_wall = False
                self.__cells[n_i][n_j].has_left_wall = False
            elif n_dir == "top":
                self.__cells[i][j].has_top_wall = False
                self.__cells[n_i][n_j].has_bottom_wall = False
            else:
                self.__cells[i][j].has_bottom_wall = False
                self.__cells[n_i][n_j].has_top_wall = False

            self.__break_walls_r(n_i, n_j)
