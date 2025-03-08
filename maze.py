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
        window=None):
        self.__x_left = x_left
        self.__y_top = y_top
        self.__num_rows = num_rows
        self.__num_cols = num_cols
        self.__cell_size_x = cell_size_x
        self.__cell_size_y = cell_size_y
        self.__window = window
        self.__cells = []

        self.__create_cells()

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
