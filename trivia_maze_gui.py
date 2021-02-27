import tkinter as tk
# from tkinter.filedialog import askopenfilename, asksaveasfilename, Tk
from PIL import ImageTk, Image
# from gameboard import GameBoard
# from view import View, INTRO
# from controller import Controller
from tkinter import *


class TriviaGUI(Frame):

    # def menu_bar(self):
    #     menu_bar = Menu(self)
    #     file_menu = Menu(menu_bar, tearoff=0)
    #     file_menu.add_command(label="New")
    #     file_menu.add_command(label="Load")
    #     file_menu.add_command(label="Save")
    #     file_menu.add_command(label="Exit")
    #     file_menu.add_cascade(label="File", menu=file_menu)
    #
    #     help_menu = Menu(self)
    #     help_menu.add_command(label="Help")
    #     help_menu.add_command(label="About")
    #     help_menu.add_cascade(label="Help", menu=help_menu)
    #
    #     return menu_bar

    def menu_widgets(self):
        self.new = Button(self, text="NEW", height=1, width=5, bg="gold",
                          fg="black", relief="raised", command=self.new)
        self.new.place(x=4, y=4)
        self.load = Button(self, text="LOAD", height=1, width=5, bg="gold",
                           fg="black", relief="raised", command=self.load)
        self.load.place(x=49, y=4)
        self.save = Button(self, text="SAVE", height=1, width=5, bg="gold",
                           fg="black", relief="raised", command=self.save)
        self.save.place(x=94, y=4)
        self.help = Button(self, text="HELP", height=1, width=5, bg="gold",
                           fg="black", relief="raised", command=self.help)
        self.help.place(x=139, y=4)
        self.exit = Button(self, text="EXIT", height=1, width=5, bg="gold",
                           fg="black", relief="raised", command=self.exit)
        self.exit.place(x=184, y=4)

    def move_widgets(self):
        self.move_up = Button(self, text="MOVE UP", height=1, width=10, bg="gold",
                              fg="black", relief="raised", command=self.move_up)
        self.move_up.place(x=585, y=140)
        self.move_down = Button(self, text="MOVE DOWN", height=1, width=10, bg="gold",
                              fg="black", relief="raised", command=self.move_down)
        self.move_down.place(x=585, y=340)
        self.move_left = Button(self, text="MOVE\nLEFT", height=2, width=6, bg="gold",
                              fg="black", relief="raised", command=self.move_left)
        self.move_left.place(x=490, y=230)
        self.move_right = Button(self, text="MOVE\nRIGHT", height=2, width=6, bg="gold",
                              fg="black", relief="raised", command=self.move_right)
        self.move_right.place(x=710, y=230)

    def legend(self):
        label = Label(self.canvas, text='LEGEND', fg='black', bg='lightskyblue1', font="bold")
        self.canvas.create_window(80, 500, window=label)
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
        # finish
        self.img4 = ImageTk.PhotoImage(file="finish.png")
        self.canvas.create_image(80, 660, image=self.img4)
        label3 = Label(self.canvas, text='Finish', fg='black', bg='lightskyblue1', font="bold")
        self.canvas.create_window(160, 660, window=label3)

    def __init__(self, dimension, master=None):
        Frame.__init__(self, master)
        Pack.config(self)
        self.master.title("Rocket Man Trivia Game")
        self.master = master
        self.dimension = dimension
        self.canvas = Canvas(self, width=dimension, height=dimension, bg="lightskyblue1")
        self.canvas.pack()
        self.show_board()
        self.show_cell()
        self.menu_widgets()
        self.move_widgets()
        self.legend()
        # self.menu_bar()

    def show_board(self):
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
        cell_1 = self.canvas.create_rectangle(x1, y1, x2, y2, fill='ivory2')
        path_1_2 = self.canvas.create_rectangle(x2, y1, x3, y2, fill='red')
        cell_2 = self.canvas.create_rectangle(x3, y1, x4, y2, fill='ivory2')
        path_2_3 = self.canvas.create_rectangle(x4, y1, x5, y2, fill='red')
        cell_3 = self.canvas.create_rectangle(x5, y1, x6, y2, fill='ivory2')
        path_3_4 = self.canvas.create_rectangle(x6, y1, x7, y2, fill='red')
        cell_4 = self.canvas.create_rectangle(x7, y1, x8, y2, fill='ivory2')

        # # Row 2
        path_1_5 = self.canvas.create_rectangle(x1, y2, x2, y3, fill='red')
        empty_1 = self.canvas.create_rectangle(x2, y2, x3, y3, fill='lightskyblue1')
        path_2__6 = self.canvas.create_rectangle(x3, y2, x4, y3, fill='red')
        empty_2 = self.canvas.create_rectangle(x4, y2, x5, y3, fill='lightskyblue1')
        path_3_7 = self.canvas.create_rectangle(x5, y2, x6, y3, fill='red')
        empty_3 = self.canvas.create_rectangle(x6, y2, x7, y3, fill='lightskyblue1')
        path_4_8 = self.canvas.create_rectangle(x7, y2, x8, y3, fill='red')

        # Row 3
        cell_5 = self.canvas.create_rectangle(x1, y3, x2, y4, fill='ivory2')
        path_5_6 = self.canvas.create_rectangle(x2, y3, x3, y4, fill='red')
        cell_6 = self.canvas.create_rectangle(x3, y3, x4, y4, fill='ivory2')
        path_6_7 = self.canvas.create_rectangle(x4, y3, x5, y4, fill='red')
        cell_7 = self.canvas.create_rectangle(x5, y3, x6, y4, fill='ivory2')
        path_7_8 = self.canvas.create_rectangle(x6, y3, x7, y4, fill='red')
        cell_8 = self.canvas.create_rectangle(x7, y3, x8, y4, fill='ivory2')

        # Row 4
        path_5_9 = self.canvas.create_rectangle(x1, y4, x2, y5, fill='red')
        empty_4 = self.canvas.create_rectangle(x2, y4, x3, y5, fill='lightskyblue1')
        path_6_10 = self.canvas.create_rectangle(x3, y4, x4, y5, fill='red')
        empty_5 = self.canvas.create_rectangle(x4, y4, x5, y5, fill='lightskyblue1')
        path_7_11 = self.canvas.create_rectangle(x5, y4, x6, y5, fill='red')
        empty_6 = self.canvas.create_rectangle(x6, y4, x7, y5, fill='lightskyblue1')
        path_8_12 = self.canvas.create_rectangle(x7, y4, x8, y5, fill='red')

        # Row 5
        cell_9 = self.canvas.create_rectangle(x1, y5, x2, y6, fill='ivory2')
        path_9_10 = self.canvas.create_rectangle(x2, y5, x3, y6, fill='red')
        cell_10 = self.canvas.create_rectangle(x3, y5, x4, y6, fill='ivory2')
        path_10_11 = self.canvas.create_rectangle(x4, y5, x5, y6, fill='red')
        cell_11 = self.canvas.create_rectangle(x5, y5, x6, y6, fill='ivory2')
        path_11_12= self.canvas.create_rectangle(x6, y5, x7, y6, fill='red')
        cell_12 = self.canvas.create_rectangle(x7, y5, x8, y6, fill='ivory2')

        # # Row 6
        path_9_13 = self.canvas.create_rectangle(x1, y6, x2, y7, fill='red')
        empty_7 = self.canvas.create_rectangle(x2, y6, x3, y7, fill='lightskyblue1')
        path_10_14 = self.canvas.create_rectangle(x3, y6, x4, y7, fill='red')
        empty_8 = self.canvas.create_rectangle(x4, y6, x5, y7, fill='lightskyblue1')
        path_11_15 = self.canvas.create_rectangle(x5, y6, x6, y7, fill='red')
        empty_9 = self.canvas.create_rectangle(x6, y6, x7, y7, fill='lightskyblue1')
        path_12_16 = self.canvas.create_rectangle(x7, y6, x8, y7, fill='red')

        # Row 7
        cell_13 = self.canvas.create_rectangle(x1, y7, x2, y8, fill='ivory2')
        path_13_14 = self.canvas.create_rectangle(x2, y7, y8, y8, fill='red')
        cell_14 = self.canvas.create_rectangle(x3, y7, x4, y8, fill='ivory2')
        path_14_15 = self.canvas.create_rectangle(x4, y7, x5, y8, fill='red')
        cell_15 = self.canvas.create_rectangle(x5, y7, x6, y8, fill='ivory2')
        path_15_16 = self.canvas.create_rectangle(x6, y7, x7, y8, fill='red')
        cell_16 = self.canvas.create_rectangle(x7, y7, x8, y8, fill='ivory2')

    def show_cell(self):
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

        # Row 1
        nw = self.canvas.create_rectangle(x1, y1, x2, y2, fill='lightskyblue1')
        n = self.canvas.create_rectangle(x2, y1, x3, y2, fill='red')
        ne = self.canvas.create_rectangle(x3, y1, x4, y2, fill='lightskyblue1')

        # Row 2
        w = self.canvas.create_rectangle(x1, y2, x2, y3, fill='red')
        center = self.canvas.create_rectangle(x2, y2, x3, y3, fill='ivory2')
        e = self.canvas.create_rectangle(x3, y2, x4, y3, fill='red')

        # Row 3
        sw = self.canvas.create_rectangle(x1, y3, x2, y4, fill='lightskyblue1')
        s = self.canvas.create_rectangle(x2, y3, x3, y4, fill='red')
        se = self.canvas.create_rectangle(x3, y3, x4, y4, fill='lightskyblue1')


    def show_question(self):
        pass

    def new(self):
        pass

    def load(self):
        pass

    def save(self):
        pass

    def help(self):
        pass

    def exit(self):
        pass

    def move_up(self):
        pass

    def move_down(self):
        pass

    def move_left(self):
        pass

    def move_right(self):
        pass


if __name__ == '__main__':
    main = TriviaGUI(800)
    main.mainloop()
