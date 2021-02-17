from cell import Cell
import random


class GameBoard:
    """class creates an instance of a game board, creates 2D matrix, adds entrance
    & exit, and stores all of the locations and string representations"""
    def __init__(self, nx=4, ny=4, ix=0, iy=0):
        """initialize game board 2D matrix at (0,0)"""
        self.__nx = nx
        self.__ny = ny
        self.__ix = ix
        self.__iy = iy
        self.__current_cell = 0, 0
        self.__game_board = [[Cell(x, y) for y in range(ny)] for x in range(nx)]
        self.__entrance_cell = 0, 0
        self.__exit_cell = 0, 0
        self.original_map = ""

    def cell_at(self, x, y):
        """Return the Room string at (x,y)"""
        return self.__game_board[x][y]

    def get_nx(self):
        """return number of columns (horizontal)"""
        return self.__nx

    def get_ny(self):
        """returns the number of rows (vertical)"""
        return self.__ny

    def current_cell(self):
        """current cell pointer"""
        return self.__current_cell

    # def entrance_cell(self):
    #     """entrance getter"""
    #     return self.__entrance_cell

    def exit_cell(self):
        """exit getter"""
        return self.__exit_cell

    def move_to(self, x, y):
        """movement function in gameplay via user_input"""
        self.__current_cell = x, y

    # def find_neighbors(self, cell):
    #     """Return a list of unvisited neighbors to cell.
    #     Helper function for make_dungeon"""
    #     # options to go to find neighbors
    #     delta = [('W', (-1, 0)),
    #              ('E', (1, 0)),
    #              ('S', (0, 1)),
    #              ('N', (0, -1))]
    #     neighbors = []
    #     for direction, (dx, dy) in delta:
    #         x2, y2 = room.x + dx, room.y + dy
    #         if (0 <= x2 < self.__nx) and (0 <= y2 < self.__ny):
    #             neighbour = self.room_at(x2, y2)
    #             if neighbour.has_all_walls():
    #                 neighbors.append((direction, neighbour))
    #     return neighbors

    # def make_game_board(self):
    #     """creating game board will all open paths"""
    #     # Total number of cells
    #     n = self.__nx * self.__ny
    #     room_stack = []
    #     current_room = self.room_at(self.__ix, self.__iy)
    #     # Total number of visited rooms during maze construction
    #     nv = 1
    #
    #     # iterate over all rooms of dungeon
    #     while nv < n:
    #         neighbors = self.find_neighbors(current_room)
    #
    #         if not neighbors:
    #             # We've reached a dead end: backtrack.
    #             current_room = room_stack.pop()
    #             continue
    #
    #         # Choose a random neighboring room and move to it
    #         direction, next_room = random.choice(neighbors)
    #         current_room.remove_path(next_room, direction)
    #         room_stack.append(current_room)
    #         current_room = next_room
    #         nv += 1

    # def place_entrance(self):
    #     """places entrance on game board; currently at the 0,0 index of dungeon"""
    #     x = random.randint(0, (self.__nx - 1))
    #     y = random.randint(0, (self.__ny - 1))
    #     self.__current_room = x, y  # places adventurer in dungeon at start of game
    #     self.__entrance_room = x, y
    #     self.__maze[x][y].set_entrance(True)

    def place_entrance_exit(self):
        """set exit in game board"""
        x = 0
        y = 0
        self.__game_board[x][y].set_current_cell(True)
        a = 3
        b = 3
        self.__game_board[a][b].set_exit(True)

    def __repr__(self):
        """Return a visual string representation of the game board."""

        # A: creates northern border of game board
        board_rows = ['*' * (self.__nx * 2 + 1)]
        # B: creates a cell row for ny (except the last row)
        for y in range(self.__ny - 1):
            cell_row = ['*']
            # creates a wall if wall to the east is true (excludes last column)
            for x in range(self.__nx - 1):
                cell_row.append(self.__game_board[x][y].get_letter())
                if self.__game_board[x][y].paths['E']:
                    cell_row.append('-')
                else:
                    cell_row.append(' ')
            # creates eastern border of game board
            cell_row.append(self.__game_board[x+1][y].get_letter())
            cell_row.append('*')
            board_rows.append(''.join(cell_row))
            # C: adds rows of paths between cells if S wall is True
            cell_row = ['*']
            for x in range(self.__nx):
                # creates a path if path to the east is true
                if self.__game_board[x][y].paths['S']:
                    cell_row.append('|*')
                else:
                    cell_row.append(' *')

            board_rows.append(''.join(cell_row))

        # append last cell row of the board
        for y in range(self.__ny - 1, self.__ny):
            cell_row = ['*']
            # creates a path if path to the east is true (excludes last column)
            for x in range(self.__nx - 1):
                cell_row.append(self.__game_board[x][y].get_letter())
                if self.__game_board[x][y].paths['E']:
                    cell_row.append('-')
                else:
                    cell_row.append(' ')
            # creates eastern border of board
            cell_row.append(self.__game_board[x+1][y].get_letter())
            cell_row.append('*')
            board_rows.append(''.join(cell_row))
            # C: adds rows of paths between cells if S path is True
            cell_row = ['*']
            cell_row.append('**' * self.__nx)
            board_rows.append(''.join(cell_row))

        return '\n'.join(board_rows)

    def is_valid_room(self, x, y):
        """helper method to keep cell pointer inside the confines of the board"""
        return 0 <= x < self.__nx and 0 <= y < self.__ny

    def traverse(self):
        pass


# game_board = GameBoard()
# game_board.place_entrance_exit()
# print(game_board)
