import sys
from window import Window

def main() -> int:
    win = Window(800, 600)
    win.wait_for_close()

if __name__ == '__main__':
    sys.exit(main())