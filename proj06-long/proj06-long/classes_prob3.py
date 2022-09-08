""" File: classes_prob3.py
    Author: Otabek Abduraimov
    Purpose: This program creates a grid of
                room objects with north, south, east, and west
                exits. It links them together in a way that
                the exit that takes you to another room can bring
                you back to the same room with the opposite exit.

    Course #: CS 120, Fall 2021
"""


class Room:
    """
    This class creates a room object with four
    exits, north, south, east, and west, which can be
    None.
    :methods:
            1. constructor: sets room name as private
            and the exit as public fields to None
            2. set_name(name): sets the name of the room object
            3. get_name(): returns the name of the room
            4. collapse(room): cut the links to the room and
            from the room to other rooms.
    """
    def __init__(self):
        self._room_name = None
        self.n = self.s = None
        self.e = self.w = None

    def set_name(self, name):
        self._room_name = str(name)

    def get_name(self):
        return self._room_name

    def collapse_room(self):
        if self.n is not None:
            self.n.s = None
            self.n = None
        if self.s is not None:
            self.s.n = None
            self.s = None
        if self.e is not None:
            self.e.w = None
            self.e = None
        if self.w is not None:
            self.w.e = None
            self.w = None


def build_grid(wid, hei):
    """
    :param wid: width of the grid (that is West-East size)
    :param hei: height of the grid (that is North-South size)
    :return: Room object in the South West corner
    This function creates a grid of Room objects
    and connects them symmetrically.
    """
    rooms_grid = []
    for i in range(hei):
        room_row = []
        for j in range(wid):
            room = Room()
            room_name = "room" + str(i) + str(j)
            room.set_name(room_name)
            room_row.append(room)
        rooms_grid.append(room_row)

    for room_row in rooms_grid:
        i = 0
        while i < len(rooms_grid[0])-1:
            room_row[i].e = room_row[i+1]
            room_row[i + 1].w = room_row[i]
            i += 1

    for i in range(hei-1):
        for j in range(wid):
            rooms_grid[i][j].n = rooms_grid[i+1][j]
            rooms_grid[i+1][j].s = rooms_grid[i][j]

    return rooms_grid[0][0]
