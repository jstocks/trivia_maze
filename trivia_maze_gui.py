# from tkinter import *
#
# # create the canvas, size in pixels
# canvas = Canvas(width=300, height=200, bg='black')
#
# # pack the canvas into a frame/form
# canvas.pack(expand=YES, fill=BOTH)
#
# # load the .gif image file
# gif1 = PhotoImage(file='rocket_man.gif')
#
# # put gif image on canvas
# # pic's upper left corner (NW) on the canvas is at x=50 y=10
# canvas.create_image(50, 10, image=gif1, anchor=NW)
#
# # run it ...
# mainloop()

import tkinter as tk
from tkinter.filedialog import askopenfilename, asksaveasfilename, Tk
from tkinter import *
from PIL import ImageTk, Image
from gameboard import GameBoard
from view import View, INTRO
from controller import Controller

from tkinter import Tk, Canvas, Frame, BOTH


class Example(Frame):

    def __init__(self):
        super().__init__()

        self.IMAGE_BACKGROUND = PhotoImage(file='rocket_man.gif')

        self.init_gui()


    def init_gui(self):

        self.master.title("Rocket Man Trivia Game")
        self.pack(fill=BOTH, expand=1)

        self.canvas = Canvas(self)
        self.canvas.pack(expand=YES, fill=BOTH)
        # self.canvas.create_line(15, 25, 200, 25)
        # Room_A = self.canvas.create_line(300, 35, 300, 200, dash=(4, 2))
        # self.canvas.create_line(55, 85, 155, 85, 105, 180, 55, 85)
        # self.canvas.create_text(20, 30, anchor="w", font="Purisa", text="Most relationships seem so transitory")
        # self.canvas.create_image(50, 10, image=background, anchor=NW)

        self.canvas.create_image(50, 10, image=self.IMAGE_BACKGROUND, anchor=NW)



        # print(self.canvas.find_all())
        #
        self.menu_bar = self.create_menu(self.master)
        self.master.config(menu=self.menu_bar)

        self.canvas.pack(fill=BOTH, expand=1)

        self.mainloop()

    def create_menu(self, main):
        menu_bar = Menu(main)
        menu_file = Menu(menu_bar, tearoff=0)
        menu_file.add_command(label="New", command=self.command_new_game)
        menu_bar.add_cascade(label="File", menu=menu_file)
        return menu_bar

    # def draw_background(self):
    #     self.canvas.create_image(50, 10, image=self.IMAGE_BACKGROUND, anchor=NW)

    def command_new_game(self):
        print("NEW GAME")

def main():

    root = Tk()
    ex = Example()
    root.mainloop()


if __name__ == '__main__':
    main()

# class TriviaMazeGUI(Frame):
#
#     def __init__(self):
#         super().__init__()
#         self.master.title("Rocket Man Trivia Game")
#
#         self.canvas = Canvas(self)
#         self.canvas.create_line(0, 0, 500, 500)
#         self.pack()
#         #self.canvas.grid(row=0, column=0, sticky="nw")
#
#         self.maze_menu = self.create_menu(self.master)
#         self.master.config(menu=self.maze_menu)
#         self.master.mainloop()
#
#         # # window grid configurations
#         # self.top_frame = ttk.Frame(main)
#         # self.top_frame.grid(column=0, row=0, sticky="N, S, E, W")
#         # self.main.columnconfigure(0, weight=1)
#         # self.main.rowconfigure(0, weight=1)
#
#         # # menu buttons config
#         # self.frame_a_buttons = ttk.Frame(self.top_frame, relief=tk.RAISED, borderwidth=0)
#         # self.button_new = ttk.Button(self.frame_a_buttons, text="New", command=self.new_game)
#         # self.button_load = ttk.Button(self.frame_a_buttons, text="Load", command=self.load_game)
#         # self.button_save = ttk.Button(self.frame_a_buttons, text="Save", command=self.save_game)
#         # self.button_help = ttk.Button(self.frame_a_buttons, text="Help", command=self.help_menu)
#         # self.button_exit = ttk.Button(self.frame_a_buttons, text="Exit", command=self.exit_game)
#         #
#         # # menu buttons grid
#         # self.button_new.grid(row=0, column=0, sticky="ew")
#         # self.button_load.grid(row=0, column=1, sticky="ew")
#         # self.button_save.grid(row=0, column=2, sticky="ew")
#         # self.button_help.grid(row=0, column=3, sticky="ew")
#         # self.button_exit.grid(row=0, column=4, sticky="ew")
#         #
#         # self.frame_a_buttons.grid(row=0, column=0, sticky="nw")
#         # self.button_new.focus()  # cursor starts on New button
#
#
#
#         # intro picture
#         # self.splash = ImageTk.PhotoImage(Image.open("rocket_man.jpeg"))
#         #
#         # self.rocket_man_frame = tk.Label(image=self.splash)
#         # self.rocket_man_frame.image = self.splash
#         # self.rocket_man_frame.grid(row=1, column=0, sticky="nw")
#
#         #self.main.mainloop()
#
#     def create_menu(self, main):
#         menu_bar = Menu(main)
#         menu_file = Menu(menu_bar, tearoff=0)
#         menu_file.add_command(label="New", command=self.new_game)
#         menu_bar.add_cascade(label="File", menu=menu_file)
#         return menu_bar
#
#     def new_game(self):
#         """start a new game"""
#
#         #new = Controller()
#         #new.init_game()
#
#         welcome_frame = ttk.Frame(self.main, relief=tk.RAISED, borderwidth=0)
#         #welcome = ttk.Label(welcome_frame, text=View.display_welcome_msg())
#         welcome = ttk.Label(welcome_frame, text=INTRO)
#         welcome.grid(row=1, column=0)
#
#         # self.rocket_man_frame.grid_forget()
#         self.rocket_man_frame.config(image='', text=INTRO)
#
#     @staticmethod
#     def load_game(self):
#         """Load a game from a previously saved game."""
#         filepath = askopenfilename(
#             filetypes=[("All Files", "*.*")]
#         )
#         if not filepath:
#             return
#         with open(filepath, "r") as input_file:
#             pass
#
#     @staticmethod
#     def save_game(self):
#         """Save the current game as a new file."""
#         filepath = asksaveasfilename(
#             defaultextension="",
#             filetypes=[("All Files", "*.*")],
#         )
#         if not filepath:
#             return
#         with open(filepath, "w") as output_file:
#             # info = x
#             # output_file.write(info)
#             pass
#
#     def help_menu(self):
#         """Display the help menu and instructions of the game."""
#         pass
#
#     def exit_game(self):
#
#         pass
#
#     def select_level(self):
#         pass
#
#
# root = Tk()
# TriviaMazeGUI()
# root.mainloop()  # run the event loop
