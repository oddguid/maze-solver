import sys
from window import Window
from point import Point
from line import Line

def main() -> int:
    win = Window(800, 600)
    win.draw_line(Line(Point(0, 0), Point(40, 30)), "black")
    win.draw_line(Line(Point(50,50), Point(40, 70)), "blue")
    win.wait_for_close()

if __name__ == '__main__':
    sys.exit(main())