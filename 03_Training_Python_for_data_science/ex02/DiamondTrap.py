from S1E7 import Baratheon, Lannister


class King(Baratheon, Lannister):
    """
    Representing the King character.
    """

    def __init__(self, first_name):
        """
        Constructor for King class.

        :param first_name: The first name of the character.
        """
        super().__init__(first_name)

    def set_eyes(self, eyes_color):
        """
        Explicit setter method for eyes attribute.

        :param eyes_color: The new eyes color of the character.
        """
        self.eyes = eyes_color

    def get_eyes(self):
        """
        Explicit getter method for eyes attribute.

        :return: The eyes color of the character.
        """
        return self.eyes

    def set_hairs(self, hairs_color):
        """
        Explicit setter method for hairs attribute.

        :param hairs_color: The new hairs color of the character.
        """
        self.hairs = hairs_color

    def get_hairs(self):
        """
        Explicit getter method for hairs attribute.

        :return: The hairs color of the character.
        """
        return self.hairs

    def __str__(self):
        return f"Vector: ({self.family_name}, {self.is_alive}, {self.hairs})"

    def __repr__(self):
        return f"Vector: ({self.family_name}, {self.is_alive}, {self.hairs})"
