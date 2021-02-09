from adventurer import Adventurer
from dungeon import Dungeon
from room import Room


"""DungeonAdventure holds the logic of playing the game.  Re/starts game, creates
adventurer and dungeon through respective classes, controls user input/options,
and logic for winning game"""


def start_game():
    """This method starts the game.  Provides an introduction and how to play guide.
    It also kicks off the game with character creation and dungeon / difficulty."""
    intro()
    how_to_play()
    adventurer = create_player()
    dungeon = difficulty()
    play(dungeon, adventurer)


def restart_game():
    """This method restarts the game without intro / how to play guide."""
    adventurer = create_player()
    dungeon = difficulty()
    play(dungeon, adventurer)


def play(dungeon, adventurer):
    """This method holds the logic for playing the game."""
    print_room(dungeon)
    user_input(dungeon, adventurer)
    hidden_menu()
    # print_dungeon()
    game_over()


def intro():
    """This method provides an overview of the game"""
    print("Welcome to the Dungeon of Doom!  Prepare for the most difficult \n"
          "challenge of your adventure-seeking life.  Check your pride at the door,\n"
          "and bring an extra ounce of courage as you face off against countless\n"
          "pits and race against your own agony to capture the elusive....... \n\n"
          "*****  Four Pillars of Object-Oriented Programming *****\n")


def how_to_play():
    """This method describes the goal of the game, how to win, and the objects
    encountered during the game"""
    print("The goal of this game is to escape the dungeon maze after finding the\n"
          "four pillars:\n"
          "   1: Abstraction\n"
          "   2: Encapsulation\n"
          "   3: Inheritance\n"
          "   4: Polymorphism\n\n"

          "Be warned - you have limited health points [HP]. If you fall in a pit, you\n"
          "will lose HP. Don't fret - there are also Healing Potions and Vision\n"
          "Potions scattered about the dungeon to help you in your quest. Once you\n"
          "collect all Four Pillars of OO, the exit door will unlock --- if you reach\n"
          "the exit before your HP reaches a big fat zero, you win!\n\n"
          "Move throughout the map by typing \'u\', \'d\', \'l\', or \'r\'\n"
          "You can only move through the doors that exist in the dungeon.\n\n"
          "Check the status of your adventurer by typing \'s\'.\n\n"
          "Be strong in your journey...\n\"Even death is not to be feared by one who "
          "has lived wisely\" --- Buddha\n")


def create_player():
    """This method asks user for Character Name input. This should reference the
    Adventurer Class"""
    player_name = input("Welcome to the bridge of death... What is your name?: ")
    return Adventurer(player_name)


def difficulty():
    """This method will define the size of the dungeon array.  1 = 3x3, 2 = 5x5, 3 = 6x6"""
    low = 1
    high = 5
    level = int(input("What is your quest? Enter a difficulty from 1 (Easy) to 5 (Hard): "))
    if low <= level <= high:
        # create dungeon by array size based on level input
        if level == 1:
            nx, ny = 5, 5
        if level == 2:
            nx, ny = 6, 6
        if level == 3:
            nx, ny = 7, 7
        if level == 4:
            nx, ny = 8, 8
        if level == 5:
            nx, ny = 10, 10
        ix, iy = 0, 0
        game_board = Dungeon(nx, ny, ix, iy)
        game_board.make_dungeon()
        game_board.place_dungeon_items()
        while game_board.traverse() is not True:
            game_board.make_dungeon()
            game_board.place_dungeon_items()
        print(game_board)
        return game_board
    else:
        print("\n\"Ahhhhhhhhhhhhh\" (That's the sound of you being thrown into "
              "the gorge because you didn't enter an integer between 1-5.)  Game over.\n")
        input("Press Enter to restart game...")
        restart_game()


def print_room(dungeon):
    """ prints the dungeon as a visual """
    x, y = dungeon.current_room()

    def print_top_row(row, col):
        # print top row
        room = dungeon.room_at(row, col)

        print("*", end='')
        if col == 0:
            print("*", end='')
        else:  # it's not border
            if room.has_north_wall():
                print("-", end='')
            else:
                print(" ", end='')
        print("*")

    def print_mid_row(row, col):
        # print middle row
        room = dungeon.room_at(row, col)

        if row == 0:
            print("*", end='')
        else:  # it's not border
            if room.has_west_wall():
                print("|", end='')
            else:
                print(" ", end='')

        print(room.get_letter(), end='')

        if row == int(dungeon.get_nx() - 1):
            print("*")
        else:  # it's not border
            if room.has_east_wall():
                print("|")
            else:
                print(" ")

    def print_bot_row(row, col):
        # print third row
        room = dungeon.room_at(row, col)

        print("*", end='')
        if col == (int(dungeon.get_ny()) - 1):
            print("*", end='')
        else:
            if room.has_south_wall():
                print("-", end='')
            else:
                print(" ", end='')
        print("*")

    print_top_row(x, y)
    print_mid_row(x, y)
    print_bot_row(x, y)


def show_vision_map(dungeon):
    x, y = dungeon.current_room()

    def print_first_row(row, col):
        if col == 0:
            print("       ")
            return
        if col > 0 and row == 0:
            print("  *", end='')
            # move to room 2
            dungeon.move_to(row, col - 1)  # up one col from initial room
            row, col = dungeon.current_room()
            room = dungeon.room_at(row, col)
            if col == 0:
                print("**", end='')
            elif room.has_north_wall():
                print("-*", end='')
            else:
                print(" *", end='')
            # room 3 (assuming an array of 3 or more cols)
            dungeon.move_to((row + 1), col)
            row, col = dungeon.current_room()
            room = dungeon.room_at(row, col)
            if col == 0:
                print("**")
            elif room.has_north_wall():
                print("-*")
            else:
                print(" *")
        else:
            # room 1
            dungeon.move_to((row - 1), col - 1)
            row, col = dungeon.current_room()
            room = dungeon.room_at(row, col)
            print("*", end='')
            if col == 0:
                print("*", end='')
            elif room.has_north_wall():
                print("-", end='')
            else:
                print(" ", end='')
            print("*", end='')
            # room 2
            dungeon.move_to((row + 1), col)
            row, col = dungeon.current_room()
            room = dungeon.room_at(row, col)
            if col == 0:
                print("*", end='')
            elif room.has_north_wall():
                print("-", end='')
            else:
                print(" ", end='')
            print("*", end='')
            # room 3
            dungeon.move_to((row + 1), col)
            row, col = dungeon.current_room()
            # case if out of bounds to right
            if row == dungeon.get_nx():
                print("  ")
            else:
                room = dungeon.room_at(row, col)
                if col == 0:
                    print("*", end='')
                elif room.has_north_wall():
                    print("-", end='')
                else:
                    print(" ", end='')
                print("*")

    def print_second_row(row, col):
        if col == 0:
            print("       ")
            return
        if col > 0 and row == 0:
            print("  *", end='')
            # move to room 2, up from initial room
            dungeon.move_to(row, col - 1)
            row, col = dungeon.current_room()
            room = dungeon.room_at(row, col)
            print(room.get_letter(), end='')
            if room.has_east_wall():
                print("|", end='')
            else:
                print(" ", end='')
            # room 3 (assuming an array of more than 3 cols)
            dungeon.move_to((row + 1), col)
            row, col = dungeon.current_room()
            room = dungeon.room_at(row, col)
            print(room.get_letter(), end='') #
            if row == dungeon.get_nx():
                print("*")
            elif room.has_east_wall():
                print("|")
            else:
                print(" ")
        else:
            # room 1
            dungeon.move_to((row - 1), col - 1)
            row, col = dungeon.current_room()
            room = dungeon.room_at(row, col)

            if row == 0:  # edge of dungeon - doesn't work for some reason
                print("*", end='')
            elif room.has_west_wall():
                print("|", end='')
            else:
                print(" ", end='')
            print(room.get_letter(), end='')
            if room.has_east_wall():
                print("|", end='')
            else:
                print(" ", end='')
            # room 2
            dungeon.move_to((row + 1), col)
            row, col = dungeon.current_room()
            room = dungeon.room_at(row, col)
            print(room.get_letter(), end='')
            temp = int(dungeon.get_nx())
            if row == temp - 1:
                print("*", end='')
            elif room.has_east_wall():
                print("|", end='')
            else:
                print(" ", end='')
            # room 3
            dungeon.move_to((row + 1), col)
            row, col = dungeon.current_room()
            # case if out of bounds to right
            if row == dungeon.get_nx():
                print("  ")
            else:
                room = dungeon.room_at(row, col)
                print(room.get_letter(), end='')
                a = int(dungeon.get_nx())
                if row == a - 1:
                    print("*")
                elif room.has_east_wall():
                    print("|")
                else:
                    print(" ")

    def print_third_row(row, col):
        if row == 0 and col == 0:
            # top left corner
            print("  *****")
        elif col == 0 and row > 0:
            # top row excluding left corner
            print("*****", end='')
            # move to right room
            dungeon.move_to((row + 1), col)
            row, col = dungeon.current_room()
            # if room doesn't exist
            if row == dungeon.get_nx():
                print("  ")
            else:
                print("**")
        elif col > 0 and row == 0:
            # first column
            print("  *", end='')
            # room 2
            # row, col = dungeon.current_room()
            room = dungeon.room_at(row, col)
            if room.has_north_wall():  # error?
                print("-", end='')
            else:
                print(" ", end='')
            print("*", end='')
            # room 3 (assuming an array of 3 or more cols)
            dungeon.move_to((row + 1), col)
            row, col = dungeon.current_room()
            room = dungeon.room_at(row, col)
            if room.has_north_wall():
                print("-", end='')
            else:
                print(" ", end='')
            print("*")
        else:
            # room 1 (move left 1 room)
            dungeon.move_to((row - 1), col)
            row, col = dungeon.current_room()
            room = dungeon.room_at(row, col)
            print("*", end='')
            if col == 0:
                print("*", end='')
            elif room.has_north_wall():
                print("-", end='')
            else:
                print(" ", end='')
            print("*", end='')
            # room 2 (was the initial room)
            dungeon.move_to((row + 1), col)
            row, col = dungeon.current_room()
            room = dungeon.room_at(row, col)
            if room.has_north_wall():
                print("-", end='')
            else:
                print(" ", end='')
            print("*", end='')
            # room 3
            dungeon.move_to((row + 1), col)
            row, col = dungeon.current_room()
            # case if out of bounds to right
            if row == dungeon.get_nx():
                print("  ")
            else:
                room = dungeon.room_at(row, col)
                if room.has_north_wall():
                    print("-", end='')
                else:
                    print(" ", end='')
                print("*")

    def print_fourth_row(row, col):
        # top left corner
        if col == 0 and row == 0:
            # first room
            print("  *", end='')
            # second room
            room = dungeon.room_at(row, col)
            print(room.get_letter(), end='')
            if room.has_east_wall():
                print("|", end='')
            else:
                print(" ", end='')
            # third room
            dungeon.move_to((row + 1), col)
            row, col = dungeon.current_room()
            room = dungeon.room_at(row, col)
            print(room.get_letter(), end='')
            if room.has_east_wall():
                print("|")
            else:
                print(" ")
        elif col > 0 and row == 0:  # (west dungeon border) assume array >= than 3
            print("  *", end='')
            room = dungeon.room_at(row, col)
            print(room.get_letter(), end='')
            if room.has_east_wall():
                print("|", end='')
            else:
                print(" ", end='')
            dungeon.move_to((row + 1), col)
            row, col = dungeon.current_room()
            room = dungeon.room_at(row, col)
            print(room.get_letter(), end='')
            if room.has_east_wall():
                print("|")
            else:
                print(" ")
        else:  # room not at row 0 (east dungeon border)
            # room 1 to left
            dungeon.move_to((row - 1), col)
            row, col = dungeon.current_room()
            room = dungeon.room_at(row, col)
            if row == 0:  # edge of dungeon - doesn't work for some reason
                print("*", end='')
            elif room.has_west_wall():
                print("|", end='')
            else:
                print(" ", end='')
            print(room.get_letter(), end='')
            if room.has_east_wall():
                print("|", end='')
            else:
                print(" ", end='')
            # room 2 (initial room)
            dungeon.move_to((row + 1), col)
            row, col = dungeon.current_room()
            room = dungeon.room_at(row, col)
            print(room.get_letter(), end='')
            temp = int(dungeon.get_nx())
            if row == temp - 1:
                print("*", end='')
            elif room.has_east_wall():
                print("|", end='')
            else:
                print(" ", end='')
            # room 3 (right room)
            dungeon.move_to((row + 1), col)
            row, col = dungeon.current_room()
            #temp = int(dungeon.get_nx())
            if row == dungeon.get_nx():
                print("  ")

            else:
                room = dungeon.room_at(row, col)
                print(room.get_letter(), end='')
                temp = int(dungeon.get_nx())
                if row == temp - 1:
                    print("*")
                elif room.has_east_wall():
                    print("|")
                else:
                    print(" ")

    def print_fifth_row(row, col):
        # temp = int(dungeon.get_ny())
        # room at bottom left corner
        if row == 0 and col == int(dungeon.get_ny()) - 1:
            print("  *****")
        # room at bottom right corner
        elif row == (int(dungeon.get_nx()) - 1) and col == (int(dungeon.get_ny()) - 1):
            print("*****  ")
        # room on bottom row
        elif col == (int(dungeon.get_ny()) - 1):
            print("*******")
        else:
            # room bordering west dungeon border
            if row == 0:
                print("  *", end='')
                # row, col = dungeon.current_room()  # bug fix hash?
                room = dungeon.room_at(row, col)
                if room.has_south_wall():  # bug?
                    print("-*", end='')
                else:
                    print(" *", end='')
                dungeon.move_to((row + 1), col)
                row, col = dungeon.current_room()
                room = dungeon.room_at(row, col)
                if room.has_south_wall():
                    print("-*")
                else:
                    print(" *")
            # room bordering east dungeon border
            elif row == int(dungeon.get_nx() - 1):
                print("*", end='')
                # first room (to left)
                dungeon.move_to((row -1), col)
                row, col = dungeon.current_room()
                room = dungeon.room_at(row, col)
                if room.has_south_wall():
                    print("-*", end='')
                else:
                    print(" *", end='')
                dungeon.move_to((row + 1), col)
                row, col = dungeon.current_room()
                room = dungeon.room_at(row, col)
                if room.has_south_wall():
                    print("-*", end='')
                else:
                    print(" *", end='')
                print("  ")
            else:
                # no dungeon borders
                print("*", end='')
                # first room (to left)
                dungeon.move_to((row - 1), col)
                row, col = dungeon.current_room()
                room = dungeon.room_at(row, col)
                if room.has_south_wall():
                    print("-*", end='')
                else:
                    print(" *", end='')
                dungeon.move_to((row + 1), col)
                row, col = dungeon.current_room()
                room = dungeon.room_at(row, col)
                if room.has_south_wall():
                    print("-*", end='')
                else:
                    print(" *", end='')
                dungeon.move_to((row + 1), col)
                row, col = dungeon.current_room()
                room = dungeon.room_at(row, col)
                if room.has_south_wall():
                    print("-*")
                else:
                    print(" *")

    def print_sixth_row(row, col):
        # room on bottom row
        if col == (int(dungeon.get_ny()) - 1):
            print("       ")
        # room on west dungeon border
        elif row == 0:  # assumes array larger than 3
            print("  *", end='')
            # move down a room
            dungeon.move_to(row, (col + 1))
            row, col = dungeon.current_room()
            room = dungeon.room_at(row, col)
            print(room.get_letter(), end='')
            if room.has_east_wall():
                print("|", end='')
            else:
                print(" ", end='')
            # move right a room
            dungeon.move_to(row + 1, col)
            row, col = dungeon.current_room()
            room = dungeon.room_at(row, col)
            print(room.get_letter(), end='')
            if room.has_east_wall():
                print("|", end='')
            else:
                print(" ")

        elif row == 1:  # assumes array larger than 3
            print("*", end='')
            # room 1 move down, to left
            dungeon.move_to((row - 1), (col + 1))
            row, col = dungeon.current_room()
            room = dungeon.room_at(row, col)
            print(room.get_letter(), end='')
            if room.has_east_wall():
                print("|", end='')
            else:
                print(" ", end='')
            # room 2 move right a room
            dungeon.move_to(row + 1, col)
            row, col = dungeon.current_room()
            room = dungeon.room_at(row, col)
            print(room.get_letter(), end='')
            if room.has_east_wall():
                print("|", end='')
            else:
                print(" ", end='')
            # room 3 move right a room
            dungeon.move_to(row + 1, col)
            row, col = dungeon.current_room()
            room = dungeon.room_at(row, col)
            print(room.get_letter(), end='')
            if room.has_east_wall():
                print("|")
            else:
                print(" ")
            # room bordering east dungeon border
        elif row == int(dungeon.get_nx() - 1):
            # first room (down one, left one)
            dungeon.move_to((row -1), (col + 1))
            row, col = dungeon.current_room()
            room = dungeon.room_at(row, col)
            if room.has_west_wall():
                print("|", end='')
            else:
                print(" ", end='')
            print(room.get_letter(), end='')
            dungeon.move_to((row + 1), col)
            row, col = dungeon.current_room()
            room = dungeon.room_at(row, col)
            if room.has_west_wall():
                print("|", end='')
            else:
                print(" ", end='')
            print(room.get_letter(), end='')
            print("*  ")
        # second from last row, shows east dungeon border
        elif row == int(dungeon.get_nx() - 2):
            # first room (down one, left one)
            dungeon.move_to((row -1), (col + 1))
            row, col = dungeon.current_room()
            room = dungeon.room_at(row, col)
            if room.has_west_wall():
                print("|", end='')
            else:
                print(" ", end='')
            print(room.get_letter(), end='')
            # second room
            dungeon.move_to((row + 1), col)
            row, col = dungeon.current_room()
            room = dungeon.room_at(row, col)
            if room.has_west_wall():
                print("|", end='')
            else:
                print(" ", end='')
            print(room.get_letter(), end='')
            if room.has_east_wall():
                print("|", end='')
            else:
                print(" ", end='')
            # third room
            dungeon.move_to((row + 1), col)
            row, col = dungeon.current_room()
            room = dungeon.room_at(row, col)
            print(room.get_letter(), end='')
            print("*")

        else:
            # middle rooms
            # first room (down one, left one)
            dungeon.move_to((row - 1), (col + 1))
            row, col = dungeon.current_room()
            room = dungeon.room_at(row, col)
            if room.has_west_wall():
                print("|", end='')
            else:
                print(" ", end='')
            print(room.get_letter(), end='')
            # second room
            dungeon.move_to((row + 1), col)
            row, col = dungeon.current_room()
            room = dungeon.room_at(row, col)
            if room.has_west_wall():
                print("|", end='')
            else:
                print(" ", end='')
            print(room.get_letter(), end='')
            if room.has_east_wall():
                print("|", end='')
            else:
                print(" ", end='')
            # third room
            dungeon.move_to((row + 1), col)
            row, col = dungeon.current_room()
            room = dungeon.room_at(row, col)
            print(room.get_letter(), end='')
            if room.has_east_wall():
                print("|")
            else:
                print(" ")

    def print_seventh_row(row, col):
        # room on bottom row
        if col == (int(dungeon.get_ny()) - 1):
            print("       ")
        # print dungeon border
        elif col == (int(dungeon.get_ny()) - 2) and row == 0:
            print("  *****")
        elif col == (int(dungeon.get_ny()) - 2) and row == (int(dungeon.get_nx()) -1):
            print("*****  ")
        elif row == 0:
            print("  *", end='')
            # first room (down one)
            dungeon.move_to(row, (col + 1))
            row, col = dungeon.current_room()
            room = dungeon.room_at(row, col)
            if room.has_south_wall():
                print("-*", end='')
            else:
                print(" *", end='')
            # second room
            dungeon.move_to((row + 1), col)
            row, col = dungeon.current_room()
            room = dungeon.room_at(row, col)
            if room.has_south_wall():
                print("-*")
            else:
                print(" *")
        elif row == (int(dungeon.get_nx()) -1):
            print("*", end='')
            # first room (down one, left one)
            dungeon.move_to((row - 1), (col + 1))
            row, col = dungeon.current_room()
            room = dungeon.room_at(row, col)
            if room.has_south_wall():
                print("-*", end='')
            else:
                print(" *", end='')
            # second room (room to the right)
            dungeon.move_to((row + 1), col)
            row, col = dungeon.current_room()
            room = dungeon.room_at(row, col)
            if room.has_south_wall():
                print("-*  ")
            else:
                print(" *  ")
        else:
            (print("*", end=''))
            # first room (down one, left one)
            dungeon.move_to((row - 1), (col + 1))
            row, col = dungeon.current_room()
            room = dungeon.room_at(row, col)
            if room.has_south_wall():
                print("-*", end='')
            else:
                print(" *", end='')
            # second room
            dungeon.move_to((row + 1), col)
            row, col = dungeon.current_room()
            room = dungeon.room_at(row, col)
            if room.has_south_wall():
                print("-*", end='')
            else:
                print(" *", end='')
            # third room
            dungeon.move_to((row + 1), col)
            row, col = dungeon.current_room()
            room = dungeon.room_at(row, col)
            if room.has_south_wall():
                print("-*")
            else:
                print(" *")

    print_first_row(x, y)
    print_second_row(x, y)
    print_third_row(x, y)
    print_fourth_row(x, y)
    print_fifth_row(x, y)
    print_sixth_row(x, y)
    print_seventh_row(x, y)


def user_input(dungeon, adventurer):
    """This method will allow the user to perform a set of tasks based on the room and
    inventory the adventurer holds:  Move, use healing/vision potion, view inventory, give up"""
    keystroke = input("What would you like to do? Press \"1\" for all options: ")
    # print all options

    player = adventurer
    x, y = dungeon.current_room()
    room = dungeon.room_at(x, y)
    if keystroke == "1":
        options = []
        if dungeon.is_valid_room(x, y) is True and room.has_north_wall() is False:
            options.append("u")
        if dungeon.is_valid_room(x, y) is True and room.has_south_wall() is False:
            options.append("d")
        if dungeon.is_valid_room(x, y) is True and room.has_east_wall() is False:
            options.append("r")
        if dungeon.is_valid_room(x, y) is True and room.has_west_wall() is False:
            options.append("l")
        if adventurer.has_healing_potion is > 0:
            options.append("h")
        if adventurer.has_vision_potion is True:
            options.append("v")
        # View Status
        options.append("s")
        options.append("q")
        print(options)
        print_room(dungeon)
        user_input(dungeon, adventurer)

    # quit option
    elif keystroke == "q":
        a = input("Temptation to quit is the greatest just before you are about "
                  "to succeed.\nDo you really want to give up? (y or n): ")
        if a == "y":
            print("\nThere is a difference between giving up and knowing when you had enough.\n\n"
                  "Better luck next time.  Game over.\n")
            input("Press Enter to restart or exit the game.")
            restart_game()
        elif a == "n":
            print_room(dungeon)
            user_input(dungeon, adventurer)
        else:
            print("That is not a valid command. Try again.")
    # move adventurer
    elif keystroke == "u":
        # need to validate if it is possible to move up
        # if it is not possible then use the keyword break
        x, y = dungeon.current_room()
        if dungeon.is_valid_room(x, y) is True and room.has_north_wall() is False:
            dungeon.move_to(x, y - 1)
        else:
            print("That is not a valid command.  Try again. ")
    elif keystroke == "d":
        x, y = dungeon.current_room()
        if dungeon.is_valid_room(x, y) is True and room.has_south_wall() is False:
            dungeon.move_to(x, y + 1)
        else:
            print("That is not a valid command.  Try again. ")
    elif keystroke == "l":
        x, y = dungeon.current_room()
        if dungeon.is_valid_room(x, y) is True and room.has_west_wall() is False:
            dungeon.move_to(x - 1, y)
        else:
            print("That is not a valid command.  Try again. ")
    elif keystroke == "r":
        x, y = dungeon.current_room()
        if dungeon.is_valid_room(x, y) is True and room.has_east_wall() is False:
            dungeon.move_to(x + 1, y)
        else:
            print("That is not a valid command.  Try again. ")

    elif keystroke == "s":
        print("Status:")
        print(player)
        print_room(dungeon)
        user_input(dungeon, adventurer)
    # use healing potion
    elif keystroke == "h":
        adventurer.use_healing_potion()
    # use vision potion
    elif keystroke == "v":
        adventurer.use_vision_potion()

    # hidden menu item to show map
    elif keystroke == "map":
        print(dungeon)
    else:
        print("That is not a valid command.  Try again. ")
        print_room(dungeon)
    # prints new room, then prompts for next user input

    # discover_room() # will pick up potion, discover pillar, or hurt you via pit
    # check for pick_up healing potion if....
    # check for pick up vision if...
    # check for pit, hurt if so...

    print_room(dungeon)
    user_input(dungeon, adventurer)


def print_dungeon(dungeon):
    print(dungeon)


def game_over(dungeon):
    """This method determines the end of the game --- 1) LOSE if hero runs out of HP
     2) WIN if the adventurer collects all four pillars and finds the exit."""
    if Adventurer.is_alive is False:
        print("It is not just a flesh wound this time.  You died.")
        print(dungeon)
        roll_credits()
        input("Press Enter to restart game...")
        restart_game()
    if Adventurer.all_pillars_found:
        if Room.is_exit:
            print("Horace Mann once said, \"Be ashamed to die until you have "
                  "won some victory for humanity.\"  And today, you won!\n\n"
                  "Congratulations!  You defeated the Dungeon of Doom!\n\n")
            print(dungeon)
            roll_credits()

def roll_credits():
    print("Created by Dee \"Python Slayer\" Turco, Kishan \"Code Killer\" Vekaria, "
          "and Jeff \"Algo Assassin\" Stockman")


# start_game()

game_board = Dungeon(6, 6, 0, 0)
game_board.make_dungeon()
game_board.place_dungeon_items()
print(game_board)
print("current room")
print(game_board.current_room())
print("\n room map")
print_room(game_board)
print("\n vision map")
show_vision_map(game_board)

