""" File: twine.py
    Author: Otabek Abduraimov
    Purpose: This program tracks a lost person's
    path in a forest. It reads input from the user
    until it is stopped.
    It tells the user:
                      the current position
                      the start
                      the track
                      the obstacles
                      the map
                      how many times hey have been in a place
                      how far they have been from the start
    Unfortunately, it does not tell the user
    how to get out of the forest
    Course #: CS 120, Fall 2021
"""


def obstacles():
    """
    This function reads in a text file which
    includes the coordinates of obstacles.
    The text format is two ints per line.
    :return: list of tuples of two integers
    """
    obs_data = []
    flag = True
    while flag:
        obs_file = input("Please give the name of the \
                    obstacles filename, or - for none: ")
        if obs_file == "":
            print("ERROR: filename is blank")
        elif obs_file == "-":
            obs_data = []
            flag = False
        else:
            try:
                open_obs_file = open(obs_file, "r")
                for elem in open_obs_file:
                    elem = elem.strip()
                    try:
                        x = int(elem.split()[0])
                        y = int(elem.split()[1])
                        xy_tuple = (x, y)
                        obs_data.append(xy_tuple)
                    except ValueError:
                        print("ERROR: invalid data type")
                        flag = False
                flag = False
            except FileNotFoundError:
                print("ERROR: file not exists")
    return obs_data


def history():
    """
    This function reads continuously input from the user
    and prints out the details of the twine.
    The input can be: n(north), s(south), e(east), w(west),
                    back, crossings, ranges, map, or ""(blank line)
    It calls the appropriate function based on the input.
    :return: None
    """
    obs_data = obstacles()
    print()
    track = [(0, 0)]

    while True:
        cur_pos = track[-1]
        print(f"Current position: {cur_pos}")
        print(f"Your history:     {track}")
        print("What is your next command?")
        try:
            next_command = input()
        except EOFError:
            break

        if next_command == "n":
            next_move = north_move(track, obs_data)
            if next_move is not None:
                track.append(next_move)

        elif next_command == "e":
            next_move = east_move(track, obs_data)
            if next_move is not None:
                track.append(next_move)

        elif next_command == "s":
            next_move = south_move(track, obs_data)
            if next_move is not None:
                track.append(next_move)

        elif next_command == "w":
            next_move = west_move(track, obs_data)
            if next_move is not None:
                track.append(next_move)

        elif next_command == "back":
            track = back_move(track)

        elif next_command == "crossings":
            crossings(track)

        elif next_command == "map":
            track_map(track, obs_data)

        elif next_command == "ranges":
            ranges(track)

        elif next_command == "":
            print("You do nothing.")
        else:
            error_handler(next_command)
        print()


def north_move(track, obs_data):
    """
    This function takes two lists as params and
    if the north move (x+0, y+1) is not in the
    obstacles list (obs_data), it returns the north move
    as a tuple of x and y
    :param track: a list of tuples of x and y that
            shows the track of the person
    :param obs_data: a list of tuples of x and y that
                     shows which coordinates are blocked
    :return: a tuple of x and y that includes the north movement
    """
    cur_pos = track[-1]
    x = cur_pos[0]
    y = cur_pos[1] + 1
    move = (x, y)
    if move in obs_data:
        print("You could not move in that direction, \
                because there is an obstacle in the way.")
        print("You stay where you are.")
    else:
        return move


def east_move(track, obs_data):
    """
    This function takes two lists as params and
    if the east move (x+1, y+0) is not in the
    obstacles list (obs_data), it returns the east move
    as a tuple of x and y
    :param track: a list of tuples of x and y that
            shows the track of the person
    :param obs_data: a list of tuples of x and y that
                     shows which coordinates are blocked
    :return: a tuple of x and y that includes the east movement
    """
    cur_pos = track[-1]
    x = cur_pos[0] + 1
    y = cur_pos[1]
    move = (x, y)
    if move in obs_data:
        print("You could not move in that direction, \
                because there is an obstacle in the way.")
        print("You stay where you are.")
    else:
        return move


def south_move(track, obs_data):
    """
    This function takes two lists as params and
    if the south move (x+0, y-1) is not in the
    obstacles list (obs_data), it returns the south move
    as a tuple of x and y
    :param track: a list of tuples of x and y that
            shows the track of the person
    :param obs_data: a list of tuples of x and y that
                     shows which coordinates are blocked
    :return: a tuple of x and y that includes the south movement
    """
    cur_pos = track[-1]
    x = cur_pos[0]
    y = cur_pos[1] - 1
    move = (x, y)
    if move in obs_data:
        print("You could not move in that direction, \
                because there is an obstacle in the way.")
        print("You stay where you are.")
    else:
        return move


def west_move(track, obs_data):
    """
    This function takes two lists as params and
    if the west move (x-1, y+0) is not in the
    obstacles list (obs_data), it returns the west move
    as a tuple of x and y
    :param track: a list of tuples of x and y that
            shows the track of the person
    :param obs_data: a list of tuples of x and y that
                     shows which coordinates are blocked
    :return: a tuple of x and y that includes the west movement
    """
    cur_pos = track[-1]
    x = cur_pos[0] - 1
    y = cur_pos[1]
    move = (x, y)
    if move in obs_data:
        print("You could not move in that direction, \
                because there is an obstacle in the way.")
        print("You stay where you are.")
    else:
        return move


def back_move(track):
    """
    This one removes the last move from the track
    unless it has only one element, i.e the person
    is at the start
    :param track: a list of tuples of x and y that
            shows the track of the person
    :return: the updated version of track
    """
    if len(track) > 1:
        track.pop()
        print("You retrace your steps by one space")
    else:
        print("Cannot move back, as you're at the start!")
    return track


def crossings(track):
    """
    This function prints out how many times the user
    has been at a particular spot
    :param track: a list of tuples of x and y that
            shows the track of the person
    :return: None
    """
    count = 0
    cur_pos = track[-1]
    for elem in track:
        if elem == cur_pos:
            count += 1
    print(f"There have been {count} times in \
            the history when you were at this point.")


def track_map(track, obs_data):
    """
    This one shows the map of the twine with special chars.
    The map is 11x11.
    +: current position
    *: start
    .: the places where the user has been
    X: obstacles

    :param track: a list of tuples of x and y that
            shows the track of the person
    :param obs_data: a list of tuples of x and y that
                     shows which coordinates are blocked
    :return: None
    """
    coor_real = []
    for elem in track:
        x, y = (6 + elem[0]), (5 - elem[1])
        coor_real.append((x, y)
                         )
    cur_pos = coor_real[-1]
    obs_data_real = []
    for elem in obs_data:
        x, y = (6 + elem[0]), (5 - elem[1])
        obs_data_real.append((x, y))
    # print(obs_data_real)
    """
    the map format
    """
    print("+-----------+")
    for i in range(11):
        for j in range(13):
            coor_xy = (j, i)
            if j == 0 or j == 12:
                print("|", end="")
            elif coor_xy == cur_pos:
                print("+", end="")
            elif coor_xy == (6, 5):
                print("*", end="")
            elif coor_xy in obs_data_real:
                print("X", end="")
            elif coor_xy in coor_real:
                print(".", end="")
            else:
                print(" ", end="")
        print()
    print("+-----------+")


def ranges(track):
    """
    This function prints out the furthest West, North,
    South, and West the player has walked.
    :param track: a list of tuples of x and y that
            shows the track of the person
    :return: None
    """
    east_or_west_moves = []
    north_or_south_moves = []
    for elem in track:
        east_or_west_moves.append(elem[0])
        north_or_south_moves.append(elem[1])

    far_west = min(east_or_west_moves)
    if far_west > 0:
        far_west = 0
    print(f"The furthest West your twine goes is {far_west}")

    far_east = max(east_or_west_moves)
    if far_east < 0:
        far_east = 0
    print(f"The furthest East your twine goes is {far_east}")

    far_south = min(north_or_south_moves)
    if far_south > 0:
        far_south = 0
    print(f"The furthest South your twine goes is {far_south}")

    far_north = max(north_or_south_moves)
    if far_north < 0:
        far_north = 0
    print(f"The furthest North your twine goes is {far_north}")


def error_handler(next_command):
    """
    This one prints out an error message
    if the input of the user is not valid
    :param next_command: the input of the user
    :return: None
    """
    if len(next_command.split()) > 1:
        print("ERROR: command should be one word")
    else:
        print("ERROR: invalid command")


def main():
    history()

if __name__ == '__main__':
    main()

