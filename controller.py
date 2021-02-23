from gameboard import GameBoard
from view import View


class Controller:
    def __init__(self):
        # self.__view = view
        self.__game_board = None
        self.init_game()

    def set_game_board(self, x, y):
        self.__game_board = GameBoard(x, y)

    def player_input(self, __game_board):
        """
        Allows a player to move based on available paths and options
        :return: Action based on input
        """

        x, y = __game_board.current_cell()
        cell = __game_board.cell_at(x, y)
        options = []
        # movement options based on available paths
        if self.__game_board.is_valid_room(x, y - 1) is True and cell.has_north_path() is True:
            options.append("u")
        if self.__game_board.is_valid_room(x, y + 1) is True and cell.has_south_path() is True:
            options.append("d")
        if self.__game_board.is_valid_room(x + 1, y) is True and cell.has_east_path() is True:
            options.append("r")
        if self.__game_board.is_valid_room(x - 1, y) is True and cell.has_west_path() is True:
            options.append("l")
        # save, load, quit options
        options.append("s")  # save game
        options.append("o")  # load game
        options.append("q")  # quit
        print(options)
        # return options

        keystroke = input("What would you like to do? Press \"1\" for all options: ")

        if keystroke == "1":  # all available user options
            return options, True

        # exit, save, load a game
        elif keystroke == "q":  # option to exit the game
            a = input("Houston, you have a problem. Do you really want to exit? (y or n): ")
            if a == "y":
                return "***GAME OVER***", False
                # place 'exit game' method here
            elif a == "n":
                return "\nCarry on, space cowboy!\n", True
            else:
                return "That is not a valid command. Try again.", True
        elif keystroke == "s":
            pass  # insert 'save game' method here
        elif keystroke == "o":
            pass  # insert 'load game' method here

        # move commands
        elif keystroke == "u":
            if "u" in options:
                pass
                # prompt for question
                # if question answered correctly:
                self.__game_board.move_to(x, y - 1)
                return "", True
                # else:
                #     current_cell.remove_path(next_room, direction)
            else:
                return "That is not a valid command.  Try again.", True
        elif keystroke == "d":
            if "d" in options:
                pass
                # prompt for question
                # if question answered correctly:
                self.__game_board.move_to(x, y + 1)
                return "", True
                # else:
                #     current_cell.remove_path(next_room, direction)
            else:
                return "That is not a valid command.  Try again.", True
        elif keystroke == "l":
            if "l" in options:
                pass
                # prompt for question
                # if question answered correctly:
                self.__game_board.move_to(x - 1, y)
                return "", True
                # else:
                #     current_cell.remove_path(next_room, direction)
            else:
                return "That is not a valid command.  Try again.", True
        elif keystroke == "r":
            if "r" in options:
                pass
                # prompt for question
                # if question answered correctly:
                self.__game_board.move_to(x + 1, y)
                return "", True
                # else:
                #     current_cell.remove_path(next_room, direction)
            else:
                return "That is not a valid command.  Try again.", True
        else:
            return "That is not a valid command.  Try again.", True

    def init_game(self):
        """
        Initialises the game. Displays welcome message. Gets the menu option. Loads a new or saved game.
        Gets the game level. Initialises the game board.
        :return: None
        """
        View.display_welcome_msg()
        # menu_option = View.get_menu_option()
        # if menu_option == "1":
        #     file_option = View.get_file_option()
        #     if file_option == "1":
        level = View.get_level()
        if level == "1":
            self.set_game_board(4, 4)
        elif level == "2":
            self.set_game_board(5, 5)
        elif level == "3":
            self.set_game_board(6, 6)
        self.__game_board.place_entrance_exit()
        self.__game_board.update_border_paths()
        self.play_game()

            # elif file_option == 2:
            #     if self.__saved_game_board:
            #         self.__game_board = self.__saved_game_board
            #         self.__play_game()
            #     else:
            #         self.__view.display_msg("No saved game. Choose another option.")
            #         self.__view.get_menu_option()
            #
            # elif file_option == 3:
            #     if self.__game_board:
            #         self.__saved_game_board = self.__game_board
            #         self.__view.display_msg("Game saved.")
            #         self.init_game()
            #     else:
            #         self.__view.display_msg("No game to save. Choose another option.")
            #         self.__view.get_menu_option()
            # ADD code for file option 4 - Exit
        # ADD code for menu option 2 -  Help
        # else:
        #     pass

    def play_game(self):
        """
        This is the main game loop. It takes input, and prints
        responses to the console. At the end it asks whether the
        user would like to play again.
        """
        play = True
        while play:
            x, y = self.__game_board.current_cell()
            current_cell = self.__game_board.cell_at(x, y)
            # Display game board and current room
            View.display_gameboard_map(self.__game_board)
            View.display_current_location(current_cell)
            # if current room is exit You won!! else continue
            if current_cell.get_exit() is True:
                View.display_game_won()
                play = False
            else:
                statement, play = self.player_input(self.__game_board)
                View.display_msg(statement)
                # check if exit is reachable from current loc
                # if self.__game_board.traverse(x, y) is False:
                #     # game lost as theres no way out!!
                #     View.display_game_lost()
                #     play = False

        while True:
            user_input = View.replay()
            if user_input == 'y' or user_input == 'yes':
                self.init_game()
            else:
                # print Thanks for playing.
                View.display_closing_msg()
                break


new = Controller()
new.init_game()

