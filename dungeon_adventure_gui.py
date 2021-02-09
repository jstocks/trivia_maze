from tkinter import *
from PIL import Image, ImageTk
from tkinter import messagebox
from tkinter.simpledialog import askstring
from tkinter.messagebox import showinfo
from dungeon import Dungeon

tk = Tk()
tk.geometry('680x700')
tk.title("THE Dungeon OF Doom by Jeff-Dee-Kishan")

frame = Frame(tk, relief='raised', borderwidth=2)
frame.pack(fill=BOTH, expand=YES)
frame.pack_propagate(False)

HD_DOOM = 'THE Dungeon OF Doom'
FONT_B = ('Courier New', 18, 'bold')
FONT = ('Courier New', 18)
BGB = 'black'
FGG = 'green'
FGY = 'yellow'
BGW = 'white'
FGB = 'black'

INTRO = "\n Welcome to the Dungeon of Doom!  Prepare for the most difficult\n" \
                "challenge of your adventure-seeking life.  Check your pride at the door,\n" \
                "and bring an extra ounce of courage as you face off against countless\n" \
                "pits and race against your own agony to capture the elusive.......\n" \
                "*****  Four Pillars of Object-Oriented Programming *****\n"

HOWTOPLAY = "The goal of this game is to escape the dungeon maze after finding the\n" \
                  "four pillars:\n" \
                  "   1: Abstraction\n" \
                  "   2: Encapsulation\n" \
                  "   3: Inheritance\n" \
                  "   4: Polymorphism\n\n" \
                  "Be warned - you have limited health points [HP]. If you fall in a pit, you\n" \
                  "will lose HP. Don't fret - there are also Healing Potions and Vision\n" \
                  "Potions scattered about the dungeon to help you in your quest. Once you\n" \
                  "collect all Four Pillars of OO, the exit door will unlock --- if you reach\n" \
                  "the exit before your HP reaches a big fat zero, you win!\n\n" \
                  "You can move throughout the map by typing \'u\', \'d\', \'l\', or \'r\'\n" \
                  "You can only move through the doors that exist in the dungeon.\n\n" \
                  "Be strong in your journey...\n\"Even death is not to be feared by one who " \
                  "has lived wisely\" --- Buddha\n"


class DungeonAdventure:

    def __init__(self):
        self.__player_name = ''
        self.__difficult_level = 0
        self.__active = True
        self.game_active()

    def user_name(self):
        return self.__player_name

    # ------------------------------------------------------
    # This is the main method for THE DUNGEON OF DOOOM game
    # ------------------------------------------------------
    def playing(self):

        def resize_image(event):
            new_width = event.width
            new_height = event.height

            image = copy_of_image.resize((new_width, new_height))
            photo = ImageTk.PhotoImage(image)

            label.config(image=photo)
            label.image = photo  # avoid garbage collection

        def what_is_your_name():
            self.__player_name = askstring(HD_DOOM, 'Identify Yourself!')
            if self.__player_name is None:
                showinfo('THE Dungeon OF Doom', "Don't be shy. Name is required to the start the game !!!")
            else:
                self.game_active()

        def how_to():
            messagebox.showinfo("THE Dungeon OF Doom", HOWTOPLAY)

        # ----------------------------------------------------
        # ------------- Introduction Page --------------------
        # ----------------------------------------------------
        copy_of_image = Image.open("wizard.jpg")
        photo = ImageTk.PhotoImage(copy_of_image)

        label = Label(frame, image=photo)
        label.place(x=0, y=0, relwidth=1, relheight=1)
        label.bind('<Configure>', resize_image)

        center_frame = Frame(frame, relief='raised', borderwidth=8, bg=BGB, width=80)
        center_frame.place(relx=.5, rely=.5, anchor=CENTER)

        # ---------------- introduction -----------------
        Label(center_frame, text=INTRO, width=60, bg=BGB, fg=FGY).pack()

        # ------------- "Let's the game begin..." buttons --------------------
        bottom_frame = Frame(tk)
        bottom_frame.pack(side=BOTTOM)
        start_button = Button(center_frame,
                              text="CLICK TO START",
                              bg=BGW,
                              font=FONT,
                              command=what_is_your_name)

        start_button.pack(side=BOTTOM)

        # ----------------------------------------------------------------------------
        # ------------ After get a play name, start the game -------------------------
        # ----------------------------------------------------------------------------
        if self.__player_name != '':

            center_frame.pack_forget()
            copy_of_image = Image.open("Maze.jpg")
            photo = ImageTk.PhotoImage(copy_of_image)

            label = Label(frame, image=photo)
            label.place(x=0, y=0, relwidth=1, relheight=1)
            label.bind('<Configure>', resize_image)

            center_frame = Frame(frame, relief='raised', borderwidth=5, bg=BGB, width=80)
            center_frame.place(relx=.5, rely=.5, anchor=CENTER)

            howto_button = Button(frame, text="How to play...", bg=BGW, font=FONT, command=how_to)
            howto_button.pack(side=TOP)

            # -----------------------------------------------------------
            # ----------------- Difficulty Level ------------------------
            # -----------------------------------------------------------

            Label(center_frame, text=self.__player_name, bg=BGB, fg=FGY, font=FONT).pack()
            Label(center_frame, text="You are about to enter THE DUNGEON OF DOOM.", bg=BGB, fg=FGY, font=FONT).pack()
            Label(center_frame, text="Select a difficulty from 1 (Easy) to 5 (Hard)", bg=BGB, fg=FGY, font=FONT).pack()
            Label(center_frame, bg=BGB).pack()

            # ------------ Get player input on the difficult Level  ------------------
            player_level = Entry(center_frame)
            player_level.pack()

            Label(center_frame, bg=BGB).pack()  # create space in between

            def get_level():
                self.__difficult_level = player_level.get()
                tk.after(20, self.game_active())

            btn_start = Button(center_frame, text="GO", bg=BGW, fg=FGB, font=FONT_B, command=get_level)
            btn_start.pack()

            # -------------------------------------------------
            # ---------------- Start Playing ------------------
            # -------------------------------------------------
            if 0 < int(self.__difficult_level) < 6:

                # ---------- Clean every things in the frame --------
                center_frame.pack_forget()

                # -------- Change the background -------
                copy_of_image = Image.open("Pillars.jpg")
                photo = ImageTk.PhotoImage(copy_of_image)

                label = Label(frame, image=photo)
                label.place(x=0, y=0, relwidth=1, relheight=1)
                label.bind('<Configure>', resize_image)

                # -------- put it in the center of the frame --------
                center_frame = Frame(frame, relief='raised', borderwidth=5, bg=BGB, width=80)
                center_frame.place(relx=.5, rely=.5, anchor=CENTER)

                # ------------------ Difficult Level Maze -------------------
                game_board = Dungeon(5, 5, 0, 0)
                if int(self.__difficult_level) == 1:
                    game_board = Dungeon(5, 5, 0, 0)
                elif int(self.__difficult_level) == 2:
                    game_board = Dungeon(6, 6, 0, 0)
                elif int(self.__difficult_level) == 3:
                    game_board = Dungeon(7, 7, 0, 0)
                elif int(self.__difficult_level) == 4:
                    game_board = Dungeon(8, 8, 0, 0)
                elif int(self.__difficult_level) == 5:
                    game_board = Dungeon(10, 10, 0, 0)
                else:
                    game_board = Dungeon(5, 5, 0, 0)

                game_board.make_dungeon()
                game_board.place_dungeon_items()
                # -------- To Do -----------
                # while game_board.traverse() is not True:
                #     game_board.make_dungeon()
                #     game_board.place_dungeon_items()

                Label(center_frame, text=game_board, bg=BGB, fg=FGY, font=("Courier New", 18)).pack()

                # ------------------- Show the Items in the Dungeon --------------------
                bottom_frame1 = Frame(tk)
                bottom_frame1.pack(side=TOP)

                # ---------------------- if not MAC computer, uncomment this -----------------------
                # Button(bottom_frame, text="Pillar A", fg=FGG).pack(side=LEFT)
                # Button(bottom_frame, text="Pillar E", fg=FGG).pack(side=LEFT)
                # Button(bottom_frame, text="Pillar I", fg=FGG).pack(side=LEFT)
                # Button(bottom_frame, text="Pillar P", fg=FGG).pack(side=LEFT)

                Button(bottom_frame1, text="Use HEALING Potion", highlightbackground='#3E4149').pack(side=LEFT)
                Button(bottom_frame1, text="Use VISION Potion", highlightbackground='#3E4149').pack(side=LEFT)
                Button(bottom_frame1, text="Map Key", highlightbackground='#3E4149').pack(side=LEFT)
                Button(bottom_frame1, text="       ", bd=0).pack(side=LEFT)


                bottom_frame2 = Frame(tk)
                bottom_frame2.pack(side=TOP)
                Button(bottom_frame2, text="Move Up", highlightbackground='#3E4149').pack(side=LEFT)
                Button(bottom_frame2, text="Move Down", highlightbackground='#3E4149').pack(side=LEFT)
                Button(bottom_frame2, text="Move Left", highlightbackground='#3E4149').pack(side=LEFT)
                Button(bottom_frame2, text="Move Right", highlightbackground='#3E4149').pack(side=LEFT)

                # ------------------ Place "How to Play" button -------------------
                Button(bottom_frame2,
                       text="How to play",
                       highlightbackground='#3E4149',
                       command=how_to).pack(side=LEFT)

                def exit_game():
                    tk.quit()

                Button(bottom_frame2,
                       text="Exit The Game",
                       highlightbackground='#3E4149',
                       command=exit_game).pack(side=LEFT)

    def game_active(self):
        if self.__active:
            self.playing()


da = DungeonAdventure()
tk.mainloop()