WELCOME = "Welcome to the Trivia Space Adventure game. \n"

INTRO = "Find your way back to Earth by answering questions to board the space shuttle \n " \
        "from one planet to the next. Wrong answers result in you missing the space shuttle. \n " \
        "Too many wrong answers and you miss all available space shuttles and \n " \
        "find yourself stranded and lost in space with no way to return back home."


class View:
    def __init__(self):
        pass

    @staticmethod
    def display_welcome_msg():
        """
        Displays welcome message
        :return: None
        """
        print(WELCOME)
        print(INTRO)

    @staticmethod
    def get_menu_option():
        """
         Gets user input to choose one of the menu options.
        :return: Int
        """
        MENU = {
            "1": "File",
            "2": "Help"
        }
        while True:
            try:
                menu_input = input(f"Choose one of the menu options "
                                   f"by entering the corresponding "
                                   f"number \n {MENU} : ")
                if menu_input in MENU:
                    return menu_input
                else:
                    print("Error: Invalid option")
            except ValueError:
                print("Error: Invalid option")

    @staticmethod
    def get_file_option():
        """
        Gets user input to either start a new game or
        save the game or load a previously saved game
        :return: Int
        """
        FILE = {
            "1": "New game",
            "2": "Load game",
            "3": "Save game",
            "4": "Exit"
        }
        while True:
            try:
                file_input = input(f"Choose one of the file"
                                   f" menu options by entering "
                                   f"the corresponding number \n {FILE} : ")
                if file_input in FILE:
                    print(file_input)
                    return file_input
                else:
                    print("Error: Invalid option")
            except ValueError:
                print("Error: Invalid option")

    @staticmethod
    def get_level():
        """
        Gets user input to determine the level of the game.
        :return: Int
        """
        LEVEL = {
            "1": "Easy",
            "2": "Medium",
            "3": "Hard"
        }
        while True:
            try:
                level_input = input(f"Choose one of the levels "
                                    f"by entering the corresponding "
                                    f"number: \n {LEVEL}")
                if level_input in LEVEL:
                    return level_input
                else:
                    print("Error: Invalid option")
            except ValueError:
                print("Error: Invalid option")

##########
    @staticmethod
    def display_gameboard_map(gameboard):
        """
        Displays the gameboard map.
        :param gameboard: Gameboard
        :return: String rep of the gameboard(map)
        """
        print(gameboard)

    @staticmethod
    def display_current_location(room):
        """
        Displays info about the current location
        :param room: Object - current location
        :return: String rep of the current location.
        """
        pass

    @staticmethod
    def display_game_won():
        print("You have reached home. You won!!!!")

    @staticmethod
    def display_game_lost():
        print("You lost the game.")

    @staticmethod
    def get_user_command(moves):
        user_input = str(input(f'\nPossible paths: {moves} \n Enter your command :'))
        return user_input

    @staticmethod
    def replay():
        user_input = (str(input('\nEnter \'y\' or \'yes\' to play again >>> '))
                      .lower())
        return user_input

    @staticmethod
    def display_closing_msg():
        print("Thanks for playing! See you soon")
##########


