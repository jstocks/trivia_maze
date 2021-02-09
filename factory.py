class Factory:
    @staticmethod
    def to_integer(number):
        """
          Converts an inputted string to an integer, if possible,
          raises value error if not.
        """
        if int(str(number)):
            return int(str(number))
        else:
            raise ValueError('value must be an integer or convertable to'
                             ' an integer')

    @staticmethod
    def is_string(some_input):
        """
          Verifies that input is a string, returns value error if not.
        """
        if isinstance(some_input, str):
            return some_input
        else:
            raise ValueError('value must be a string')
