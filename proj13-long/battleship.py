""" File: battleship.py
    Author: Otabek Abduraimov
    Purpose: This program represents a board game in which two players
             try to shot ship on each others' boards. One person
             announces a target and the other player tells where that
             lands on their board: it may be a hit on a ship, perhaps
             leads it to sink, or a miss
    Course #: CS 120, Fall 2021
"""


class Board:
    """
    This class represents a Board, the size of which is
    self._size x self._size.
    It is responsible for
        1. Adding a ship on the board
        2. Printing the current state of the board
        3. Checking if the target has not been shot before
        4. Shooting at the target
    """

    def __init__(self, size):
        """
        :param size: the size of the board, which is a square
        self._coords_to_ships represents what each coord on the board
            contains, it could be a ship obj, a shot, a miss, or "."
        self._ship_to_shape represents what spaces the ship with some
            name takes on the board
        The constructor:
            sets the self._size to size,
            sets self._coords_to_ships dictionary to an empty dict
            sets self._ship_to_shape dictionary to an empty dict
        """
        assert size >= 0
        self._size = size
        self._coords_to_ships = {}  # {(x, y): ship_object}
        self._ship_to_shape = {}    # {"Battleship": [(0,0), (1,0), (2,0)]}

    def add_ship(self, ship, pos):
        """
        This one adds a ship obj onto the board
        :param ship: it represents the shape of the ship as
                     a list of (x,y) coords
        :param pos: (x, y) pos to insert the shi=
        """
        assert pos[0] <= self._size and pos[1] <= self._size
        assert pos not in self._coords_to_ships
        ship.set_ship_coords_on_board(pos)
        ship_real_coords = ship.get_ship_coords()

        for coord in ship_real_coords:
            self._coords_to_ships[coord] = ship

        self._ship_to_shape[ship.get_ship_name()] = ship_real_coords
        ship.set_ship_state()

    def print(self):
        """
        This one prints out the current state of the board
        with all the ships at their locations.
        What is on the board
            1. empty spaces never shot at -> .
            2. shot but a miss            -> o
            3. shot and a hit             -> *
            4. sunk ship                  -> X
            5. ship                       -> first letter of the ship
        """
        print((len(str(self._size-1)) + 1) * " " +
              "+" +
              "-" * ((self._size - 1) * 2 + 3) + "+")

        for i in range(self._size - 1, -1, -1):
            print(format(i, f"{len(str(self._size-1))}") + " |", end=" ")
            for j in range(self._size):
                curr_coord = (j, i)
                if curr_coord in self._coords_to_ships:
                    if self._coords_to_ships[curr_coord] == "o":
                        print("o", end=" ")
                    elif self._coords_to_ships[curr_coord] == "*":
                        print("*", end=" ")
                    elif self._coords_to_ships[curr_coord] == "X":
                        print("X", end=" ")
                    elif self._coords_to_ships[curr_coord] != ".":
                        # assert that self._coords_to_ships[curr_coord] is a ship obj
                        print(self._coords_to_ships[curr_coord].get_ship_name()[0].upper(),
                              end=" ")
                    else:
                        print(".", end=" ")
                else:
                    self._coords_to_ships[curr_coord] = "."
                    print(".", end=" ")
            print("|")
        print((len(str(self._size-1)) + 1) * " " +
              "+" +
              "-" * ((self._size - 1) * 2 + 3) + "+")

        if self._size <= 10:
            print(4 * " ", end="")
            for i in range(self._size):
                print(i, end=" ")
        else:
            for i in range(len(str(self._size))):
                print(5 * " ", end="")
                if i == 0:
                    for j in range(0, 10):
                        print(" ", end=" ")
                    for h in range(10, self._size):
                        print(str(h)[0], end=" ")
                    print()
                else:
                    for k in range(self._size):
                        print(str(k)[-1], end=" ")
        print()

    def has_been_used(self, pos):
        """
        This one checks if the position has already been shot at
        :param pos: (x,y) pos to check
        :return: Bool val, True if shot
                           False if not
        """
        assert pos[0] <= self._size and pos[1] <= self._size
        shot_signs = ["*", "o"]
        if self._coords_to_ships[pos] in shot_signs:
            return True
        return False

    def attempt_move(self, pos):
        """
        Handles the shot that is directed at the (x, y) pos
        :param pos: (x,y) pos to try shooting
        :return: ret_val == "Miss" or
                            "Hit (Ship Name)" or
                            "Hit"
        """
        assert pos[0] <= self._size and pos[1] <= self._size
        assert self.has_been_used(pos) is False

        if self._coords_to_ships[pos] == ".":
            self._coords_to_ships[pos] = "o"
            return "Miss"
        else:
            curr_ship = self._coords_to_ships[pos]
            curr_ship.update_ship_state(pos, "*")
            if curr_ship.is_sunk():
                for coord in curr_ship.get_ship_coords():
                    self._coords_to_ships[coord] = "X"
                return f"Sunk ({curr_ship.get_ship_name()})"
            else:
                self._coords_to_ships[pos] = "*"
                return "Hit"





class Ship:
    """
    This class creates a single ship object and rotates it
    if necessary.
    It is responsible for:
        1. Setting the name and shape of a ship
        2. Setting current state of the ship
        3. Updating the state of the ship
        4. Adjusting ship coords so they can be represented
                on the board
        5. Printing the current state of the ship
        6. Checking if the ship has sunk
        7. Rotating the ship objects
        8. Getting the ship name, shape, and ship coords
    """

    def __init__(self, name, shape):
        """
        1. Sets the ship name and shape
        2. Sets ship coords on the board to an empty list
        3. Sets the current ship state to an empty dict
        :param name: the name of the ship
        :param shape: a list of ordered (x,y) positions
        """
        self._name = name
        self._shape = shape
        self._ship_coords = []
        self._ship_state = {}



    def set_ship_state(self):
        """

        Sets the current state of the ship object to a dict
        with keys as ship coords and vals as
                                            1. First letter of the Ship
                                            2. Miss --> o
                                            3. Hit  --> *
        """
        for coord in self._ship_coords:
            self._ship_state[coord] = self._name[0].upper()

    def update_ship_state(self, pos, shot):
        """
        Updates the current state of the ship
        :param pos: (x, y) pos to change to a hit
        :param shot: "*" representing a shot
        """
        self._ship_state[pos] = shot

    def set_ship_coords_on_board(self, pos):
        """
        Adjusts the internal representation of the ship
        into a coords, so they can be represented on the board
        :param pos: pos on the board where the ship is to be placed
        """
        for coord in self._shape:
            x_coord = pos[0] + coord[0]
            y_coord = pos[1] + coord[1]
            self._ship_coords.append((x_coord, y_coord))

    def get_ship_coords(self):
        """
        Returns the board coords of the ship
        """
        return self._ship_coords

    def print(self):
        """
        Prints a single of input showing the state of the ship
        :return:
            1. * --> hit parts
            2. first letter --> not hit parts
        """
        ship_state_str = "".join(self._ship_state.values())
        print(format(ship_state_str, "10"), end="")
        print(self._name)

    def is_sunk(self):
        """
        Returns True if the Ship has been sunk (if all slots are hit)
                False if not
        """
        ship_state_str = "".join(self._ship_state.values())
        if len(self._ship_state) > 0:
            if ship_state_str.count("*") == len(self._ship_state):
                return True
        return False

    def rotate_once(self):
        """
        Rotates the ship by 90 degrees clockwise
        """
        rot_shape = []
        for coord in self._shape:
            coord = list(coord)
            coord[0], coord[1] = coord[1], -coord[0]
            coord = tuple(coord)
            rot_shape.append(coord)
        self._shape = rot_shape

    def rotate(self, amount):
        """
        Rotates the ship around the (0, 0) coord
        :param amount: units of 90 degrees of rotate clockwise
                       assert 0 <= amount <= 3
                       0 --> no rotate
                       1 --> 90 degrees
                       2 --> 180 degrees
                       3 --> 270 degrees
        """
        assert 0 <= amount <= 3, "invalid rotation val"
        for i in range(amount):
            self.rotate_once()

    def get_ship_name(self):
        """
        Returns the name of the ship object
        """
        return self._name

    def get_ship_shape(self):
        """
        Returns the internal representation of the
        shape of the ship object
        :return:
        """
        return self._shape



