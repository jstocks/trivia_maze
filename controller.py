from gameboard import GameBoard


class Controller:
    def __init__(self, view):
        self.__view = view
        self.__game_board = None
        self.init_game()

    def set_game_board(self, x, y):
        self.__game_board = GameBoard(x, y)

    def get_valid_paths(self, x, y):
        """
        Returns a list containing the possible paths that the player can go in
        :return: List
        """
        options = []
        if self.__game_board.is_valid_room(x, y) is True and self.__game_board.__current_cell.has_north_path() is False:
            options.append("n")
        if self.__game_board.is_valid_room(x, y) is True and self.__game_board.__current_cell.has_south_path() is False:
            options.append("s")
        if self.__game_board.is_valid_room(x, y) is True and self.__game_board.__current_cell.has_east_path() is False:
            options.append("e")
        if self.__game_board.is_valid_room(x, y) is True and self.__game_board.__current_cell.has_west_path() is False:
            options.append("w")
        return options

    def init_game(self):
        """
        Initialises the game. Displays welcome message. Gets the menu option. Loads a new or saved game.
        Gets the game level. Initialises the game board.
        :return: None
        """
        self.__view.display_welcome_msg()
        menu_option = self.__view.get_menu_option()
        if menu_option == "1":
            file_option = self.__view.get_file_option()
            if file_option == "1":
                level = self.__view.get_level()
                if level == "1":
                    self.set_game_board(4, 4)
                elif level == "2":
                    self.set_game_board(5, 5)
                elif level == "3":
                    self.set_game_board(6, 6)
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
        else:
            pass

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
            self.__view.display_gameboard_map(self.__game_board)
            self.__view.display_current_location(current_cell)
            # if current room is exit You won!! else continue
            if current_cell.get_exit is True:
                self.__view.display_game_won()
                play = False
            else:
                # check if exit is reachable from current loc

                # get valid paths possible depending on current loc
                paths = self.get_valid_paths(x, y)
                if len(paths) > 0:
                    user_input = self.__view.get_user_command(paths)
                    # retrieve question from database and instantiate question class.
                    # q =
                    # display question
                    # get answer
                    # if q.verify_ans(user_ans):
                    # if answer is right, update the player position
                    #  pass
                    # else:
                    # lock the path
                    pass
                else:
                    # game lost as theres no way out!!
                    self.__view.display_game_lost()
                    play = False

        while True:
            user_input = self.__view.replay()
            if user_input == 'y' or user_input == 'yes':
                self.init_game()
            else:
                # print Thanks for playing.
                self.__view.display_closing_msg()
                break
