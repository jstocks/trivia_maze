from room_feature import RoomFeature


# Main Class
class HealingPotion(RoomFeature):

    def __init__(self, hit_points):
        """
        Healing potion class creates a subclass of room feature.
        """
        super().__init__(f'Healing Potion ({hit_points})', 'Item')
        self.__hit_points = hit_points

    @property
    def description(self):
        """
        Returns a string of the hit points that the Healing potion heals.
        """
        return f'A potion that heals {self.hit_points} hit points'

    @property
    def effect(self):
        """
        You take a healing potion and gain {self.}
        """
        return (f'You take a healing potion and gain {self.hit_points}'
                ' hit points.')

    @property
    def hit_points(self):
        """
        Returns the hit points that the Healing potion heals.
        """
        return self.__hit_points
