from tkinter import *
from tkinter import messagebox
from PIL import ImageTk
from gameboard import GameBoard
import os
from db_access import *
import random
from multiple_choice_question import MultipleChoiceQuestion
from short_ans_question import ShortAnsQuestion
from true_false_question import TrueFalseQuestion
import pickle
import winsound
from playsound import playsound


class TriviaGUI(Canvas):
    """
    Initializes the Canvas - widgets and visible items
    """
    def __init__(self, dimension, master=None, gameboard=None, sound=True):
        Canvas.__init__(self, master)
        Pack.config(self)
        self.master.title("Get to Mars!")
        self.pack()
        self.board = gameboard
        self.sound = sound
        self.dimension = dimension
        self.database = r"python_sqlite.db"
        self.moving_to = 0  # 1 up 2 down 3 left 4 right
        self.canvas = Canvas(self, width=dimension, height=dimension, bg="lightskyblue1")
        self.canvas.pack()
        self.show_board()
        self.show_cell()
        self.menu_widgets()
        self.move_widgets()
        self.legend()
        self.question()
        self.init_menu()

    def init_menu(self):
        """
        Displays the Text Menu at top of screen.
        """
        menu = Menu(self.master)
        self.master.config(menu=menu)

        file_menu = Menu(menu, tearoff=False)
        file_menu.add_command(label="New", command=self.new)
        file_menu.add_separator()
        file_menu.add_command(label="Load", command=self.load)
        file_menu.add_command(label="Save", command=self.save)
        file_menu.add_separator()
        file_menu.add_command(label="Exit", command=self.quit)
        menu.add_cascade(label="File", menu=file_menu)

        help_menu = Menu(menu, tearoff=False)
        help_menu.add_command(label="Help", command=self.help)
        help_menu.add_separator()
        help_menu.add_command(label="About", command=self.about)
        menu.add_cascade(label="Help", menu=help_menu)

    def new(self):
        """ Method to start a new game"""
        mbox = messagebox.askquestion('Start a new game?', icon='warning')
        if mbox == 'yes':
            program = sys.executable
            os.execl(program, program, *sys.argv)
        else:
            return

    def load(self):
        """
        Method to load the previously saved game
        """
        if not os.path.isfile("saved_game"):
            messagebox.showinfo(title='Error', message="You have no saved games.")
            return
        mbox = messagebox.askquestion('Load saved game?', icon='warning')
        if mbox == 'yes':
            game_file = open('saved_game', 'rb')
            game = pickle.load(game_file)
            game_file.close()
            self.board = game
            self.show_board()
            self.show_cell()
            messagebox.showinfo(title='Game Loaded', message="Welcome back, Captain.")
        else:
            return

    def save(self):
        """
        Method to save the current game.
        """
        mbox = messagebox.askquestion('Save game?', icon='warning')
        if mbox == 'yes':
            game = self.board
            game_file = open('saved_game', 'wb')
            pickle.dump(game, game_file)
            game_file.close()
            messagebox.showinfo(title='Game Saved', message="We'll be floating in space.... waiting.")
        else:
            return

    def help(self):
        """
        Displays the instructions for the game.
        """
        intro = "Find your way to Mars by answering questions along the game board. \n\n Correct answers allow you to " \
                "continue along your journey. Wrong answers require you to seek an alternate orbit.  If you find " \
                "yourself without a path to Mars, you will run out of oxygen and meet your ultimate demise...\n\n So, " \
                "are you as smart as a Rocket Scientist...? Let's find out! "

        messagebox.showinfo(title='Directions', message=intro)

    def about(self):
        """
        Displays information about the game creators and course.
        """
        messagebox.showinfo(title='Directions', message="Rocket Man Trivia Game\n\n"
                                                        "Created by Sriba Rajendran & "
                                                        "Jeff Stockman\n\n"
                                                        "University of Washington Graduate "
                                                        "Certificate Program for Software "
                                                        "Development Engineering\n\n"
                                                        "Core requirement for TCSS504 - March 2021 ")

    def quit(self):
        """
        Method to quit the game.
        """

        self.sound_quit()
        mbox = messagebox.askquestion('Exit... Are you sure?', icon='warning')
        if mbox == 'yes':
            self.master.destroy()
        else:
            return

    def menu_widgets(self):
        """
        Displays the top menu buttons
        """
        self.bnew = Button(self, text="NEW", height=1, width=5, bg="gold",
                          fg="black", relief="raised", command=self.new)
        self.bnew.place(x=4, y=4)
        self.bload = Button(self, text="LOAD", height=1, width=5, bg="gold",
                           fg="black", relief="raised", command=self.load)
        self.bload.place(x=49, y=4)
        self.bsave = Button(self, text="SAVE", height=1, width=5, bg="gold",
                           fg="black", relief="raised", command=self.save)
        self.bsave.place(x=94, y=4)
        self.bhelp = Button(self, text="HELP", height=1, width=5, bg="gold",
                           fg="black", relief="raised", command=self.help)
        self.bhelp.place(x=139, y=4)
        self.bexit = Button(self, text="EXIT", height=1, width=5, bg="gold",
                           fg="black", relief="raised", command=self.quit)
        self.bexit.place(x=184, y=4)
        self.bhidden = Button(self, text=" ", height=1, width=2, bg="lightskyblue1",
                             fg="lightskyblue1", relief="flat", command=self.sound_hidden)
        self.bhidden.place(x=780, y=4)

    def move_widgets(self):
        """
        Displays the move buttons.
        """

        self.move_up = Button(self, text="MOVE UP", height=1, width=10, bg="gold",
                              fg="black", relief="raised", state=NORMAL, command=self.plan_to_move_up)
        self.move_up.place(x=585, y=140)
        self.move_down = Button(self, text="MOVE DOWN", height=1, width=10, bg="gold",
                                fg="black", relief="raised", state=NORMAL,command=self.plan_to_move_down)
        self.move_down.place(x=585, y=340)
        self.move_left = Button(self, text="MOVE\nLEFT", height=2, width=6, bg="gold",
                                fg="black", relief="raised", state=NORMAL,command=self.plan_to_move_left)
        self.move_left.place(x=490, y=230)
        self.move_right = Button(self, text="MOVE\nRIGHT", height=2, width=6, bg="gold",
                                 fg="black", relief="raised", state=NORMAL, command=self.plan_to_move_right)
        self.move_right.place(x=710, y=230)

    def disable(self):
        """
        Helper method to disable the move buttons between turns.
        """
        self.move_up["state"] = "disabled"
        self.move_down["state"] = "disabled"
        self.move_left["state"] = "disabled"
        self.move_right["state"] = "disabled"

    def enable(self):
        """
        Helper method to enable the move buttons after turns.
        """
        self.move_up["state"] = "normal"
        self.move_down["state"] = "normal"
        self.move_left["state"] = "normal"
        self.move_right["state"] = "normal"

    def legend(self):
        """
        Displays the legend widgets.
        """
        label = Label(self.canvas, text='LEGEND', fg='black', bg='lightskyblue1', font="bold")
        self.canvas.create_window(168, 490, window=label)
        # player token
        self.img = ImageTk.PhotoImage(file="player_token.png")
        self.canvas.create_image(80, 545, image=self.img)
        label = Label(self.canvas, text='Player Token', fg='black', bg='lightskyblue1', font="bold")
        self.canvas.create_window(180, 540, window=label)
        # available paths
        self.img2 = ImageTk.PhotoImage(file="path_horiz.png")
        self.canvas.create_image(50, 600, image=self.img2)
        self.img3 = ImageTk.PhotoImage(file="path_vert.png")
        self.canvas.create_image(100, 600, image=self.img3)
        label2 = Label(self.canvas, text='Available Paths', fg='black', bg='lightskyblue1', font="bold")
        self.canvas.create_window(190, 600, window=label2)
        # blocked paths
        self.img4 = ImageTk.PhotoImage(file="blocked.png")
        self.canvas.create_image(80, 660, image=self.img4)
        label3 = Label(self.canvas, text='Blocked Paths', fg='black', bg='lightskyblue1', font="bold")
        self.canvas.create_window(188, 660, window=label3)
        # finish
        self.img5 = ImageTk.PhotoImage(file="finish.png")
        self.canvas.create_image(80, 720, image=self.img5)
        label4 = Label(self.canvas, text='Finish', fg='black', bg='lightskyblue1', font="bold")
        self.canvas.create_window(160, 720, window=label4)

    def question(self):
        """
        Displays the Question Widget.
        """
        # question box
        label = Label(self.canvas, text='QUESTION', fg='black', bg='lightskyblue1', font="bold")
        self.canvas.create_window(550, 490, window=label)

        self.canvas.create_rectangle(360, 525, 750, 750, fill='lightskyblue1')

    def show_board(self):
        """
        Displays the game board, player token, and available paths / blocked paths.
        """
        self.canvas.create_rectangle(70, 70, 430, 430, fill='')

        origin_x = 75
        origin_y = 75
        size = 50
        x1 = origin_x
        x2 = x1 + size
        x3 = x2 + size
        x4 = x3 + size
        x5 = x4 + size
        x6 = x5 + size
        x7 = x6 + size
        x8 = x7 + size
        y1 = origin_y
        y2 = y1 + size
        y3 = y2 + size
        y4 = y3 + size
        y5 = y4 + size
        y6 = y5 + size
        y7 = y6 + size
        y8 = y7 + size

        # Row 1
        cell_1 = self.canvas.create_rectangle(x1, y1, x2, y2, fill='ivory2', outline="")
        path_1_2 = self.canvas.create_rectangle(x2, y1, x3, y2, fill='lightskyblue1', outline="")
        cell_2 = self.canvas.create_rectangle(x3, y1, x4, y2, fill='ivory2', outline="")
        path_2_3 = self.canvas.create_rectangle(x4, y1, x5, y2, fill='lightskyblue1', outline="")
        cell_3 = self.canvas.create_rectangle(x5, y1, x6, y2, fill='ivory2', outline="")
        path_3_4 = self.canvas.create_rectangle(x6, y1, x7, y2, fill='lightskyblue1', outline="")
        cell_4 = self.canvas.create_rectangle(x7, y1, x8, y2, fill='ivory2', outline="")

        # # Row 2
        path_1_5 = self.canvas.create_rectangle(x1, y2, x2, y3, fill='lightskyblue1', outline="")
        empty_1 = self.canvas.create_rectangle(x2, y2, x3, y3, fill='lightskyblue1', outline="")
        path_2__6 = self.canvas.create_rectangle(x3, y2, x4, y3, fill='lightskyblue1', outline="")
        empty_2 = self.canvas.create_rectangle(x4, y2, x5, y3, fill='lightskyblue1', outline="")
        path_3_7 = self.canvas.create_rectangle(x5, y2, x6, y3, fill='lightskyblue1', outline="")
        empty_3 = self.canvas.create_rectangle(x6, y2, x7, y3, fill='lightskyblue1', outline="")
        path_4_8 = self.canvas.create_rectangle(x7, y2, x8, y3, fill='lightskyblue1', outline="")

        # Row 3
        cell_5 = self.canvas.create_rectangle(x1, y3, x2, y4, fill='ivory2', outline="")
        path_5_6 = self.canvas.create_rectangle(x2, y3, x3, y4, fill='lightskyblue1', outline="")
        cell_6 = self.canvas.create_rectangle(x3, y3, x4, y4, fill='ivory2', outline="")
        path_6_7 = self.canvas.create_rectangle(x4, y3, x5, y4, fill='lightskyblue1', outline="")
        cell_7 = self.canvas.create_rectangle(x5, y3, x6, y4, fill='ivory2', outline="")
        path_7_8 = self.canvas.create_rectangle(x6, y3, x7, y4, fill='lightskyblue1', outline="")
        cell_8 = self.canvas.create_rectangle(x7, y3, x8, y4, fill='ivory2', outline="")

        # Row 4
        path_5_9 = self.canvas.create_rectangle(x1, y4, x2, y5, fill='lightskyblue1', outline="")
        empty_4 = self.canvas.create_rectangle(x2, y4, x3, y5, fill='lightskyblue1', outline="")
        path_6_10 = self.canvas.create_rectangle(x3, y4, x4, y5, fill='lightskyblue1', outline="")
        empty_5 = self.canvas.create_rectangle(x4, y4, x5, y5, fill='lightskyblue1', outline="")
        path_7_11 = self.canvas.create_rectangle(x5, y4, x6, y5, fill='lightskyblue1', outline="")
        empty_6 = self.canvas.create_rectangle(x6, y4, x7, y5, fill='lightskyblue1', outline="")
        path_8_12 = self.canvas.create_rectangle(x7, y4, x8, y5, fill='lightskyblue1', outline="")

        # Row 5
        cell_9 = self.canvas.create_rectangle(x1, y5, x2, y6, fill='ivory2', outline="")
        path_9_10 = self.canvas.create_rectangle(x2, y5, x3, y6, fill='lightskyblue1', outline="")
        cell_10 = self.canvas.create_rectangle(x3, y5, x4, y6, fill='ivory2', outline="")
        path_10_11 = self.canvas.create_rectangle(x4, y5, x5, y6, fill='lightskyblue1', outline="")
        cell_11 = self.canvas.create_rectangle(x5, y5, x6, y6, fill='ivory2', outline="")
        path_11_12 = self.canvas.create_rectangle(x6, y5, x7, y6, fill='lightskyblue1', outline="")
        cell_12 = self.canvas.create_rectangle(x7, y5, x8, y6, fill='ivory2', outline="")

        # # Row 6
        path_9_13 = self.canvas.create_rectangle(x1, y6, x2, y7, fill='lightskyblue1', outline="")
        empty_7 = self.canvas.create_rectangle(x2, y6, x3, y7, fill='lightskyblue1', outline="")
        path_10_14 = self.canvas.create_rectangle(x3, y6, x4, y7, fill='lightskyblue1', outline="")
        empty_8 = self.canvas.create_rectangle(x4, y6, x5, y7, fill='lightskyblue1', outline="")
        path_11_15 = self.canvas.create_rectangle(x5, y6, x6, y7, fill='lightskyblue1', outline="")
        empty_9 = self.canvas.create_rectangle(x6, y6, x7, y7, fill='lightskyblue1', outline="")
        path_12_16 = self.canvas.create_rectangle(x7, y6, x8, y7, fill='lightskyblue1', outline="")

        # Row 7
        cell_13 = self.canvas.create_rectangle(x1, y7, x2, y8, fill='ivory2', outline="")
        path_13_14 = self.canvas.create_rectangle(x2, y7, y8, y8, fill='lightskyblue1', outline="")
        cell_14 = self.canvas.create_rectangle(x3, y7, x4, y8, fill='ivory2', outline="")
        path_14_15 = self.canvas.create_rectangle(x4, y7, x5, y8, fill='lightskyblue1', outline="")
        cell_15 = self.canvas.create_rectangle(x5, y7, x6, y8, fill='ivory2', outline="")
        path_15_16 = self.canvas.create_rectangle(x6, y7, x7, y8, fill='lightskyblue1', outline="")
        cell_16 = self.canvas.create_rectangle(x7, y7, x8, y8, fill='ivory2', outline="")

        # draw the current position of the player
        x, y = self.board.current_cell()

        self.img6 = ImageTk.PhotoImage(file="player_token.png")
        self.canvas.create_image(100 + x * 100, 100 + y * 100, image=self.img6)

        # draw Mars / exit
        x, y = self.board.exit_cell()
        self.image_exit = ImageTk.PhotoImage(file="finish.png")
        self.canvas.create_image(100 + x * 100, 100 + y * 100, image=self.image_exit)

        # land the rocket on the exit
        if self.board.current_cell() == self.board.exit_cell():
            self.canvas.create_image(100 + x * 100, 100 + y * 100, image=self.image_exit)
            self.canvas.create_image(100 + x * 100, 100 + y * 100, image=self.img6)

        # set path icons
        self.paths_vertical = ImageTk.PhotoImage(file="path_vert.png")
        self.paths_horizontal = ImageTk.PhotoImage(file="path_horiz.png")
        self.paths_blocked = ImageTk.PhotoImage(file="blocked.png")
        for a in range(0, self.board.get_nx(), 2):
            for b in range(0, self.board.get_ny(), 2):
                if a - 1 >= 0:
                    if self.board.cell_at(a, b).has_west_path():
                        self.canvas.create_image(50 + a * 100, 100 + b * 100, image=self.paths_horizontal)
                    else:
                        self.canvas.create_image(50 + a * 100, 100 + b * 100, image=self.paths_blocked)
                if a + 1 <= self.board.get_nx() - 1:
                    if self.board.cell_at(a, b).has_east_path():
                        self.canvas.create_image(150 + a * 100, 100 + b * 100, image=self.paths_horizontal)
                    else:
                        self.canvas.create_image(150 + a * 100, 100 + b * 100, image=self.paths_blocked)
                if b + 1 <= self.board.get_ny() - 1:
                    if self.board.cell_at(a, b).has_south_path():
                        self.canvas.create_image(100 + a * 100, 150 + b * 100, image=self.paths_vertical)
                    else:
                        self.canvas.create_image(100 + a * 100, 150 + b * 100, image=self.paths_blocked)
                if b - 1 >= 0:
                    if self.board.cell_at(a, b).has_north_path():
                        self.canvas.create_image(100 + a * 100, 50 + b * 100, image=self.paths_vertical)
                    else:
                        self.canvas.create_image(100 + a * 100, 50 + b * 100, image=self.paths_blocked)

        for a in range(1, self.board.get_nx(), 2):
            for b in range(1, self.board.get_ny(), 2):
                if a - 1 >= 0:
                    if self.board.cell_at(a, b).has_west_path():
                        self.canvas.create_image(50 + a * 100, 100 + b * 100, image=self.paths_horizontal)
                    else:
                        self.canvas.create_image(50 + a * 100, 100 + b * 100, image=self.paths_blocked)
                if a + 1 <= self.board.get_nx() - 1:
                    if self.board.cell_at(a, b).has_east_path():
                        self.canvas.create_image(150 + a * 100, 100 + b * 100, image=self.paths_horizontal)
                    else:
                        self.canvas.create_image(150 + a * 100, 100 + b * 100, image=self.paths_blocked)
                if b + 1 <= self.board.get_ny() - 1:
                    if self.board.cell_at(a, b).has_south_path():
                        self.canvas.create_image(100 + a * 100, 150 + b * 100, image=self.paths_vertical)
                    else:
                        self.canvas.create_image(100 + a * 100, 150 + b * 100, image=self.paths_blocked)
                if b - 1 >= 0:
                    if self.board.cell_at(a, b).has_north_path():
                        self.canvas.create_image(100 + a * 100, 50 + b * 100, image=self.paths_vertical)
                    else:
                        self.canvas.create_image(100 + a * 100, 50 + b * 100, image=self.paths_blocked)

    def show_cell(self):
        """
        Displays the current cell and available options.
        """
        label = Label(self.canvas, text='CURRENT LOCATION', fg='black', bg='lightskyblue1', font="bold")
        self.canvas.create_window(625, 100, window=label)

        origin_x = 550
        origin_y = 175
        size = 50
        x1 = origin_x
        x2 = x1 + size
        x3 = x2 + size
        x4 = x3 + size
        y1 = origin_y
        y2 = y1 + size
        y3 = y2 + size
        y4 = y3 + size

        self.paths_blocked2 = ImageTk.PhotoImage(file="blocked.png")
        a, b = self.board.current_cell()

        # Row 1
        n = self.canvas.create_rectangle(x2, y1, x3, y2, fill='lightskyblue1', outline="")
        if b - 1 >= 0:
            if self.board.cell_at(a, b).has_north_path():
                self.canvas.create_image((x2 + x3) / 2, (y1 + y2) / 2, image=self.paths_vertical)
            else:
                self.canvas.create_image((x2 + x3) / 2, (y1 + y2) / 2, image=self.paths_blocked)

        # self.canvas.create_image((x2 + x3) / 2, (y1 + y2) / 2, image=self.paths_blocked2)

        # Row 2
        w = self.canvas.create_rectangle(x1, y2, x2, y3, fill='lightskyblue1', outline="")
        if a - 1 >= 0:
            if self.board.cell_at(a, b).has_west_path():
                self.canvas.create_image((x1 + x2) / 2, (y2 + y3) / 2, image=self.paths_horizontal)
            else:
                self.canvas.create_image((x1 + x2) / 2, (y2 + y3) / 2, image=self.paths_blocked)

        center = self.canvas.create_rectangle(x2, y2, x3, y3, fill='ivory2', outline="")
        self.img_token = ImageTk.PhotoImage(file="player_token.png")
        self.canvas.create_image((x2 + x3) / 2, (y2 + y3) / 2, image=self.img_token)

        e = self.canvas.create_rectangle(x3, y2, x4, y3, fill='lightskyblue1', outline="")
        if a + 1 <= self.board.get_nx() - 1:
            if self.board.cell_at(a, b).has_east_path():
                self.canvas.create_image((x3 + x4) / 2, (y3 + y2) / 2, image=self.paths_horizontal)
            else:
                self.canvas.create_image((x3 + x4) / 2, (y3 + y2) / 2, image=self.paths_blocked)

        # Row 3
        s = self.canvas.create_rectangle(x2, y3, x3, y4, fill='lightskyblue1', outline="")
        if b + 1 <= self.board.get_ny() - 1:
            if self.board.cell_at(a, b).has_south_path():
                self.canvas.create_image((x2 + x3) / 2, (y3 + y4) / 2, image=self.paths_vertical)
            else:
                self.canvas.create_image((x2 + x3) / 2, (y3 + y4) / 2, image=self.paths_blocked)

    def plan_to_move_up(self):
        """
        Helper move function that stores movement until after question is answered.
        """
        self.sound_click()
        self.moving_to = 1
        x, y = self.board.current_cell()
        cell = self.board.cell_at(x, y)
        if self.board.is_valid_cell(x, y - 1) is True and cell.has_north_path() is True:
            self.show_question()
        else:
            self.question()

    def plan_to_move_down(self):
        """
        Helper move function that stores movement until after question is answered.
        """
        self.sound_click()
        self.moving_to = 2
        x, y = self.board.current_cell()
        cell = self.board.cell_at(x, y)
        if self.board.is_valid_cell(x, y + 1) is True and cell.has_south_path() is True:
            self.show_question()
        else:
            self.question()

    def plan_to_move_left(self):
        """
        Helper move function that stores movement until after question is answered.
        """
        self.sound_click()
        self.moving_to = 3
        x, y = self.board.current_cell()
        cell = self.board.cell_at(x, y)
        if self.board.is_valid_cell(x - 1, y) is True and cell.has_west_path() is True:
            self.show_question()
        else:
            self.question()

    def plan_to_move_right(self):
        """
        Helper move function that stores movement until after question is answered.
        """
        self.sound_click()
        self.moving_to = 4
        x, y = self.board.current_cell()
        cell = self.board.cell_at(x, y)
        if self.board.is_valid_cell(x + 1, y) is True and cell.has_east_path() is True:
            self.show_question()
        else:
            self.question()

    def pick_question(self, stat):
        """
        Randomly selects a new question from the database.
        :return: Int
        """
        count = get_question_count(self.database)
        while True:
            rand_q = random.randint(1, count)
            if stat[rand_q - 1] == 0:
                return rand_q

    def prompt_question(self, __game_board):
        """
        Initializes the question status list of the gameboard depending on the number of questions
        in the database. Based on the random question type picked instantiates the Question class
        and return the question object.
        """
        # initialize question stat for a new gameboard
        if len(__game_board.question_stat) == 0:
            __game_board.set_question_stat(65)
        # in case all the questions in the database have been used.
        if __game_board.question_stat.count(0) == 0:
            __game_board.set_question_stat(65)
        else:
            rand_question = self.pick_question(__game_board.question_stat)
            q_a = get_q_a(self.database, rand_question)
            if q_a[0][0] == 'MULTIPLE CHOICE':
                question = MultipleChoiceQuestion(q_a[0][1], q_a[1], q_a[2])
            elif q_a[0][0] == 'TRUE / FALSE':
                question = TrueFalseQuestion(q_a[0][1], q_a[1])
            elif q_a[0][0] == 'SHORT ANSWER':
                question = ShortAnsQuestion(q_a[0][1], q_a[1])
            __game_board.update_question_stat(rand_question - 1, 1)
            # return question.verify_ans(ans)
            return question

    def show_question(self):
        """
        Displays the question and gets user input - answer. Calls the verify answer method
        to check if its the correct answer.
        """
        self.disable()
        question = self.prompt_question(self.board)
        q = question.get_question()
        var = StringVar()
        widget_holder = []

        if question.__class__.__name__ == "MultipleChoiceQuestion":
            label1 = Label(self.canvas, text=q[0], fg='black', bg='lightskyblue1',
                           font="bold", wraplength=375, justify="left")
            widget_holder.append(label1)

            def get_ans():
                ans = (str(var.get()))
                self.verify_answer(question.verify_ans(ans))
                for widget in widget_holder:
                    widget.destroy()

            r1 = Radiobutton(self.canvas, text=q[1][0], padx=20, fg='black', bg='lightskyblue1',
                             font="bold", variable=var, value=q[1][0], command=get_ans)
            r1.place(x=400, y=620)
            r2 = Radiobutton(self.canvas, text=q[1][1], padx=20, fg='black', bg='lightskyblue1',
                             font="bold", variable=var, value=q[1][1], command=get_ans)
            r2.place(x=400, y=650)
            r3 = Radiobutton(self.canvas, text=q[1][2], padx=20, fg='black', bg='lightskyblue1',
                             font="bold", variable=var, value=q[1][2], command=get_ans)
            r3.place(x=400, y=680)
            r4 = Radiobutton(self.canvas, text=q[1][3], padx=20, fg='black', bg='lightskyblue1',
                             font="bold", variable=var, value=q[1][3], command=get_ans)
            r4.place(x=400, y=710)
            widget_holder.append(r1)
            widget_holder.append(r2)
            widget_holder.append(r3)
            widget_holder.append(r4)

        elif question.__class__.__name__ == "TrueFalseQuestion":
            label1 = Label(self.canvas, text=q[0], fg='black', bg='lightskyblue1', font="bold", wraplength=375,
                           justify="center")
            widget_holder.append(label1)

            def get_ans():
                ans = (str(var.get()))
                self.verify_answer(question.verify_ans(ans))
                for widget in widget_holder:
                    widget.destroy()

            r1 = Radiobutton(self.canvas, text=q[1][0], padx=20, fg='black', bg='lightskyblue1',
                             font="bold", variable=var, value=q[1][0], command=get_ans)
            r1.place(x=400, y=600)
            r2 = Radiobutton(self.canvas, text=q[1][1], padx=20, fg='black', bg='lightskyblue1',
                             font="bold", variable=var, value=q[1][1], command=get_ans)
            r2.place(x=400, y=630)
            widget_holder.append(r1)
            widget_holder.append(r2)

        else:
            label1 = Label(self.canvas, text=q, fg='black', bg='lightskyblue1', font="bold", wraplength=375,
                           justify="center")
            widget_holder.append(label1)

            def take_input():
                INPUT = inputtxt.get("1.0", "end-1c")
                self.verify_answer(question.verify_ans(INPUT))
                for widget in widget_holder:
                    widget.destroy()

            inputtxt = Text(self.canvas, height=1, width=25, bg="white")
            inputtxt.place(x=400, y=655)
            widget_holder.append(inputtxt)
            b = Button(self.canvas, height=1, width=10, text="Enter", command=lambda: take_input())
            b.place(x=400, y=680)

            # binds Enter key for short answer question
            self.master.bind('<Return>', lambda event=None: b.invoke())

            widget_holder.append(b)

        self.canvas.create_window(550, 570, window=label1)

    def verify_answer(self, answer):
        """
        Determines if player moves or path is blocked, based on answer.
        """
        x, y = self.board.current_cell()
        # simulate the question system
        if answer is True:
            if self.moving_to == 1:  # up
                self.now_move_up()
            elif self.moving_to == 2:  # down
                self.now_move_down()
            elif self.moving_to == 3:  # left
                self.now_move_left()
            elif self.moving_to == 4:  # right
                self.now_move_right()
        else:
            if self.moving_to == 1:  # up
                self.board.cell_at(x, y).remove_path(self.board.cell_at(x, y - 1), "N")
            elif self.moving_to == 2:  # down
                self.board.cell_at(x, y).remove_path(self.board.cell_at(x, y + 1), "S")
            elif self.moving_to == 3:  # left
                self.board.cell_at(x, y).remove_path(self.board.cell_at(x - 1, y), "W")
            elif self.moving_to == 4:  # right
                self.board.cell_at(x, y).remove_path(self.board.cell_at(x + 1, y), "E")

            self.show_board()
            self.show_cell()
            self.losing()

        self.show_board()
        self.show_cell()
        self.enable()

    def now_move_up(self):
        """
        Method to move player to correct position if question answered correctly.
        Determines if player has won the game.
        """
        x, y = self.board.current_cell()
        if y - 1 < 0:
            return
        self.board.move_to(x, y - 1)
        self.show_board()
        self.winning()

    def now_move_down(self):
        """
        Method to move player to correct position if question answered correctly.
        Determines if player has won the game.
        """
        x, y = self.board.current_cell()
        if y + 1 >= self.board.get_ny():
            return
        self.board.move_to(x, y + 1)
        self.show_board()
        self.winning()

    def now_move_left(self):
        """
        Method to move player to correct position if question answered correctly.
        Determines if player has won the game.
        """
        x, y = self.board.current_cell()
        if x - 1 < 0:
            return
        self.board.move_to(x - 1, y)
        self.show_board()
        self.winning()

    def now_move_right(self):
        """
        Method to move player to correct position if question answered correctly.
        Determines if player has won the game.
        """
        x, y = self.board.current_cell()
        if x + 1 >= self.board.get_nx():
            return
        self.board.move_to(x + 1, y)
        self.show_board()
        self.winning()

    def winning(self):
        """
        Determines if player reaches the exit.
        """
        x, y = self.board.current_cell()
        if self.board.cell_at(x, y).get_exit() is True:
            self.sound_win()
            mbox1 = messagebox.askquestion(title='You made it to Mars!',
                                        message="Congratulations, you won the game!\n\n"
                                        "Play again?")
            if mbox1 == 'yes':
                program = sys.executable
                os.execl(program, program, *sys.argv)
            else:
                return

    def losing(self):
        """Checks to see if all paths are blocked / can't traverse board.
        """
        x, y = self.board.current_cell()
        if self.board.traverse(x, y) is False:
            self.sound_lose()
            messagebox.showinfo(title='GAME OVER', message="Sorry, you lose!")

    def sound_click(self):
        """
        Sound.
        """
        if self.sound is True:
            winsound.Beep(300, 200)

    def menu_click(self):
        """
        Sound.
        """
        if self.sound is True:
            winsound.Beep(100, 200)

    def sound_quit(self):
        """
        Quit Sound.
        """
        if self.sound is True:
            playsound('houston.mp3')

    def sound_win(self):
        """
        Win Sound.
        """
        if self.sound is True:
            playsound('winning.mp3')

    def sound_lose(self):
        """
        Lose Sound.
        """
        if self.sound is True:
            playsound('lose.mp3')

    def sound_hidden(self):
        """
        Easter Egg - Thanks for all your help, Major Tom!!!
        """
        if self.sound is True:
            playsound('space_odyssey.mp3', False)


def start_main():
    """
    Initializes a new game board and the GUI.
    """
    game = GameBoard()
    game.place_entrance_exit()
    game.update_border_paths()

    # initialize a new game
    # ctrl = Controller()
    root = TriviaGUI(800, gameboard=game, sound=False)

    root.mainloop()


if __name__ == '__main__':
    start_main()
