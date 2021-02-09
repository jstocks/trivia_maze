from dungeon import Dungeon
from adventurer_factory import AdventurerFactory

VALID_INPUT = [
    'n', 'north',  # move north
    's', 'south',  # move south
    'e', 'east',  # move east
    'w', 'west',  # move west
    'i', 'info',  # get adventurer status
    'r', 'room',  # show current room
    'h', 'help',  # get help
    'p', 'potion',  # use healing potion
    'v', 'vision',  # use vision potion
    'q', 'quit',  # exit the dungeon
    'm', 'map',  # reveal the dungeon map
    # Cheat Commands
    'c', 'cheat',  # toggle cheat mode
    't', 'treasure',  # add all treasure
    'g', 'god',  # add 1,000 hit points
    'u', 'unveil'  # show all rooms
]

INPUT_HELP = """GAME HELP

Movement commands:
  n, north to move the character north.
  s, south to move the character south.
  e, east to move the  character east.
  w, west to move the character west.
Status commands:
  i, info to show adventurer status.
  r, room to show the current room.
  m, show adventurer map.
Use item commands:
  p, potion to use a healing potion.
  v, vision to use a vision potion.
Game commands:
  q, quit to leave the dungeon.
Cheat commands (when enabled):
  c, cheat to toggle cheat mode.
  t, treasure to add all treasures.
  g, god to add 1,000 hit points.
  u, unveil to see all rooms."""


class DungeonAdventureController:
    def __init__(self, adventurer_name):
        self.__dungeon = Dungeon()
        self.__adventurer = (AdventurerFactory
                             .create_adventurer(adventurer_name))
        self.__current_room = None
        self.__cheat = False

    @property
    def adventurer_map(self):
        """
          Returns the adventurer map.
        """
        return str(self.__dungeon.adv_map())

    def user_input(self, user_input):
        """
          This static method determines whether a user command is
          in the list of valid input. Calls appropriate methods if so,
          returns an error message if not.
        """

        # Convert user input to lower case.
        user_input = user_input.lower()
        if user_input in VALID_INPUT:
            # Move commands
            if user_input == 'n' or user_input == 'north':
                # Do move north
                self.__current_room = self.__dungeon.update_adv_pos(-1, 0)
                if self.__current_room:
                    return self.__enter_room()
                else:
                    return ('You cannot go north here.\n\n'
                            f'{self.adventurer_map}', True)
            elif user_input == 's' or user_input == 'south':
                # Do move south
                self.__current_room = self.__dungeon.update_adv_pos(1, 0)
                if self.__current_room:
                    return self.__enter_room()
                else:
                    return ('You cannot go south here.\n\n'
                            f'{self.adventurer_map}', True)
            elif user_input == 'e' or user_input == 'east':
                # Do move east
                self.__current_room = self.__dungeon.update_adv_pos(0, 1)
                if self.__current_room:
                    return self.__enter_room()
                else:
                    return ('You cannot go east here.\n\n'
                            f'{self.adventurer_map}', True)
            elif user_input == 'w' or user_input == 'west':
                # Do move west
                self.__current_room = self.__dungeon.update_adv_pos(0, -1)
                if self.__current_room:
                    return self.__enter_room()
                else:
                    return ('You cannot go west here.\n\n'
                            f'{self.adventurer_map}', True)

            # Status commands
            elif user_input == 'i' or user_input == 'info':
                # Show adventurer status
                return str(self.__adventurer), True
            elif user_input == 'r' or user_input == 'room':
                # Show room
                return self.__dungeon.display_curr_room(), True
            elif user_input == 'm' or user_input == 'map':
                return self.adventurer_map, True

            # Use item commands
            elif user_input == 'p' or user_input == 'potion':
                result = self.__adventurer.use_healing_potion()
                if result:
                    return result.effect, True
                else:
                    return 'You do not have any healing potions', True
            elif user_input == 'v' or user_input == 'vision':
                # Do vision
                result = self.__adventurer.use_vision_potion()
                if result:
                    map_string = f'{result.effect}\n'
                    map_dictionary = self.__dungeon.use_vision_potion()
                    for key, value in map_dictionary.items():
                        map_string += f'\n{key} {value}'
                    return map_string, True
                else:
                    return 'You do not have any vision potions', True
            # Game commands
            elif user_input == 'h' or user_input == 'help':
                return INPUT_HELP, True
            elif user_input == 'q' or user_input == 'quit':
                # Exit the dungeon
                return 'Exiting the dungeon', False
            # Cheat commands
            elif user_input == 'c' or user_input == 'cheat':
                self.__cheat = not self.__cheat
                if self.__cheat:
                    return 'You have enabled cheat mode.', True
                else:
                    return 'You have disabled cheat mode', True
            elif user_input == 't' or user_input == 'treasure':
                if self.__cheat:
                    for treasure in ["ABSTRACTION", "ENCAPSULATION",
                                     "INHERITANCE", "POLYMORPHISM"]:
                        self.__adventurer.find_treasure(treasure)
                    return 'You have cheated and added all treasures.', True
                else:
                    return f'{user_input} is not enabled.', True
            elif user_input == 'g' or user_input == 'god':
                if self.__cheat:
                    self.__adventurer.god_mode()
                    return 'You have cheated and added 1,000 hit points.', True
                else:
                    return f'{user_input} is not enabled.', True
            elif user_input == 'u' or user_input == 'unveil':
                if self.__cheat:
                    return str(self.__dungeon), True
                else:
                    return f'{user_input} is not enabled.', True
            # Shouldn't get here
            else:
                return 'Something went wrong', True
        else:
            return f'{user_input} is not a valid command.', True

    def __enter_room(self):
        """
          This function handles the actions that happen when an
          adventurer enters a room. It builds a string that is
          returned to the interface to report what happened
          in the UI.
        """
        room_string = ''
        room_string += f'{self.adventurer_map}\n'
        # If room is empty.
        if (not self.__current_room.features and
                not self.__current_room.treasure and
                not self.__current_room.is_entrance and
                not self.__current_room.is_exit):
            room_string += 'There is nothing in this room!'
        # When the room is an exit.
        if self.__current_room.is_exit:
            room_string += ('You have found the exit!\nSun peeks through an'
                            ' opening to the surface. You can hear birds'
                            ' chirping.\n')
            if sorted(self.__adventurer.treasure_found) == ["ABSTRACTION",
                                                            "ENCAPSULATION",
                                                            "INHERITANCE",
                                                            "POLYMORPHISM"]:
                room_string += ('You are satisfied that you have collected'
                                ' all the treasure to be found.'
                                '\nCongratulations, you leave the dungeon'
                                f' a winner!\n\n{str(self.__dungeon)}')
                return room_string, False
            else:
                missing_treasure = ''
                for treasure in ["ABSTRACTION", "ENCAPSULATION",
                                 "INHERITANCE", "POLYMORPHISM"]:
                    if treasure not in self.__adventurer.treasure_found:
                        missing_treasure += f'{treasure}\n'
                room_string += ('You think there is more to find here before'
                                ' you leave this place.\n\nYou still need to'
                                ' find the following treasures:\n'
                                f'{missing_treasure}')
        # When the room is an entrance.
        if self.__current_room.is_entrance:
            room_string += ('This is where you entered the dungeon.\nThe way'
                            ' out here is blocked.')
        # When the room has features.
        index = 0
        while index < len(self.__current_room.features):
            if self.__current_room.features[index].category == 'Item':
                item = self.__current_room.features.pop(index)
                self.__adventurer.add_item(item)
                room_string += f'You have picked up a {item.description}\n'
            elif self.__current_room.features[index].category == 'Obstacle':
                self.__adventurer.encounter_obstacle(
                    self.__current_room.features[index]
                )
                room_string += (
                    f'{self.__current_room.features[index].effect}\n'
                )
                index += 1
        # When the room has a treasure.
        if (self.__current_room.treasure and self.__current_room.treasure
                not in self.__adventurer.treasure_found):
            self.__adventurer.find_treasure(self.__current_room.treasure)
            room_string += ('You have found treasure:'
                            f' {self.__current_room.treasure}!\n')
            self.__current_room.treasure = None
        elif self.__current_room.treasure:
            room_string += ('You have already found treasure:'
                            f' {self.__current_room.treasure}!\n')
            self.__current_room.treasure = None

        # When adventurer dies.
        if self.__adventurer.hit_points < 1:
            room_string += ('Oh noes, you have died! :\'(\n\n'
                            f'{str(self.__dungeon)}')
            return room_string, False
        play = True
        return room_string, play
