WELCOME = "Welcome to the Trivia Space Adventure game. \n"

INTRO = "Find your way to Mars by answering questions along the game board. \n\n" \
        "Correct answers allow you to continue along your journey.  Wrong answers "\
        "require you to seek an alternate orbit.  If you find yourself without a "\
        "path to Mars, you will run out of oxygen and meet your ultimate demise...\n\n"\
        "So, are you as smart as a Rocket Scientist...? Let's find out!"


class View:
    def __init__(self):
        pass

    @staticmethod
    def display_welcome_msg():
        """
        Displays welcome message
        :return: None
        """
        # print(WELCOME)
        return INTRO

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
        print(room)

    @staticmethod
    def display_msg(msg):
        """
        Displays message
        :return: None
        """
        print(msg)

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

    @staticmethod
    def ask_m_question(question):
        OPTIONS = {
            "1" : question[1][0],
            "2" : question[1][1],
            "3" : question[1][2],
            "4" : question[1][3]
        }
        while True:
            try:
                answer_input = input(f"Answer the following question: \n {question[0]} \n {OPTIONS}")
                if answer_input in OPTIONS:
                    return OPTIONS[answer_input]
                else:
                    print("Error: Invalid option")
            except ValueError:
                print("Error: Invalid option")

    @staticmethod
    def ask_true_false_question(question):
        OPTIONS = {
            "1": question[1][0],
            "2": question[1][1]
        }
        while True:
            try:
                answer_input = input(f"Answer the following question: \n {question[0]} \n {OPTIONS}")
                if answer_input in OPTIONS:
                    return OPTIONS[answer_input]
                else:
                    print("Error: Invalid option")
            except ValueError:
                print("Error: Invalid option")

    @staticmethod
    def ask_short_ans_question(question):
        while True:
            try:
                answer_input = input(f"Answer the following question: \n {question}")
                return answer_input
            except ValueError:
                print("Error: Invalid option")
##########
