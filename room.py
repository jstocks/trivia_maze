"""room creation inspired by https://github.com/scipython/scipython-maths/blob/
master/maze/df_maze.py"""


class Room:
    """class holds the Room attributes and methods to change these attributes,
    including all of the items and walls"""
    wall_pairs = {"N": "S", "S": "N", "E": "W", "W": "E"}

    def __init__(self, x, y):
        self.__healing_potion = False
        self.__pit = False
        self.__pillar_a = False
        self.__pillar_e = False
        self.__pillar_i = False
        self.__pillar_p = False
        self.__vision_potion = False
        self.__exit = False
        self.__entrance = False
        self.__impassable = False
        self.__visited = False
        self.__item_count = 0
        self.x = x
        self.y = y
        self.walls = {"N": True, "S": True, "E": True, "W": True}

    def get_healing_potion(self, ):
        """getter for healing potion"""
        return self.__healing_potion

    def set_healing_potion(self, add_potion):
        """setter for healing potion"""
        self.__healing_potion = add_potion
        if add_potion:
            self.__item_count += 1
        else:
            self.__item_count -= 1

    def get_pit(self):
        """getter for pit"""
        return self.__pit

    def set_pit(self, fall_in):
        """setter for pit"""
        self.__pit = fall_in
        if fall_in:
            self.__item_count += 1
        else:
            self.__item_count -= 1

    def get_pillar_a(self):
        """getter for pillar a"""
        return self.__pillar_a

    def set_pillar_a(self, add_pillar_a):
        """setter for pillar a"""
        self.__pillar_a = add_pillar_a
        if add_pillar_a:
            self.__item_count += 1
        else:
            self.__item_count -= 1

    def get_pillar_e(self):
        """getter for pillar e"""
        return self.__pillar_e

    def set_pillar_e(self, add_pillar_e):
        """setter for pillar e"""
        self.__pillar_e = add_pillar_e
        if add_pillar_e:
            self.__item_count += 1
        else:
            self.__item_count -= 1

    def get_pillar_i(self):
        """getter for pillar i"""
        return self.__pillar_i

    def set_pillar_i(self, add_pillar_i):
        """setter for pillar i"""
        self.__pillar_i = add_pillar_i
        if add_pillar_i:
            self.__item_count += 1
        else:
            self.__item_count -= 1

    def get_pillar_p(self):
        """getter for pillar p"""
        return self.__pillar_p

    def set_pillar_p(self, add_pillar_p):
        """setter for pillar p"""
        self.__pillar_p = add_pillar_p
        if add_pillar_p:
            self.__item_count += 1
        else:
            self.__item_count -= 1

    def get_vision_potion(self):
        """getter for vision potion"""
        return self.__vision_potion

    def set_vision_potion(self, add_vision):
        """setter for vision potion"""
        self.__vision_potion = add_vision
        if add_vision:
            self.__item_count += 1
        else:
            self.__item_count -= 1

    def get_exit(self):
        """getter for exit"""
        return self.__exit

    def set_exit(self, add_exit):
        """setter for exit"""
        self.__exit = add_exit

    def get_entrance(self):
        """getter for entrance"""
        return self.__entrance

    def set_entrance(self, add_entrance):
        """setter for entrance"""
        self.__entrance = add_entrance

    def set_visited(self, add_visited):
        """setter for visited room, used for maze creation"""
        self.__visited = add_visited

    def reset_visited(self):
        """setter for visited"""
        self.__visited = False

    def is_visited(self):
        """getter for visited"""
        return self.__visited is True

    def is_multiple_item(self):
        """getter for M if room has multiple items"""
        return self.__item_count > 1

    def has_a_pillar(self):
        """getter for if a room contains a pillar"""
        if self.__pillar_a or self.__pillar_e or self.__pillar_i or self.__pillar_p:
            return True
        else:
            return False

    def __repr__(self):
        return "Walls: " + str(self.walls) + "\n" \
            + "Healing Potion: " + str(self.__healing_potion) + "\n" \
            + "Pit: " + str(self.__pit) + "\n" \
            + "Pillar A: " + str(self.__pillar_a) + "\n" \
            + "Pillar E: " + str(self.__pillar_e) + "\n" \
            + "Pillar I: " + str(self.__pillar_i) + "\n" \
            + "Pillar P: " + str(self.__pillar_p) + "\n" \
            + "Vision: " + str(self.__vision_potion) + "\n" \
            + "Exit: " + str(self.__exit) + "\n" \
            + "Entrance: " + str(self.__entrance) + "\n" \
            + "Impassable: " + str(self.__impassable) + "\n" \
            + "Visited: " + str(self.__visited)

    def has_all_walls(self):
        """returns True if Room has all 4 walls"""
        return all(self.walls.values())

    def has_north_wall(self):
        """getter for north wall"""
        return self.walls["N"]

    def has_south_wall(self):
        """getter for south wall"""
        return self.walls["S"]

    def has_east_wall(self):
        """getter for east wall"""
        return self.walls["E"]

    def has_west_wall(self):
        """getter for west wall"""
        return self.walls["W"]

    def connect(self, other, wall):
        """Removes the wall between two adjacent cells."""
        self.walls[wall] = False
        other.walls[Room.wall_pairs[wall]] = False

    def get_letter(self):
        """getters for dungeon representation"""
        if self.__entrance:
            return "i"
        if self.__exit:
            return "o"
        if self.__item_count > 1:
            return "M"

        # we have 1 item
        if self.__healing_potion:
            return "H"
        elif self.__vision_potion:
            return "V"
        elif self.__pit:
            return "X"
        elif self.__pillar_a:
            return "A"
        elif self.__pillar_e:
            return "E"
        elif self.__pillar_i:
            return "I"
        elif self.__pillar_p:
            return "P"
        else:
            return " "
