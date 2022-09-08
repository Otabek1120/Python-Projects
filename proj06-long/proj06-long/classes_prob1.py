""" File: classes_prob1.py
    Author: Otabek Abduraimov
    Purpose: This function has three classes, all
             doing different jobs
             1. Simplest()
             2. Rotate()
             3. Band()

    Course #: CS 120, Fall 2021
"""


class Simplest:
    """
    This class takes three params
    and set them in public fields
    """
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c


class Rotate:
    """
    This class takes three values and rotates them
    in the round-robin fashion.
    It has the following methods:
        1. constructor: sets three private fields for the three vals
        2. get_first(), get_second(), get_third(): getters for the vals
        3. rotate(): for rotating the vals in the specified order
    """
    def __init__(self, first, second, third):
        self._first = first
        self._second = second
        self._third = third

    def get_first(self):
        return self._first

    def get_second(self):
        return self._second

    def get_third(self):
        return self._third

    def rotate(self):
        first_copy = self._first
        second_copy = self._second
        third_copy = self._third
        self._third, self._second, self._first = \
            first_copy, third_copy, second_copy


class Band:
    """
    This one represents a musical group, which
    has only one singer, one drummer, and some
    number of guitar players. It creates music
    based on the singer, drummer, and guitar players.
    :methods:
            1. constructor: it takes the name of the
                            singer and sets three private fields

            2. set_singer(new_singer): sets a new singer
            3. get_singer(): returns the name of the singer
            4. get_drummer(): returns the name of the drummer
            5. set_drummer(new_drummer): sets a new drummer
            6. add_guitar_player(new_guitar_player): add a new player
            7. fire_all_guitar_players(): removes all the guitar players
            8. get_guitar_players(): returns a copy of the list of guitar players
            9. play_music(): prints out tones of some music
    """
    def __init__(self, singer):
        self._singer = singer
        self._drummer = None
        self._guitar_players = []

    def set_singer(self, new_singer):
        self._singer = new_singer

    def get_singer(self):
        return self._singer

    def get_drummer(self):
        return self._drummer

    def set_drummer(self, new_drummer):
        self._drummer = new_drummer

    def add_guitar_player(self, new_guitar_player):
        self._guitar_players.append(new_guitar_player)

    def fire_all_guitar_players(self):
        self._guitar_players = []

    def get_guitar_players(self):
        return self._guitar_players[:]

    def play_music(self):
        if self._singer == "Frank Sinatra":
            print("Do be do be do")
        elif self._singer == "Kurt Cobain":
            print("bargle nawdle zouss")
        else:
            print("La la la")

        if self._drummer is not None:
            print("Bang bang bang!")

        for player in self._guitar_players:
            print("Strum!")








