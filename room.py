from obstacle import Obstacle
from vision_potion import VisionPotion
from healing_potion import HealingPotion


class Room:

    def __init__(self):
        """
        Abstract base class for a room, should not be
        used for a concrete object.
        """
        self.__features = []
        self.__treasure = False  # A I P E
        self.__is_entrance = False
        self.__is_exit = False
        self.__is_impassable = False
        self.__visited = False
        self.__explored = False
        self.__current_pos = False

    def __str__(self):
        """
        Returns string representation of the current room and features
        """
        if self.__is_entrance:
            return "i: Entrance"
        elif self.__is_exit:
            return "O: Exit"
        elif self.__is_impassable:
            return "B: No Room (Blocked)"
        elif self.__treasure:
            return str(self.__treasure[0]) + ": " + str(self.__treasure)
        elif len(self.__features) > 1:
            return "M: Multiple Features"
        elif len(self.__features):
            if type(self.__features[0]) == HealingPotion:
                return "H: Healing Potion"
            elif type(self.__features[0]) == VisionPotion:
                return "V: Vision Potion"
            elif type(self.__features[0]) == Obstacle:
                return f"X: Obstacle ({self.__features[0].name})"
        else:
            return " : Empty Room"

    @property
    def can_enter(self):
        """
          Returns a boolean indicating whether the room is not
          impassable and has not been visited by traversal.
        """
        return not self.__is_impassable and not self.__visited

    @property
    def is_empty(self):
        """
          Returns a boolean indicating whether the room is
          empty.
        """
        return not(self.__features or self.__treasure)

    @property
    def is_impassable(self):
        """
          Returns a boolean indicating whether the room is
          impassable.
        """
        return self.__is_impassable

    @is_impassable.setter
    def is_impassable(self, value: bool):
        """
          Sets a boolean indicating whether the room
          is impassable.
        """
        self.__is_impassable = value

    @property
    def visited(self):
        """
          Returns a boolean indicating whether the
          room has been visited by traversal.
        """
        return self.__visited

    @visited.setter
    def visited(self, value: bool):
        """
          Sets a boolean indicating whether the
          room has been visited by traversal.
        """
        self.__visited = value

    @property
    def explored(self):
        """
          Returns a boolean indicating whether the
          room has been visited by adventurer.
        """
        return self.__explored

    @explored.setter
    def explored(self, value: bool):
        """
          Sets a boolean indicating whether the
          room has been visited by adventurer.
        """
        self.__explored = value

    @property
    def current_pos(self):
        """
          Returns a boolean indicating whether the
          adventurer is here.
        """
        return self.__current_pos

    @current_pos.setter
    def current_pos(self, value: bool):
        """
          Sets a boolean indicating whether the
          adventurer is here.
        """
        self.__current_pos = value

    @property
    def is_entrance(self):
        """
          Returns a boolean indicating whether the
          room is the entrance.
        """
        return self.__is_entrance

    @is_entrance.setter
    def is_entrance(self, value: bool):
        """
          Sets a boolean indicating whether the
          room is the entrance.
        """
        self.__is_entrance = value

    @property
    def is_exit(self):
        """
          Returns a boolean indicating whether the
          room is the exit.
        """
        return self.__is_exit

    @is_exit.setter
    def is_exit(self, value: bool):
        """
          Sets a boolean indicating whether the
          room is the exit.
        """
        self.__is_exit = value

    @property
    def features(self):
        """
          Returns the list of room features.
        """
        return self.__features

    def add_feature(self, feature):
        """
          Adds a feature to the list of features.
        """
        self.__features.append(feature)

    def remove_feature(self, feature):
        """
          Removes a feature form the list of features.
        """
        self.__features.remove(feature)

    @property
    def treasure(self):
        """
          Removes the room's treasure.
        """
        return self.__treasure

    @treasure.setter
    def treasure(self, treasure_string):
        """
          Sets the room's treasure.
        """
        self.__treasure = treasure_string
