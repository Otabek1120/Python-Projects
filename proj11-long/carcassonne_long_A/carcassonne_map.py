""" File: carcassonne_map.py
    Author: Otabek Abduraimov
    Purpose: This program creates a digital map of
        the tiles
    Course #: CS 120, Fall 2021
"""


from carcassonne_tile import *


class CarcassonneMap:
    """
    This class creates a map of the tiles and
    adds new tiles to the map.
    """
    def __init__(self):
        """
        The constructor creates a dictionary
        to map the coordinates of the tiles to
        the tiles. The tile at (0,0) is always tile01
        """
        self._coords_tiles = {(0, 0): tile01}

    def get_all_coords(self):
        """
        :return all_coords: the (x,y) coordinates of
        all the tiles in the map as a set
        """
        all_coords = set()
        for key in self._coords_tiles.keys():
            all_coords.add(key)
        return all_coords

    def find_map_border(self):
        """
        :param: None
        :return border_coords:  a set containing the
        coords of all the places in the map where
        new tiles can be added
        """
        border_coords = set()
        for coord in self._coords_tiles.keys():
            if (coord[0], coord[1]+1) not in self._coords_tiles.keys():
                border_coords.add((coord[0], coord[1]+1))
            if (coord[0]+1, coord[1]) not in self._coords_tiles.keys():
                border_coords.add((coord[0]+1, coord[1]))
            if (coord[0], coord[1]-1) not in self._coords_tiles.keys():
                border_coords.add((coord[0], coord[1]-1))
            if (coord[0]-1, coord[1]) not in self._coords_tiles.keys():
                border_coords.add((coord[0]-1, coord[1]))
        return border_coords

    def get(self, x, y):
        """
        :param x: x coord of the tile
        :param y: y coord of the tile
        :return: the tile at the (x,y) coord if there is one.
                 If not, it returns None
        This one finds out if there is a tile in the map
        at the (x,y) location
        """
        if (x, y) in self._coords_tiles.keys():
            return self._coords_tiles[(x, y)]
        return None

    def _add(self, x, y, tile):
        """
        This helper function checks if the given
        tile can be added at the (x,y) location.
        It returns True if the given tile matches the
        adjacent tile and False if not
        :param x: x coord of the tile
        :param y: y coord of the tile
        :param tile: a new tile to be added
        :return:
        """
        ret_val = []
        if (x, y) in self._coords_tiles.keys():
            return False
        elif (x, y) not in self.find_map_border():
            return False
        else:
            if (x, y + 1) in self._coords_tiles.keys():
                if tile.get_edge(N) == self._coords_tiles[(x, y + 1)].get_edge(S):
                    ret_val.append(True)
                else:
                    return False
            else:
                ret_val.append(True)

            if (x + 1, y) in self._coords_tiles.keys():
                if tile.get_edge(E) == self._coords_tiles[(x + 1, y)].get_edge(W):
                    ret_val.append(True)
                else:
                    return False
            else:
                ret_val.append(True)

            if (x, y - 1) in self._coords_tiles.keys():
                if tile.get_edge(S) == self._coords_tiles[(x, y - 1)].get_edge(N):
                    ret_val.append(True)
                else:
                    return False
            else:
                ret_val.append(True)

            if (x - 1, y) in self._coords_tiles.keys():
                if tile.get_edge(W) == self._coords_tiles[(x - 1, y)].get_edge(E):
                    ret_val.append(True)
                else:
                    return False
            else:
                ret_val.append(True)
        return len(ret_val) == 4

    def add(self, x, y, tile, confirm=True, tryOnly=False):
        """
        This one adds the tile if tryOnly is False. If the tryOnly
        is True it only checks if the tile can be added or not and returns
        a bool value. When confirm is True, it checks if the tile is
        matching the requirements of the map
        :param x: x coord of the new tile
        :param y: y coord of the new tile
        :param tile: new tile to be added
        :param confirm: bool val for error checking the tile
        :param tryOnly: bool val for adding the tile
        :return:
        """
        ret_val = self._add(x, y, tile)
        if not ret_val:
            return False
        if confirm and not tryOnly:
            self._coords_tiles[(x, y)] = tile
            return True
        elif confirm and tryOnly:
            return True
        elif not confirm and not tryOnly:
            self._coords_tiles[(x, y)] = tile
            return True
