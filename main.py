import sys
from window import Window
from point import Point
from line import Line
from cell import Cell
from maze import Maze

def main() -> int:
    win = Window(800, 600)

    maze = Maze(100, 100, 5, 10, 20, 10, win)

    for i in range(5):
        for j in range(10):
            maze._Maze__draw_cell(i, j)

    win.wait_for_close()

if __name__ == '__main__':
    sys.exit(main())