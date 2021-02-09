from random import choice, randint

from factory import Factory
from healing_potion import HealingPotion
from vision_potion import VisionPotion
from obstacle import Obstacle

# Configuration
HEALING_MIN = 5   # 5 - 15 per rubric
HEALING_MAX = 15
OBSTACLE_MIN = 1  # 1 - 20 per rubric
OBSTACLE_MAX = 20
OBSTACLES = {
  'Pit': 'You fall into a pit filled with spikes.',

  'Trip-wire': ('You trip a trip wire and are shot with a'
                ' baker\'s dozen arrows.'),

  'Quicksand': 'You fell into a quicksand and are trapped.',
}


class RoomFeatureFactory(Factory):
    """
      This factory creates items an adventurer might run into or use.
    """
    @staticmethod
    def create_healing_potion(hit_points=None):
        """
          Creates an and returns an healing potion object.
          :: takes an HP range as arguments.
        """
        if not hit_points:
            hit_points = randint(HEALING_MIN, HEALING_MAX)
        return HealingPotion(RoomFeatureFactory.to_integer(hit_points))

    @staticmethod
    def create_vision_potion():
        """
        Creates an and returns an vision object.
        """
        return VisionPotion()

    @staticmethod
    def create_obstacle(name=None, effect=None, hit_points=None):
        """
        Creates an and returns an obstacle object.
        :: takes an damage range as arguments.
        """
        if not hit_points:
            hit_points = randint(OBSTACLE_MIN, OBSTACLE_MAX)
        if not name or not effect:
            name, effect = choice(list(OBSTACLES.items()))

        return Obstacle(RoomFeatureFactory.is_string(name),
                        RoomFeatureFactory.is_string(effect),
                        RoomFeatureFactory.to_integer(hit_points))
