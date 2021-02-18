class Cell:
    """class holds the game board cell attributes and methods to change these
    attributes, including entrance, exit, and paths"""
    path_pairs = {"N": "S", "S": "N", "E": "W", "W": "E"}

    def __init__(self, x, y):
        self.__exit = False
        # self.__entrance = False
        self.__current_cell = False
        self.__impassable = False
        # self.__visited = False
        self.x = x
        self.y = y
        self.paths = {"N": True, "S": True, "E": True, "W": True}

    def get_exit(self):
        """getter for exit"""
        return self.__exit

    def set_exit(self, add_exit):
        """setter for exit"""
        self.__exit = add_exit

    # def get_entrance(self):
    #     """getter for entrance"""
    #     return self.__entrance
    #
    # def set_entrance(self, add_entrance):
    #     """setter for entrance"""
    #     self.__entrance = add_entrance

    def get_current_cell(self):
        """getter for current cell"""
        return self.__current_cell

    def set_current_cell(self, update_current_cell):
        """setter for current cell"""
        self.__current_cell = update_current_cell

    def set_visited(self, add_visited):
        """setter for visited room, used for maze creation"""
        self.__visited = add_visited

    def reset_visited(self):
        """setter for visited"""
        self.__visited = False

    def is_visited(self):
        """getter for visited"""
        return self.__visited is True

    def __repr__(self):
        return "Paths: " + str(self.paths) + "\n" \
            + "Exit: " + str(self.__exit) + "\n" \
            + "Impassable: " + str(self.__impassable) + "\n"

    def has_all_paths(self):
        """returns True if Room has all 4 paths"""
        return all(self.paths.values())

    def has_north_path(self):
        """getter for north path"""
        return self.paths["N"]

    def has_south_path(self):
        """getter for south path"""
        return self.paths["S"]

    def has_east_path(self):
        """getter for east path"""
        return self.paths["E"]

    def has_west_path(self):
        """getter for west path"""
        return self.paths["W"]

    def remove_path(self, other, path):
        """Removes the path between two adjacent cells."""
        self.paths[path] = False
        other.paths[Cell.path_pairs[path]] = False

    def get_letter(self):
        """getters for dungeon representation"""
        if self.__exit:
            return "o"
        if self.__current_cell:
            return "x"
        else:
            return " "
