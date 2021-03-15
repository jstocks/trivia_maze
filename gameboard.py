from cell import Cell
import random


class GameBoard:
    """class creates an instance of a game board, creates 2D matrix,
    adds entrance & exit, and stores all of the locations
    and string representations"""

    def __init__(self, nx=4, ny=4, ix=0, iy=0):
        """initialize game board 2D matrix at (0,0)"""
        self.__nx = nx
        self.__ny = ny
        self.__ix = ix
        self.__iy = iy
        self.__current_cell = 0, 0
        self.__game_board = \
            [[Cell(x, y) for y in range(ny)] for x in range(nx)]
        self.__entrance_cell = 0, 0
        self.__exit_cell = 0, 0
        self.original_map = ""
        self.question_stat = []

    def set_question_stat(self, c):
        """
        Initializes the question_stat to keep track of what questions
        have been previously asked.
        :param c: Int - Number of questions
        :return: None
        """
        self.question_stat = [0 for elem in range(c)]

    def update_question_stat(self, a, value):
        """
        Updates the value at index "a" in the question stat.
        :param a: index
        :param value: Value
        :return: None
        """
        self.question_stat[a] = value

    # def get_question_stat(self):
    #     """
    #     :return: list
    #     """
    #     return self.__question_stat

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

    def set_entrance(self, x, y):
        """
        Sets the entrance
        """
        self.__entrance_cell = x, y
        self.__game_board[x][y].set_current_cell(True)

    def set_exit(self, x, y):
        """
        Sets the entrance
        """
        self.__exit_cell = x, y
        self.__game_board[x][y].set_exit(True)

    # def entrance_cell(self):
    #     """entrance getter"""
    #     return self.__entrance_cell

    def exit_cell(self):
        """exit getter"""
        return self.__exit_cell

    def move_to(self, x, y):
        """movement function in gameplay via user_input"""
        old_x, old_y = self.__current_cell
        # set property "current_cell" of the previous cell to False
        self.__game_board[old_x][old_y].set_current_cell(False)
        # and property "current_cell" of the current cell to True
        self.__game_board[x][y].set_current_cell(True)
        # set the current room to the right coordinate
        self.__current_cell = x, y

    def place_entrance_exit(self):
        """set a random entrance(first column) and exit(last column) in game board"""
        x = 0
        y = random.randrange(0, self.__ny)
        self.__game_board[x][y].set_current_cell(True)
        self.__current_cell = x, y
        self.__entrance_cell = x, y
        while True:
            a = self.__nx - 1
            b = random.randrange(0, self.__ny)
            if (a, b) != (x, y):
                self.__exit_cell = a, b
                self.__game_board[a][b].set_exit(True)
                break

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
            cell_row.append(self.__game_board[x + 1][y].get_letter())
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
            cell_row.append(self.__game_board[x + 1][y].get_letter())
            cell_row.append('*')
            board_rows.append(''.join(cell_row))
            # C: adds rows of paths between cells if S path is True
            cell_row = ['*']
            cell_row.append('**' * self.__nx)
            board_rows.append(''.join(cell_row))

        return '\n'.join(board_rows)

    def is_valid_cell(self, x, y):
        """helper method to check if the cell at x, y
        is valid ie: inside the confines of the board"""
        return 0 <= x < self.__nx and 0 <= y < self.__ny

    def traverse(self, row, col):
        """
        Performs a DFS of the maze and checks exit is reachable
        from the cell at row, col position.
        To avoid going in cycles we maintain two colors
        grey(indicates nodes in process) and
        black(indicates nodes completed processing).
        :param row: Int index
        :param col: Int index
        :return: Bool (if exit is reachable)
        """
        stack = [(row, col)]
        found_Exit = False
        grey = []
        black = []
        while len(stack) > 0:
            node = stack.pop()
            if node not in grey:
                grey.append(node)
            if self.__game_board[node[0]][node[1]].get_exit() is True:
                found_Exit = True
                return found_Exit

            trav_neighbors = []
            # if north cell is valid and path to north cell is open and
            # north cell is not in grey(to avoid cycles) and
            # not in black(to avoid traversing a previously exhausted path)
            # we add it to the trav_neighbors list for processing
            if self.is_valid_cell(node[0] - 1, node[1]) \
                    and self.cell_at(node[0], node[1]).has_west_path() is True:
                if (node[0] - 1, node[1]) not in grey \
                        and (node[0] - 1, node[1]) not in black:
                    trav_neighbors.append((node[0] - 1, node[1]))
            if self.is_valid_cell(node[0] + 1, node[1]) \
                    and self.cell_at(node[0], node[1]).has_east_path() is True:
                if (node[0] + 1, node[1]) not in grey \
                        and (node[0] + 1, node[1]) not in black:
                    trav_neighbors.append((node[0] + 1, node[1]))
            if self.is_valid_cell(node[0], node[1] - 1) and \
                    self.cell_at(node[0], node[1]).has_north_path() is True:
                if (node[0], node[1] - 1) not in grey \
                        and (node[0], node[1] - 1) not in black:
                    trav_neighbors.append((node[0], node[1] - 1))
            if self.is_valid_cell(node[0], node[1] + 1) and \
                    self.cell_at(node[0], node[1]).has_south_path() is True:
                if (node[0], node[1] + 1) not in grey \
                        and (node[0], node[1] + 1) not in black:
                    trav_neighbors.append((node[0], node[1] + 1))

            if len(trav_neighbors) > 0:
                # We add the node and its valid neighbors to the stack
                stack.append(node)
                for neighbor in trav_neighbors:
                    stack.append(neighbor)
            else:
                # no traversable neighbors and all path exhausted so we
                # finished processing this node and add it to black.
                grey.remove(node)
                black.append(node)
        return found_Exit

    def update_border_paths(self):
        """
        Updates the path of the cells in the border of the game board.
        """
        delta = [('W', (-1, 0)),
                 ('E', (1, 0)),
                 ('S', (0, 1)),
                 ('N', (0, -1))]
        # current_cell = self.cell_at(self.__ix, self.__iy)
        for i in range(self.__nx):
            for j in range(self.__ny):
                for direction, (dx, dy) in delta:
                    current_cell = self.cell_at(i, j)
                    x2, y2 = i + dx, j + dy
                    try:
                        next_cell = self.cell_at(x2, y2)
                        if x2 < 0:
                            current_cell.remove_path(next_cell, direction)
                        if x2 > self.__nx - 1:
                            current_cell.remove_path(next_cell, direction)
                        if y2 < 0:
                            current_cell.remove_path(next_cell, direction)
                        if y2 > self.__ny - 1:
                            current_cell.remove_path(next_cell, direction)
                    except IndexError:
                        pass
