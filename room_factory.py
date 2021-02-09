from random import randint
from room_feature_factory import RoomFeatureFactory
from room import Room

HEALING_CHANCE = 10
VISION_CHANCE = 10
OBSTACLE_CHANCE = 10


class RoomFactory():
    """
      This factory creates the rooms that go in the dungeon.
    """
    @staticmethod
    def create_room():
        """
         Creates a room object and places a healing potion, vision potion
         and/or an obstacle in it depending on the random chances.
        """
        room = Room()
        if randint(0, 100) < HEALING_CHANCE:
            room.add_feature(RoomFeatureFactory.create_healing_potion())
        if randint(0, 100) < VISION_CHANCE:
            room.add_feature(RoomFeatureFactory.create_vision_potion())
        if randint(0, 100) < OBSTACLE_CHANCE:
            room.add_feature(RoomFeatureFactory.create_obstacle())
        return room
