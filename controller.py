from gameboard import GameBoard
from view import View, INTRO
from db_access import *
import random
from multiple_choice_question import MultipleChoiceQuestion
from short_ans_question import ShortAnsQuestion
from true_false_question import TrueFalseQuestion
import pickle
import os


class Controller:
    def __init__(self):
        """
        Initializes the database, question count and game board fields.
        """
        # self.__view = view
        self.__game_board = None
        self.database = r"python_sqlite.db"
        self.q_count = get_question_count(self.database)

    def set_game_board(self, x, y):
        """
        Sets the gameboard to be of a specific size based on the parameters.
        """
        self.__game_board = GameBoard(x, y)

    def pick_question(self, stat):
        """
        Randomly selects a new question from the database.
        :return: Int
        """
        while True:
            rand_q = random.randint(1, self.q_count)
            if stat[rand_q - 1] == 0:
                return rand_q

    def prompt_question(self, __game_board):
        """
        Initializes the question status list of the game board depending on the number of questions
        in the database. Based on the random question type picked instantiates the Question class.
        Displays and question by calling the appropriate method in the View and gets user input.
        Verifies the user in put to check for correct answer
        and returns Bool to indicate if the answer is correct.
        """
        # initialize question stat for a new gameboard
        if len(__game_board.question_stat) == 0:
            __game_board.set_question_stat(self.q_count)

        # in case all the questions in the database have been used.
        if __game_board.question_stat.count(0) == 0:
            __game_board.set_question_stat(self.q_count)
        else:
            rand_question = self.pick_question(__game_board.question_stat)
            __game_board.update_question_stat(rand_question - 1, 1)

            q_a = get_q_a(self.database, rand_question)
            if q_a[0][0] == 'MULTIPLE CHOICE':
                question = MultipleChoiceQuestion(q_a[0][1], q_a[1], q_a[2])
                ans = View.ask_m_question(question.get_question())
            elif q_a[0][0] == 'TRUE / FALSE':
                question = TrueFalseQuestion(q_a[0][1], q_a[1])
                ans = View.ask_true_false_question(question.get_question())
            elif q_a[0][0] == 'SHORT ANSWER':
                question = ShortAnsQuestion(q_a[0][1], q_a[1])
                ans = View.ask_short_ans_question(question.get_question())
            return question.verify_ans(ans)

    def player_input(self, __game_board):
        """
        Allows a player to move based on available paths and options
        :return: Action based on input
        """

        x, y = __game_board.current_cell()
        cell = __game_board.cell_at(x, y)
        options = []
        # movement options based on available paths
        if self.__game_board.is_valid_cell(x, y - 1) is True and cell.has_north_path() is True:
            options.append("u")
        if self.__game_board.is_valid_cell(x, y + 1) is True and cell.has_south_path() is True:
            options.append("d")
        if self.__game_board.is_valid_cell(x + 1, y) is True and cell.has_east_path() is True:
            options.append("r")
        if self.__game_board.is_valid_cell(x - 1, y) is True and cell.has_west_path() is True:
            options.append("l")
        # save, load, quit options
        options.append("s")  # save game
        options.append("o")  # load game
        options.append("q")  # quit
        # print(options)
        # return options

        keystroke = input("What would you like to do? Press \"1\" for all options: ")

        if keystroke == "1":  # all available user options
            return options, True

        # exit, save, load a game
        elif keystroke == "q":  # option to exit the game
            a = View.quit()
            if a == "y":
                return "***GAME OVER***", False
            elif a == "n":
                return "\nCarry on, space cowboy!\n", True
            else:
                return "That is not a valid command. Try again.", True

        elif keystroke == "s":
            if self.__game_board:
                game = self.__game_board
                game_file = open('saved_game', 'wb')
                pickle.dump(game, game_file)
                game_file.close()
                return "Game saved.", False
            else:
                return "No game to save. Choose another option.", True

        elif keystroke == "o":
            if not os.path.isfile("saved_game"):
                View.display_msg('Error, You have no saved games.')
            else:
                game_file = open('saved_game', 'rb')
                game = pickle.load(game_file)
                game_file.close()
                self.__game_board = game
                return 'Game Loaded, Welcome back, Captain.', True

        # move commands
        elif keystroke == "u":
            if "u" in options:
                if self.prompt_question(self.__game_board) is True:
                    self.__game_board.move_to(x, y - 1)
                    return "Correct!!", True
                else:
                    self.__game_board.cell_at(x, y).remove_path(self.__game_board.cell_at(x, y - 1), "N")
                    return "Wrong!!", True
            else:
                return "That is not a valid command.  Try again.", True

        elif keystroke == "d":
            if "d" in options:
                if self.prompt_question(self.__game_board) is True:
                    self.__game_board.move_to(x, y + 1)
                    return "Correct!!", True
                else:
                    self.__game_board.cell_at(x, y).remove_path(self.__game_board.cell_at(x, y + 1), "S")
                    return "" \
                           "Wrong!!", True
            else:
                return "That is not a valid command.  Try again.", True

        elif keystroke == "l":
            if "l" in options:
                if self.prompt_question(self.__game_board) is True:
                    self.__game_board.move_to(x - 1, y)
                    return "Correct!!", True
                else:
                    self.__game_board.cell_at(x, y).remove_path(self.__game_board.cell_at(x - 1, y), "W")
                    return "Wrong!!", True
            else:
                return "That is not a valid command.  Try again.", True

        elif keystroke == "r":
            if "r" in options:
                if self.prompt_question(self.__game_board) is True:
                    self.__game_board.move_to(x + 1, y)
                    return "Correct!!", True
                else:
                    self.__game_board.cell_at(x, y).remove_path(self.__game_board.cell_at(x + 1, y), "E")
                    return "Wrong!!", True
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
        menu_option = View.get_menu_option()
        if menu_option == "1":
            file_option = View.get_file_option()
            if file_option == "1":
                self.set_game_board(4, 4)
                self.__game_board.place_entrance_exit()
                self.__game_board.update_border_paths()
                self.play_game()

            elif file_option == "2":
                if not os.path.isfile("saved_game"):
                    View.display_msg('Error, You have no saved games.')
                    View.display_msg("No saved game. Choose another option.")
                    self.init_game()
                else:
                    game_file = open('saved_game', 'rb')
                    game = pickle.load(game_file)
                    game_file.close()
                    self.__game_board = game
                    View.display_msg('Game Loaded, Welcome back, Captain.')
                    self.play_game()

            elif file_option == "3":
                if self.__game_board:
                    game = self.__game_board
                    game_file = open('saved_game', 'wb')
                    pickle.dump(game, game_file)
                    game_file.close()
                    View.display_msg("Game saved.")
                    self.init_game()
                else:
                    View.display_msg("No game to save. Choose another option.")
                    self.init_game()
            # file option 4 - Exit
            elif file_option == "4":
                a = View.quit()
                if a == "y":
                    View.display_closing_msg()
                elif a == "n":
                    View.display_msg("\nCarry on, space cowboy!\n")
                    self.init_game()
        elif menu_option == "2":
            View.display_msg(INTRO)
            self.init_game()

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
                if self.__game_board.traverse(x, y) is False:
                    # game lost as theres no way out!!
                    View.display_game_lost()
                    play = False

        while True:
            user_input = View.replay()
            if user_input == 'y' or user_input == 'yes':
                self.init_game()
            else:
                # print Thanks for playing.
                View.display_closing_msg()
                break


if __name__ == '__main__':
    new = Controller()
    new.init_game()
