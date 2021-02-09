from room_feature import RoomFeature


# Main Class
class Obstacle(RoomFeature):
    def __init__(self, name, effect, hit_points):
        """
        Obstacle class that creates a subclass of room feature.
        """
        super().__init__(name, 'Obstacle')
        self.__effect = effect
        self.__hit_points = hit_points
        self.__description = (f'An obstacle ({name}) that deals'
                              f' {self.__hit_points} damage.')

    @property
    def description(self):
        """
        Returns a string describing the obstacle.
        """
        return self.__description

    @property
    def effect(self):
        """
        Returns a string of the effect of the obstacle
        """
        return f'{self.__effect}\nYou take {self.__hit_points} damage.'

    @property
    def hit_points(self):
        """
        Returns hit point damage of obstacle
        """
        return self.__hit_points
