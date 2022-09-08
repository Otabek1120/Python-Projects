""" File: carcassonne_map.py
    Author: Otabek Abduraimov
    Purpose: This program creates a digital map of
        the tiles.
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


    def _get_next_tile(self, x, y, side):
        """
        :param x: x coord
        :param y: y coord
        :param side: one side of the current tile
        :return next_tile: the tile connected to the side
                x_coord:   x coord of the next tile
                y_coord:   y coord of the next tile
        This function gets the coords and the side of the
        curr tile and returns the adjacent tile and its
        coords
        """
        x_coor = x
        y_coor = y
        if side == 0:
            y_coor += 1
        elif side == 1:
            x_coor += 1
        elif side == 2:
            y_coor -= 1
        elif side == 3:
            x_coor -= 1
        next_tile = self.get(x_coor, y_coor)
        return next_tile, x_coor, y_coor

    def trace_road_one_direction(self, x, y, side):
        """
        :param x: x coord
        :param y: y coord
        :param side: the side we are leaving off the curr tile
        :return track: a list of the tuples which contains the
                       tile coord and the road connections
                       [(x_coord, y_coord, road_start, road_end)]
        This one tracks the road in one directions until there is
        a crossroad in the tile or there is no tile following.
        """
        track = []
        if not self.get(x, y).edge_has_road(side):
            return track
        next_tile = self._get_next_tile(x, y, side)[0]
        x_new = self._get_next_tile(x, y, side)[1]
        y_new = self._get_next_tile(x, y, side)[2]

        while next_tile is not None:
            opp_direct = CarcassonneTile.get_opp_direction(next_tile, side)
            if next_tile.has_crossroads():
                track.append((x_new, y_new, opp_direct, -1))
                return track
            else:
                road_connect = next_tile.road_get_connection(opp_direct)
                track.append((x_new, y_new, opp_direct, road_connect))
            next_tile = self._get_next_tile(x_new, y_new, road_connect)[0]
            x_new = self._get_next_tile(x_new, y_new, road_connect)[1]
            y_new = self._get_next_tile(x_new, y_new, road_connect)[2]
        return track


    def trace_road(self, x, y, side):
        """
        :param x: x coordd
        :param y: y coord
        :param side: the side to start tracking the road
        :return full path: a list of tuples of 4 vals which are
                           the tile coords, road start and road end
        This one does a similar job with trace_road_one_direction(),
        but it tracks the road in both directions.
        """
        current_tile = self.get(x, y)
        full_path = []
        one_side = self.trace_road_one_direction(x, y, side)
        connected_edge = current_tile.road_get_connection(side)
        the_other_side = self.trace_road_one_direction(x, y, connected_edge)

        the_other_side.reverse()
        for val in the_other_side:
            val = list(val)
            val[2], val[3] = val[3], val[2]
            full_path.append(tuple(val))

        current_track = (x, y, connected_edge, side)
        full_path.append(current_track)

        for track in one_side:
            full_path.append(track)
        return full_path


    def _trace_city_inter(self, x, y, side):
        """
        :param x: x coord
        :param y: y coord of the tile
        :param side: the side of the tile to start searching
        :return: a list of internal edges which has a city on it
        This helper function returns a list of tuples with three
        vals, which are the tile coords and the edge which has has
        a city.
        """
        ret_val = []
        curr_tile = self.get(x, y)
        if curr_tile is not None:
            north = curr_tile.city_connects(side, N)
            if north:
                ret_val.append((x, y, N))

            east = curr_tile.city_connects(side, E)
            if east:
                ret_val.append((x, y, E))

            south = curr_tile.city_connects(side, S)
            if south:
                ret_val.append((x, y, S))

            west = curr_tile.city_connects(side, W)
            if west:
                ret_val.append((x, y, W))

        return ret_val

    def _trace_city_adj(self, x, y, side):
        """
        :param x: x coord
        :param y: y coord
        :param side: the side to go for other tiles
        :return: (x, y, edge) which has a city on it
        This one finds out if the the side of the tile next to
        the side of the current tile has a city and if so,
        returns a tuple of the tile coords and the edge with a city.
        """
        curr_tile = self.get(x, y)
        if curr_tile is not None:
            adj_edge = curr_tile.get_opp_direction(side)
            adj_tile_info = self._get_next_tile(x, y, side)
            adj_tile = adj_tile_info[0]
            adj_tile_x = adj_tile_info[1]
            adj_tile_y = adj_tile_info[2]

            if adj_tile is not None and "city" in adj_tile.get_edge(adj_edge):
                return adj_tile_x, adj_tile_y, adj_edge

    def city_complete(self, city_trace):
        """
        :param city_trace: a list of tuples of all the city coords
                           and edges which has a city on them
        :return: It returns True if the city is complete and False if not
        This function finds if every edge of the cities has an adjacent
        city next to them.
        """
        ret_val = None
        for city in city_trace:
            next_tile = self._get_next_tile(city[0], city[1], city[2])[0]
            if next_tile is None:
                return False
            adj_edge = next_tile.get_opp_direction(city[2])
            if "city" not in next_tile.get_edge(adj_edge):
                return False
            else:
                ret_val = True
        return ret_val

    def trace_city(self, x, y, side):
        """
        This function searches from a given point, which is side here,
        and finds all the parts of the city and returns two vals:
        1. Coords and edges of the city parts as a tuples
        2. A bool val which indicates if the city is complete
        :param x: x coord
        :param y: y coord
        :param side: the location to start searching
        """
        city_trace = set()
        city_trace.add((x, y, side))

        found_smth_new = True
        while found_smth_new:
            found_smth_new = False

            city_trace_dup = list(city_trace)
            for item in city_trace_dup:
                city_internal = self._trace_city_inter(item[0], item[1], item[2])
                for city in city_internal:
                    if city not in city_trace:
                        city_trace.add(city)
                        found_smth_new = True

                city_adjacent = self._trace_city_adj(item[0], item[1], item[2])
                if city_adjacent is not None and city_adjacent not in city_trace:
                    city_trace.add(city_adjacent)
                    found_smth_new = True
        city_complete = self.city_complete(city_trace)
        return city_complete, city_trace

