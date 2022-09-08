""" File: classes_prob2.py
    Author: Otabek Abduraimov
    Purpose: This program gives the integer values
                and hexdecimal values for a color given

    Course #: CS 120, Fall 2021
"""


def rgb_vals(val):
    """
    :param val: an integer given by the caller
    :return: val
    This function sets the val to 255 if it is over 255
    or sets it to 0 if negative.
    """
    if val >= 255:
        val = 255
    elif val <= 0:
        val = 0
    return val


class Color:
    """
    This class represents an RGB color.
    It stores the red, green, and blue
    components of a color as ints.
    :methods:
            1. constructor(r,g,b): sets three
            private fields for r,g,b vals,
            each of which is in the range of [0, 255]
            2. html_hex_color(): encodes the vals
            it into hexdecimal chars
            3. get_rgb(): returns the rgb vals
            4. set_standard_color(name): takes
            the name of one of the four given
            colors and sets their rgb vals
            5. remove_red(): removes the r vals off
            the rgb vals
    """
    def __init__(self, r, g, b):
        self._r = rgb_vals(r)
        self._g = rgb_vals(g)
        self._b = rgb_vals(b)

    def __str__(self):
        return f"rgb({self._r},{self._g},{self._b})"

    def html_hex_color(self):
        return f"#{self._r:02X}{self._g:02X}{self._b:02X}"

    def get_rgb(self):
        return self._r, self._g, self._b

    def set_standard_color(self, name):
        if name.lower() == "black":
            self._r = self._g = self._b = 0
        elif name.lower() == "red":
            self._r = 255
            self._g = self._b = 0
        elif name.lower() == "yellow":
            self._r = self._g = 255
            self._b = 0
        elif name.lower() == "white":
            self._r = self._g = self._b = 255

    def remove_red(self):
        self._r = 0

