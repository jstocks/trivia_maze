""" maze creation inspired by https://github.com/scipython/scipython-maths/blob/
master/maze/df_maze.py"""

from room import Room
import random


class Dungeon:
    """class creates an instance of a dungeon, creates matrix, removes walls between
    rooms, adds items, and stores all of the locations and string representations"""
    def __init__(self, nx, ny, ix=0, iy=0):
        """initialize dungeon 2D matrix at (0,0)"""
        self.__nx = nx
        self.__ny = ny
        self.__ix = ix
        self.__iy = iy
        self.__current_room = 0, 0
        self.__maze = [[Room(x, y) for y in range(ny)] for x in range(nx)]
        self.__entrance_room = 0, 0
        self.__exit_room = 0, 0
        self.__pillar_a = 0, 0
        self.__pillar_e = 0, 0
        self.__pillar_i = 0, 0
        self.__pillar_p = 0, 0
        self.count = 0
        self.original_map = ""

    def room_at(self, x, y):
        """Return the Room string at (x,y)"""
        return self.__maze[x][y]

    def get_nx(self):
        """return number of columns (horizontal)"""
        return self.__nx

    def get_ny(self):
        """returns the number of rows (vertical)"""
        return self.__ny

    def current_room(self):
        """current room pointer"""
        return self.__current_room

    def entrance_room(self):
        """entrance getter"""
        return self.__entrance_room

    def exit_room(self):
        """exit getter"""
        return self.__exit_room

    def pillar_a_room(self):
        """pillar A room getter"""
        return self.__pillar_a

    def pillar_e_room(self):
        """pillar E room getter"""
        return self.__pillar_e

    def pillar_i_room(self):
        """pillar I room getter"""
        return self.__pillar_i

    def pillar_p_room(self):
        """pillar P room getter"""
        return self.__pillar_p

    def move_to(self, x, y):
        """movement function in dungeon_adventure via user_input"""
        self.__current_room = x, y

    def find_neighbors(self, room):
        """Return a list of unvisited neighbors to room.
        Helper function for make_dungeon"""
        # options to go to find neighbors
        delta = [('W', (-1, 0)),
                 ('E', (1, 0)),
                 ('S', (0, 1)),
                 ('N', (0, -1))]
        neighbors = []
        for direction, (dx, dy) in delta:
            x2, y2 = room.x + dx, room.y + dy
            if (0 <= x2 < self.__nx) and (0 <= y2 < self.__ny):
                neighbour = self.room_at(x2, y2)
                if neighbour.has_all_walls():
                    neighbors.append((direction, neighbour))
        return neighbors

    def make_dungeon(self):
        """creating dungeon via removing wall pairs between rooms;
        makes all rooms accessible"""
        # Total number of rooms
        n = self.__nx * self.__ny
        room_stack = []
        current_room = self.room_at(self.__ix, self.__iy)
        # Total number of visited rooms during maze construction
        nv = 1

        # iterate over all rooms of dungeon
        while nv < n:
            neighbors = self.find_neighbors(current_room)

            if not neighbors:
                # We've reached a dead end: backtrack.
                current_room = room_stack.pop()
                continue

            # Choose a random neighboring room and move to it
            direction, next_room = random.choice(neighbors)
            current_room.connect(next_room, direction)
            room_stack.append(current_room)
            current_room = next_room
            nv += 1

    def place_dungeon_items(self):
        """ places all dungeon items into the created dungeon"""
        self.place_entrance()
        self.place_exit()
        self.place_pillar_a()
        self.place_pillar_e()
        self.place_pillar_i()
        self.place_pillar_p()
        self.place_pits()
        self.place_vision()
        self.place_healing()
        self.original_map = self.__repr__()

    def place_entrance(self):
        """places entrance in dungeon; currently at the 0,0 index of dungeon"""
        x = random.randint(0, (self.__nx - 1))
        y = random.randint(0, (self.__ny - 1))
        self.__current_room = x, y  # places adventurer in dungeon at start of game
        self.__entrance_room = x, y
        self.__maze[x][y].set_entrance(True)

    def place_exit(self):
        """set exit in dungeon"""
        x = random.randint(0, (self.__nx - 1))
        y = random.randint(0, (self.__ny - 1))
        self.__exit_room = x, y
        if self.exit_room() == self.pillar_a_room() or \
                self.exit_room() == self.pillar_e_room() or \
                self.exit_room() == self.pillar_i_room() or \
                self.exit_room() == self.pillar_p_room() or \
                self.exit_room() == self.entrance_room():
            return self.place_exit()
        self.__maze[x][y].set_exit(True)

    def place_pillar_a(self):
        """set pillar A in dungeon, can't be in entrance, exit, or with any other pillar"""
        x = random.randint(0, (self.__nx - 1))
        y = random.randint(0, (self.__ny - 1))
        self.__pillar_a = x, y
        if self.pillar_a_room() == self.pillar_e_room() or \
                self.pillar_a_room() == self.pillar_i_room() or \
                self.pillar_a_room() == self.pillar_p_room() or \
                self.pillar_a_room() == self.entrance_room() or \
                self.pillar_a_room() == self.exit_room():
            return self.place_pillar_a()
        self.__maze[x][y].set_pillar_a(True)

    def place_pillar_e(self):
        """set pillar E in dungeon, can't be in entrance, exit, or with any other pillar"""
        x = random.randint(0, (self.__nx - 1))
        y = random.randint(0, (self.__ny - 1))
        self.__pillar_e = x, y
        if self.pillar_e_room() == self.pillar_a_room() or \
                self.pillar_e_room() == self.pillar_i_room() or \
                self.pillar_e_room() == self.pillar_p_room() or \
                self.pillar_e_room() == self.entrance_room() or \
                self.pillar_e_room() == self.exit_room():
            return self.place_pillar_e()
        self.__maze[x][y].set_pillar_e(True)

    def place_pillar_i(self):
        """set pillar I in dungeon, can't be in entrance, exit, or with any other pillar"""
        x = random.randint(0, (self.__nx - 1))
        y = random.randint(0, (self.__ny - 1))
        self.__pillar_i = x, y
        if self.pillar_i_room() == self.pillar_a_room() or \
                self.pillar_i_room() == self.pillar_e_room() or \
                self.pillar_i_room() == self.pillar_p_room() or \
                self.pillar_i_room() == self.entrance_room() or \
                self.pillar_i_room() == self.exit_room():
            return self.place_pillar_i()
        self.__maze[x][y].set_pillar_i(True)

    def place_pillar_p(self):
        """set pillar P in dungeon, can't be in entrance, exit, or with any other pillar"""
        x = random.randint(0, (self.__nx - 1))
        y = random.randint(0, (self.__ny - 1))
        self.__pillar_p = x, y
        if self.pillar_p_room() == self.pillar_a_room() or \
                self.pillar_p_room() == self.pillar_e_room() or \
                self.pillar_p_room() == self.pillar_i_room() or \
                self.pillar_p_room() == self.entrance_room() or \
                self.pillar_p_room() == self.exit_room():
            return self.place_pillar_p()
        self.__maze[x][y].set_pillar_p(True)

    def place_pits(self, probability=0.1):
        """set pits in dungeon, can't be in same room as entrance, exit"""
        number = int((self.__nx * self.__ny) * probability)  # probability of having a pit
        for i in range(number):
            x = random.randint(0, (self.__nx - 1))
            y = random.randint(0, (self.__ny - 1))
            if self.__maze[x][y] != self.entrance_room() and \
                    self.__maze[x][y] != self.exit_room():
                self.__maze[x][y].set_pit(True)

    def place_healing(self, probability=0.1):
        """set healing in dungeon; can't be in entrance, exit"""
        number = int((self.__nx * self.__ny) * probability)  # probability of having a pit
        for i in range(number):
            x = random.randint(0, (self.__nx - 1))
            y = random.randint(0, (self.__ny - 1))
            if self.__maze[x][y] != self.entrance_room() and \
                    self.__maze[x][y] != self.exit_room():
                self.__maze[x][y].set_healing_potion(True)

    def place_vision(self, probability=0.1):
        """set vision potion in dungeon, can't be in entrance or exit"""
        number = int((self.__nx * self.__ny) * probability)  # probability of having a pit
        for i in range(number):
            x = random.randint(0, (self.__nx - 1))
            y = random.randint(0, (self.__ny - 1))
            if self.__maze[x][y] != self.entrance_room() and \
                    self.__maze[x][y] != self.exit_room():
                self.__maze[x][y].set_vision_potion(True)

    def __repr__(self):
        """Return a visual string representation of the maze."""

        # A: creates northern border of dungeon
        dungeon_rows = ['*' * (self.__nx * 2 + 1)]
        # B: creates a maze row for ny (except the last row)
        for y in range(self.__ny - 1):
            maze_row = ['*']
            # creates a wall if wall to the east is true (excludes last column)
            for x in range(self.__nx - 1):
                maze_row.append(self.__maze[x][y].get_letter())
                if self.__maze[x][y].walls['E']:
                    maze_row.append('|')
                else:
                    maze_row.append(' ')
            # creates eastern border of dungeon
            maze_row.append(self.__maze[x+1][y].get_letter())
            maze_row.append('*')
            dungeon_rows.append(''.join(maze_row))
            # C: adds rows of walls between rooms if S wall is True
            maze_row = ['*']
            for x in range(self.__nx):
                # creates a wall if wall to the east is true
                if self.__maze[x][y].walls['S']:
                    maze_row.append('-*')
                else:
                    maze_row.append(' *')

            dungeon_rows.append(''.join(maze_row))

        # append last room of the maze
        for y in range(self.__ny - 1, self.__ny):
            maze_row = ['*']
            # creates a wall if wall to the east is true (excludes last column)
            for x in range(self.__nx - 1):
                maze_row.append(self.__maze[x][y].get_letter())
                if self.__maze[x][y].walls['E']:
                    maze_row.append('|')
                else:
                    maze_row.append(' ')
            # creates eastern border of dungeon
            maze_row.append(self.__maze[x+1][y].get_letter())
            maze_row.append('*')
            dungeon_rows.append(''.join(maze_row))
            # C: adds rows of walls between rooms if S wall is True
            maze_row = ['*']
            maze_row.append('**' * self.__nx)
            dungeon_rows.append(''.join(maze_row))

        return '\n'.join(dungeon_rows)

    def is_valid_room(self, x, y):
        """helper method to keep room pointer inside the confines of the dungeon"""
        return 0 <= x < self.__nx and 0 <= y < self.__ny

    def count_pillars_and_exit(self, x, y):
        """method to traverse the dungeon, and continues until it finds all 4 pillars
        and the exit; returns a count - should be 5"""

        if not self.is_valid_room(x, y) or self.__maze[x][y].is_visited():
            return 0

        # check for exit or any pillar
        item_count = 0
        if self.__maze[x][y].get_exit():
            item_count = 1
        elif self.__maze[x][y].get_pillar_a():
            item_count = 1
        elif self.__maze[x][y].get_pillar_e():
            item_count = 1
        elif self.__maze[x][y].get_pillar_i():
            item_count = 1
        elif self.__maze[x][y].get_pillar_p():
            item_count = 1

        # not at exit so try another room: south, east, north, west
        self.__maze[x][y].set_visited(True)
        # if east_wall is not true, then we can go row +1
        if self.__maze[x][y].walls['E'] is False:
            item_count += self.count_pillars_and_exit(x + 1, y)
        if self.__maze[x][y].walls['S'] is False:
            item_count += self.count_pillars_and_exit(x, y + 1)
        if self.__maze[x][y].walls['W'] is False:
            item_count += self.count_pillars_and_exit(x - 1, y)
        if self.__maze[x][y].walls['N'] is False:
            item_count += self.count_pillars_and_exit(x, y - 1)

        return item_count

    def traverse(self):
        """traverses dungeon and looks for a count (5) to demonstrate it found all
         4 pillars and the exit; returns false if it can't find all 5; used in
         dungeon_adventure during dungeon creation - if this returns false, it will
         create a new traversable dungeon"""
        return self.count_pillars_and_exit(0, 0) == 5

    def print_maze_contents(self):
        """ prints all rooms and room contents as booleans"""
        for row in range(0, self.__ny):
            print("row ", row)
            for col in range(0, self.__nx):
                print(self.__maze[row][col].__str__())
            print()

