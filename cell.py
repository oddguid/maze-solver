from point import Point
from line import Line

class Cell:
    def __init__(self, x_left, x_right, y_bottom, y_top, window):
        self.has_left_wall = True
        self.has_right_wall = True
        self.has_top_wall = True
        self.has_bottom_wall = True
        self.__x_left = x_left
        self.__x_right = x_right
        self.__y_bottom = y_bottom
        self.__y_top = y_top
        self.__window = window

    def center_point(self):
        x_mid = (self.__x_left + self.__x_right) // 2
        y_mid = (self.__y_bottom + self.__y_top) // 2

        return Point(x_mid, y_mid)

    def draw(self):
        left_bottom = Point(self.__x_left, self.__y_bottom)
        left_top = Point(self.__x_left, self.__y_top)
        right_bottom = Point(self.__x_right, self.__y_bottom)
        right_top = Point(self.__x_right, self.__y_top)

        if self.has_left_wall:
            self.__window.draw_line(Line(left_bottom, left_top), "black")

        if self.has_right_wall:
            self.__window.draw_line(Line(right_bottom, right_top), "black")

        if self.has_bottom_wall:
            self.__window.draw_line(Line(left_bottom, right_bottom), "black")

        if self.has_top_wall:
            self.__window.draw_line(Line(left_top, right_top), "black")

    def draw_move(self, to_cell, undo=False):
        start_point = self.center_point()
        end_point = to_cell.center_point()
        color = "red"

        if undo:
            color = "gray"

        self.__window.draw_line(Line(start_point, end_point), color)
