"""
    File: pipes_static_B.py
    Author: Otabek Abduraimov
    Purpose: This program program draws two pictures
    onto two windows. The first one draws a random square
    with north, east, south, or west pipe and/or in blue and/or
    with a know in the middle. And if it fits the pattern,
    it is going to print move
    to the second window. Eventually, the second
    will fill up with squares of fitting patterns.
    Course #: CS 120, Fall 2021
"""

from graphics import graphics

gui = graphics(520, 520, "Pipes Static")
win = graphics(520, 520, "Store Window")


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
            gui.line(x + 50, y + 50, x + 100, y + 50, fill="blue", width=LINE_WIDTH)
        else:
            gui.line(x + 50, y + 50, x + 100, y + 50, width=LINE_WIDTH)
    if east:
        if add_blue:
            gui.line(x + 50, y + 50, x + 50, y, fill="blue", width=LINE_WIDTH)
        else:
            gui.line(x + 50, y + 50, x + 50, y, width=LINE_WIDTH)
    if south:
        if add_blue:
            gui.line(x + 50, y + 50, x, y + 50, fill="blue", width=LINE_WIDTH)
        else:
            gui.line(x + 50, y + 50, x, y + 50, width=LINE_WIDTH)
    if west:
        if add_blue:
            gui.line(x + 50, y + 50, x + 50, y + 100, fill="blue", width=LINE_WIDTH)
        else:
            gui.line(x + 50, y + 50, x + 50, y + 100, width=LINE_WIDTH)
    if knot:
        if add_blue:
            gui.rectangle(x + 35, y + 35, 30, 30, fill="blue")
        else:
            gui.rectangle(x + 35, y + 35, 30, 30)


def draw_tile_win(x, y, north, east, south, west, add_blue, knot):
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
    win.rectangle(x, y, 100, 100, fill="dark grey")
    if north:
        if add_blue:
            win.line(x + 50, y + 50, x + 100, y + 50, fill="blue", width=LINE_WIDTH)
        else:
            win.line(x + 50, y + 50, x + 100, y + 50, width=LINE_WIDTH)
    if east:
        if add_blue:
            win.line(x + 50, y + 50, x + 50, y, fill="blue", width=LINE_WIDTH)
        else:
            win.line(x + 50, y + 50, x + 50, y, width=LINE_WIDTH)
    if south:
        if add_blue:
            win.line(x + 50, y + 50, x, y + 50, fill="blue", width=LINE_WIDTH)
        else:
            win.line(x + 50, y + 50, x, y + 50, width=LINE_WIDTH)
    if west:
        if add_blue:
            win.line(x + 50, y + 50, x + 50, y + 100, fill="blue", width=LINE_WIDTH)
        else:
            win.line(x + 50, y + 50, x + 50, y + 100, width=LINE_WIDTH)
    if knot:
        if add_blue:
            win.rectangle(x + 35, y + 35, 30, 30, fill="blue")
        else:
            win.rectangle(x + 35, y + 35, 30, 30)


import random


def draw_square(gui, row, column):
    """
    This function draws squares with random
    shapes inside them and if they fit the
    requirements of the overall shape, it is gonna move
    it to the second screen and keep them there.
    :param gui: graphics instance
    :param row: the row of the square
    :param column: the column of the square
    :return:
    """
    x_coor = 0
    y_coor = 0
    if row == 1:
        x_coor = 0
    elif row == 2:
        x_coor = 105
    elif row == 3:
        x_coor = 210
    elif row == 4:
        x_coor = 315
    elif row == 5:
        x_coor = 420

    if column == 1:
        y_coor = 0
    elif column == 2:
        y_coor = 105
    elif column == 3:
        y_coor = 210
    elif column == 4:
        y_coor = 315
    elif column == 5:
        y_coor = 420
    whole_window = []

    flag1 = True
    while flag1:
        gui.clear()
        north = random.choice([True, False])
        east = random.choice([True, False])
        south = random.choice([True, False])
        west = random.choice([True, False])
        add_blue = random.choice([True, False])
        knot = random.choice([True, False])
        draw_tile(x_coor, y_coor, north, east, south, west, add_blue, knot)

        i1 = 5000
        if row == 1 and column == 1:
            if north and (not east) \
                    and (not south) and (not west) \
                    and add_blue and knot:
                draw_tile_win(x_coor, y_coor, north=True,
                              east=False, south=False, west=False,
                              add_blue=True, knot=True)
                gui.text(150, 150, "Good match", fill="green", size=50)
                i = 0
                while i <= i1:
                    gui.text(150, 150, "Good match", fill="green", size=50)
                    i += 1

                flag1 = False
        elif column == 1 and row != 5:
            if north and (not east) \
                    and south and not west \
                    and not add_blue and not knot:
                draw_tile_win(x_coor, y_coor, north=True,
                              east=False, south=True, west=False,
                              add_blue=False, knot=False)
                gui.text(150, 150, "Good match", fill="green", size=50)
                i = 0
                while i <= i1:
                    gui.text(150, 150, "Good match", fill="green", size=50)
                    i += 1
                flag1 = False
        elif column == 1 and row == 5:
            if not north and (not east) \
                    and south and west \
                    and add_blue and knot:
                draw_tile_win(x_coor, y_coor, north=False,
                              east=False, south=True, west=True,
                              add_blue=True, knot=True)
                gui.text(150, 150, "Good match", fill="green", size=50)
                i = 0
                while i <= i1:
                    gui.text(150, 150, "Good match", fill="green", size=50)
                    i += 1
                flag1 = False
        elif row == 5 and column != 1:
            if column == 5:
                if not north and east \
                        and south and not west \
                        and add_blue and knot:
                    draw_tile_win(x_coor, y_coor, north=False,
                                  east=True, south=True, west=False,
                                  add_blue=True, knot=True)
                    gui.text(150, 150, "Good match", fill="green", size=50)
                    i = 0
                    while i <= i1:
                        gui.text(150, 150, "Good match", fill="green", size=50)
                        i += 1
                    flag1 = False
            else:
                if not north and east \
                        and not south and west \
                        and not add_blue and not knot:
                    draw_tile_win(x_coor, y_coor, north=False,
                                  east=True, south=False, west=True,
                                  add_blue=False, knot=False)
                    gui.text(150, 150, "Good match", fill="green", size=50)
                    i = 0
                    while i <= i1:
                        gui.text(150, 150, "Good match", fill="green", size=50)
                        i += 1
                    flag1 = False
        elif column == 5 and row != 5:
            if row == 1:
                if north and east \
                        and not south and not west \
                        and add_blue and knot:
                    draw_tile_win(x_coor, y_coor, north=True,
                                  east=True, south=False, west=False,
                                  add_blue=True, knot=True)
                    gui.text(150, 150, "Good match", fill="green", size=50)
                    i = 0
                    while i <= i1:
                        gui.text(150, 150, "Good match", fill="green", size=50)
                        i += 1
                    flag1 = False
            else:
                if north and south \
                        and not east and not west \
                        and not add_blue and not knot:
                    draw_tile_win(x_coor, y_coor, north=True,
                                  east=False, south=True,
                                  west=False, add_blue=False, knot=False)
                    gui.text(150, 150, "Good match", fill="green", size=50)
                    i = 0
                    while i <= i1:
                        gui.text(150, 150, "Good match", fill="green", size=50)
                        i += 1
                    flag1 = False
        elif row == 1 and column != 5 and column != 1:
            if column == 2:
                if north and west \
                        and add_blue and knot \
                        and not south and not east:
                    draw_tile_win(x_coor, y_coor, north=True,
                                  east=False, south=False, west=True,
                                  add_blue=True, knot=True)
                    gui.text(150, 150, "Good match", fill="green", size=50)
                    i = 0
                    while i <= i1:
                        gui.text(150, 150, "Good match", fill="green", size=50)
                        i += 1
                    flag1 = False
            else:
                if not north and west \
                        and not add_blue and not knot \
                        and not south and east:
                    draw_tile_win(x_coor, y_coor, north=False,
                                  east=True, south=False, west=True,
                                  add_blue=False, knot=False)
                    gui.text(150, 150, "Good match", fill="green", size=50)
                    i = 0
                    while i <= i1:
                        gui.text(150, 150, "Good match", fill="green", size=50)
                        i += 1
                    flag1 = False
        elif column == 2 and row != 1 and row != 5:
            if row == 4:
                if not north and west \
                        and not add_blue and not knot \
                        and south and not east:
                    draw_tile_win(x_coor, y_coor, north=False,
                                  east=False, south=True, west=True,
                                  add_blue=True, knot=True)
                    gui.text(150, 150, "Good match", fill="green", size=50)
                    i = 0
                    while i <= i1:
                        gui.text(150, 150, "Good match", fill="green", size=50)  
                        i += 1
                    flag1 = False
            else:
                if north and west \
                        and not add_blue and not knot \
                        and south and not east:
                    draw_tile_win(x_coor, y_coor, north=True,
                                  east=False, south=True, west=False,
                                  add_blue=False, knot=False)
                    gui.text(150, 150, "Good match", fill="green", size=50)
                    i = 0
                    while i <= i1:
                        gui.text(150, 150, "Good match", fill="green", size=50)
                        i += 1
                    flag1 = False
        elif row == 4 and column == 3:
            if not north and west \
                    and not add_blue and not knot \
                    and not south and east:
                draw_tile_win(x_coor, y_coor, north=False,
                              east=True, south=False, west=True,
                              add_blue=False, knot=False)
                gui.text(150, 40, "Good match", fill="green", size=50)
                i = 0
                while i <= i1:
                    gui.text(150, 40, "Good match", fill="green", size=50)
                    i += 1
                flag1 = False
        elif row == 4 and column == 4:
            if not north and not west \
                    and add_blue and knot \
                    and south and east:
                draw_tile_win(x_coor, y_coor, north=False,
                              east=True, south=True, west=False,
                              add_blue=True, knot=True)
                gui.text(150, 40, "Good match", fill="green", size=50)
                i = 0
                while i <= i1:
                    gui.text(150, 40, "Good match", fill="green", size=50)
                    i += 1
                flag1 = False
        elif row == 3 and column == 4:
            if north and not west \
                    and not add_blue and not knot \
                    and south and not east:
                draw_tile_win(x_coor, y_coor, north=True,
                              east=False, south=True, west=False,
                              add_blue=False, knot=False)
                gui.text(150, 40, "Good match", fill="green", size=50)
                i = 0
                while i <= i1:
                    gui.text(150, 40, "Good match", fill="green", size=50)
                    i += 1
                flag1 = False
        elif row == 2 and column == 4:
            if north and not west \
                    and add_blue and knot \
                    and not south and east:
                draw_tile_win(x_coor, y_coor, north=True,
                              east=True, south=False, west=False,
                              add_blue=True, knot=True)
                gui.text(150, 40, "Good match", fill="green", size=50)
                i = 0
                while i <= i1:
                    gui.text(150, 40, "Good match", fill="green", size=50)
                    i += 1
                flag1 = False
        elif row == 2 and column == 3:
            if north and west \
                    and add_blue and knot \
                    and not south and not east:
                draw_tile_win(x_coor, y_coor, north=True,
                              east=False, south=False, west=True,
                              add_blue=True, knot=True)
                gui.text(150, 40, "Good match", fill="green", size=50)
                i = 0
                while i <= i1:
                    gui.text(150, 40, "Good match", fill="green", size=50)
                    i += 1
                flag1 = False
        elif row == 3 and column == 3:
            if not north and not west \
                    and add_blue and knot \
                    and south and not east:
                draw_tile_win(x_coor, y_coor, north=False,
                              east=False, south=True, west=False,
                              add_blue=True, knot=True)
                gui.text(150, 40, "Good match", fill="green", size=50)
                i = 0
                while i <= i1:
                    gui.text(150, 40, "Good match", fill="green", size=50)
                    i += 1
                flag1 = False
        gui.update_frame(200)


def main():
    # line 1
    draw_square(gui, 1, 1)
    draw_square(gui, 2, 1)
    draw_square(gui, 3, 1)
    draw_square(gui, 4, 1)
    draw_square(gui, 5, 1)

    draw_square(gui, 5, 2)
    draw_square(gui, 5, 3)
    draw_square(gui, 5, 4)
    draw_square(gui, 5, 5)

    draw_square(gui, 4, 5)
    draw_square(gui, 3, 5)
    draw_square(gui, 2, 5)
    draw_square(gui, 1, 5)

    draw_square(gui, 1, 4)
    draw_square(gui, 1, 3)
    draw_square(gui, 1, 2)

    draw_square(gui, 2, 2)
    draw_square(gui, 3, 2)
    draw_square(gui, 4, 2)

    draw_square(gui, 4, 3)
    draw_square(gui, 4, 4)
    draw_square(gui, 3, 4)
    draw_square(gui, 2, 4)
    draw_square(gui, 2, 3)
    draw_square(gui, 3, 3)


main()
