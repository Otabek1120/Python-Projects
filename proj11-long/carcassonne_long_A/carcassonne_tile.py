""" File: carcassonne_tile.py
    Author: Otabek Abduraimov
    Purpose: This program creates a single tile object,
        which has certain features on it, and it can
        be rotated to face any of the four directions
    Course #: CS 120, Fall 2021
"""


class CarcassonneTile:
    """
    This class creates a single tile object.
    """
    def __init__(self):
        """
        The constructor creates private north, south,
        east, west, and center variables and sets them
        to empty list
        """
        self._north, self._south, = [], []
        self._east, self._west = [], []
        self._center = []


    def get_opp_direction(self, side):
        """
        :param side: one of the four side: n, s, e, w
        :return: the direction facing the side as a corresponding int.
        """
        if side == 0:
            return 2
        elif side == 1:
            return 3
        elif side == 2:
            return 0
        elif side == 3:
            return 1


    def set_north(self, val):
        """
        :param val: a feature of the north side of the tile
        :return: None
        It adds a feature to the self._north
        """
        self._north.append(val)

    def set_south(self, val):
        """
        :param val: a feature of the south side of the tile
        :return: None
        It adds a feature to the self._south
        """
        self._south.append(val)

    def set_east(self, val):
        """
        :param val: a feature of the east side of the tile
        :return: None
        It adds a feature to the self._east
        """
        self._east.append(val)

    def set_west(self, val):
        """
        :param val: a feature of the west side of the tile
        :return: None
        It adds a feature to the self._west
        """
        self._west.append(val)

    def set_center(self, val):
        """

        :param val: a feature of the center of the tile
        :return: None
        It adds a feature to the self._center
        """
        self._center.append(val)


    def get_center(self):
        """
        :return: the features of the center of the tile
        as a str
        """
        return "".join(self._center)

    def get_edge(self, side):
        """
        :param side: one of the four side of the tile
        :return: what is on the side of the tile as a str
        This one tells what a side of the tile has.
        """
        if side == 0:
            return "+".join(sorted(self._north))
        if side == 1:
            return "+".join(sorted(self._east))
        if side == 2:
            return "+".join(sorted(self._south))
        if side == 3:
            return "+".join(sorted(self._west))

    def edge_has_road(self, side):
        """
        :param side: one of the four side of the tile
        :return: True if the edge has a road
                 False if not
        """
        if self.get_edge(side) is not None and \
                "road" in self.get_edge(side):
            return True
        return False

    def edge_has_city(self, side):
        """
        :param side: one of the four side of the tile
        :return: True if the edge has a city on it
                 False if not
        """
        if self.get_edge(side) is not None and\
                "city" in self.get_edge(side):
            return True
        return False

    def has_crossroads(self):
        """
        :return: True if there is an intersection
        on the tile or False if not.
        This one finds out if the tile has
        a crossroad on it.
        """
        if self.get_center() == "road":
            return True
        return False


    def road_get_connection(self, from_side):
        """
        :param from_side: one of the sides of the tile
        :return: an int corresponding to the side
        which is connected to from_side.
        This one finds if the given side is connected to any
        other side
        """
        if self.has_crossroads():
            return -1
        if from_side == 0:
            if self.edge_has_road(2):
                return 2
            elif self.edge_has_road(1):
                return 1
            elif self.edge_has_road(3):
                return 3
        if self.edge_has_road(self.get_opp_direction(from_side)):
            return self.get_opp_direction(from_side)
        if self.edge_has_road(from_side - 1):
            return from_side - 1
        if self.edge_has_road(from_side + 1):
            return from_side + 1

    def city_connects(self, sideA, sideB):
        """
        :param sideA: one of the sides of the tile which
        has a city on it
        :param sideB: one of the sides of the tile
        :return: True if cities are connected
                 False if not
        """
        if sideB == sideA:
            return True
        if self.get_edge(sideB) in self.get_edge(sideA):
            if self.get_center() == "city":
                return True
        return False


    def rotate(self):
        """
        :return new_tile: tile rotated 90 degrees clockwise
        This method rotates the tile 90 degrees
        clockwise.
        """
        new_tile = CarcassonneTile()
        for val in self._west:
            new_tile.set_north(val)
        for val in self._north:
            new_tile.set_east(val)
        for val in self._east:
            new_tile.set_south(val)
        for val in self._south:
            new_tile.set_west(val)
        for val in self._center:
            new_tile.set_center(val)
        return new_tile


N, E, S, W = 0, 1, 2, 3

tile01 = CarcassonneTile()
tile01.set_north("city")
tile01.set_east("grass")
tile01.set_east("road")
tile01.set_south("grass")
tile01.set_west("grass")
tile01.set_west("road")

tile02 = CarcassonneTile()
tile02.set_north("city")
tile02.set_east("city")
tile02.set_south("grass")
tile02.set_west("city")
tile02.set_center("city")

tile03 = CarcassonneTile()
tile03.set_north("grass")
tile03.set_north("road")
tile03.set_east("grass")
tile03.set_east("road")
tile03.set_south("grass")
tile03.set_south("road")
tile03.set_west("grass")
tile03.set_west("road")
tile03.set_center("road")


tile04 = CarcassonneTile()
tile04.set_north("city")
tile04.set_east("road")
tile04.set_east("grass")
tile04.set_south("road")
tile04.set_south("grass")
tile04.set_west("grass")

tile05 = CarcassonneTile()
tile05.set_north("city")
tile05.set_east("city")
tile05.set_south("city")
tile05.set_west("city")
tile05.set_center("city")

tile06 = CarcassonneTile()
tile06.set_north("grass")
tile06.set_north("road")
tile06.set_east("grass")
tile06.set_south("grass")
tile06.set_south("road")
tile06.set_west("grass")

tile07 = CarcassonneTile()
tile07.set_north("grass")
tile07.set_east("city")
tile07.set_south("grass")
tile07.set_west("city")
tile07.set_center("grass")

tile08 = CarcassonneTile()
tile08.set_north("grass")
tile08.set_east("city")
tile08.set_south("grass")
tile08.set_west("city")
tile08.set_center("city")

tile09 = CarcassonneTile()
tile09.set_north("city")
tile09.set_east("city")
tile09.set_south("grass")
tile09.set_west("city")
tile09.set_center("city")

tile10 = CarcassonneTile()
tile10.set_north("grass")
tile10.set_east("grass")
tile10.set_east("road")
tile10.set_south("grass")
tile10.set_south("road")
tile10.set_west("grass")
tile10.set_west("road")
tile10.set_center("road")

tile11 = CarcassonneTile()
tile11.set_north("city")
tile11.set_east("grass")
tile11.set_east("road")
tile11.set_south("grass")
tile11.set_south("road")
tile11.set_west("city")
tile11.set_center("city")

tile12 = CarcassonneTile()
tile12.set_north("city")
tile12.set_east("grass")
tile12.set_south("grass")
tile12.set_south("road")
tile12.set_west("grass")
tile12.set_west("road")

