"""
    File: pipes_static_A.py
    Author: Otabek Abduraimov
    Purpose: This program draws 5x5 squares in 520x520 window
                with lines and/or smaller square inside them.
    Course #: CS 120, Fall 2021
"""

from graphics import graphics
gui = graphics(520, 520, "Pipes Static")


def draw_tile(x, y, north, east, south, west, add_blue, knot):
    """
    This function draws squares of the same size with lines
    and/or square within them. The link can be in the north,
    east, south, or west direction
    :param x: the x coordinate of the square
    :param y: the y coordinate of the square
    :param north: bool val to  draws a line in the north direction
    :param east: bool val to  draws a line in the east direction
    :param south: bool val to  draws a line in the south direction
    :param west: bool val to draws a line in the west direction
    :param add_blue: bool val to fill the lines and/or square with blue
    :param knot: bool val to draw a smaller square inside.
    :return:
    """
    LINE_WIDTH = 7
    gui.rectangle(x, y, 100, 100, fill="dark grey")
    if north:
        if add_blue:
            gui.line(x+50, y+50, x+100, y+50, fill="blue", width=LINE_WIDTH)
        else:
            gui.line(x + 50, y + 50, x + 100, y + 50, width=LINE_WIDTH)
    if east:
        if add_blue:
            gui.line(x + 50, y + 50, x+50, y, fill="blue", width=LINE_WIDTH)
        else:
            gui.line(x + 50, y + 50, x + 50, y, width=LINE_WIDTH)
    if south:
        if add_blue:
            gui.line(x + 50, y + 50, x, y+50, fill="blue", width=LINE_WIDTH)
        else:
            gui.line(x + 50, y + 50, x, y + 50, width=LINE_WIDTH)
    if west:
        if add_blue:
            gui.line(x + 50, y + 50, x+50, y+100, fill="blue", width=LINE_WIDTH)
        else:
            gui.line(x + 50, y + 50, x + 50, y + 100, width=LINE_WIDTH)
    if knot:
        if add_blue:
            gui.rectangle(x+35, y+35, 30, 30, fill="blue")
        else:
            gui.rectangle(x+35, y+35, 30, 30)


def main():
    # line 1
    draw_tile(0, 0, north=True, east=False, south=False, west=True, add_blue=False, knot=False)
    draw_tile(105, 0, north=True, east=False, south=True, west=False, add_blue=False, knot=False)
    draw_tile(210, 0, north=True, east=False, south=False, west=False, add_blue=False, knot=True)
    draw_tile(315, 0, north=False, east=False, south=True, west=True, add_blue=False, knot=False)
    draw_tile(420, 0, north=False, east=False, south=False, west=True, add_blue=False, knot=True)
    # line 2
    draw_tile(0, 105, north=False, east=True, south=False, west=True, add_blue=False, knot=False)
    draw_tile(105, 105, north=False, east=False, south=False, west=True, add_blue=True, knot=True)
    draw_tile(210, 105, north=False, east=False, south=True, west=False, add_blue=False, knot=True)
    draw_tile(315, 105, north=True, east=True, south=True, west=False, add_blue=False, knot=False)
    draw_tile(420, 105, north=True, east=False, south=False, west=False, add_blue=False, knot=True)
    # line 3
    draw_tile(0, 210, north=True, east=False, south=True, west=True, add_blue=False, knot=False)
    draw_tile(105, 210, north=True, east=True, south=False, west=True, add_blue=True, knot=False)
    draw_tile(210, 210, north=False, east=True, south=True, west=True, add_blue=True, knot=True)
    draw_tile(315, 210, north=True, east=False, south=True, west=True, add_blue=False, knot=True)
    draw_tile(420, 210, north=False, east=False, south=True, west=False, add_blue=False, knot=True)
    # line 4
    draw_tile(0, 315, north=True, east=False, south=False, west=True, add_blue=True, knot=False)
    draw_tile(105, 315, north=True, east=True, south=True, west=False, add_blue=True, knot=False)
    draw_tile(210, 315, north=True, east=True, south=False, west=False, add_blue=True, knot=False)
    draw_tile(315, 315, north=True, east=True, south=False, west=True, add_blue=False, knot=False)
    draw_tile(420, 315, north=False, east=False, south=False, west=True, add_blue=False, knot=True)
    # line 5
    draw_tile(0, 420, north=False, east=False, south=False, west=True, add_blue=False, knot=True)
    draw_tile(105, 420, north=False, east=True, south=True, west=False, add_blue=False, knot=False)
    draw_tile(210, 420, north=True, east=False, south=False, west=False, add_blue=False, knot=True)
    draw_tile(315, 420, north=False, east=False, south=False, west=True, add_blue=False, knot=True)
    draw_tile(420, 420, north=False, east=False, south=False, west=True, add_blue=False, knot=True)



main()

