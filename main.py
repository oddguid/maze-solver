import sys
from window import Window
from point import Point
from line import Line
from cell import Cell

def main() -> int:
    win = Window(800, 600)

    cell_1 = Cell(10, 20, 50, 40, win)

    cell_2 = Cell(30, 40, 50, 40, win)
    cell_2.has_left_wall = False

    cell_3 = Cell(50, 60, 50, 40, win)
    cell_3.has_right_wall = False

    cell_4 = Cell(70, 80, 50, 40, win)
    cell_4.has_bottom_wall = False

    cell_5 = Cell(90, 100, 50, 40, win)
    cell_5.has_top_wall = False

    cell_6 = Cell(10, 20, 70, 60, win)
    cell_6.has_left_wall = False
    cell_6.has_right_wall = False

    cell_7 = Cell(30, 40, 70, 60, win)
    cell_7.has_bottom_wall = False
    cell_7.has_top_wall = False

    cell_1.draw()
    cell_2.draw()
    cell_3.draw()
    cell_4.draw()
    cell_5.draw()
    cell_6.draw()
    cell_7.draw()

    win.wait_for_close()

if __name__ == '__main__':
    sys.exit(main())