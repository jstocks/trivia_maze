from random import randint, choice
from factory import Factory
from adventurer import Adventurer

# Configuration
MIN_HP = 75
MAX_HP = 100
DEFAULT_NAMES = [
    'Brunhilda',
    'Mighty Thor',
    'Leonidas',
    'Boudica'
]


class AdventurerFactory(Factory):
    @staticmethod
    def create_adventurer(name=None,
                          hit_points=randint(MIN_HP, MAX_HP)):
        """
          Creates an and returns an adventurer object.
          :: takes an adventurer name and a HP range as arguments.
        """
        if not name:
            name = choice(DEFAULT_NAMES)
        return Adventurer(AdventurerFactory.is_string(name),
                          AdventurerFactory.to_integer(hit_points))
