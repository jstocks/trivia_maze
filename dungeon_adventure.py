from dungeon_adventure_controller import DungeonAdventureController


TITLE = open('title.txt', 'r').read()
WELCOME = ('Welcome to the Dungeon, it\'s got fun and games.\n'
           '     (make your terminal window wide')
INTRO = ('\nYou descend a staircase into the dungeon of objects.'
         '\nThe door slams closed behind you.\nTo escape you'
         ' must find the four treasures that conquer\nobjects'
         ' and reach the exit.\nEnter \'h\' or \'help\' for'
         ' available commands.\n\nGOOD LUCK!')


class DungeonAdventure:
    """
      This class is the main interface for the game. In an MVC model this is
      the view. It gets user input from the user, passes it to the  Dungeon
      Adventure Controller and returns responses to the user.
    """
    @staticmethod
    def init_game(play_game: bool):
        """
          Initializes a game with an adventurer name if provided by the user.
          The controller randomly selects a default name if left blank.
        """
        if play_game:
            print(f'{TITLE}\n\n\n')
            print(WELCOME)
            adventurer_name = str(input('\nEnter your adventurer\'s name or'
                                        ' press enter for a default name'
                                        ' >>> '))

            DungeonAdventure.__play_game(adventurer_name)
        else:
            print('Thank you for playing. See you next time!')

    @staticmethod
    def __play_game(adventurer_name):
        """
          This is the main game loop. It takes input, and prints
          responses to the console. At the end it asks whether the
          user would like to play again.
        """
        game = DungeonAdventureController(adventurer_name)
        play = True
        print(f'{INTRO}\n{game.adventurer_map}')
        while play:
            user_input = str(input('\nEnter your command (\'h\' or \'help\''
                                   ' for help) >>> '))
            result, play = game.user_input(user_input)
            print(f'\n{result}')
        user_input = (str(input('\nEnter \'y\' or \'yes\' to play again >>> '))
                      .lower())
        if user_input == 'y' or user_input == 'yes':
            DungeonAdventure.init_game(True)
        else:
            DungeonAdventure.init_game(False)


if __name__ == '__main__':
    DungeonAdventure.init_game(True)
