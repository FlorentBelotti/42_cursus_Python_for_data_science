from S1E7 import Baratheon, Lannister


class King(Baratheon, Lannister):

    """
Representing the King character.
    """

    def __init__(self, first_name, is_alive=True):

        """
        Constructor for King class.

        Default constructor is from Baratheon class:
        with family_name = "Baratheon"
        with eyes = "brown"
        with hairs = "dark"
        """

        super().__init__(first_name)

    """
Setters for :eyes: and :hairs: attributes.
    """

    def set_eyes(self, eyes_color):

        """
        Setter for eyes attribute.

        :param eyes: The eyes color of the character.
        """

        self.eyes = eyes_color

    def set_hairs(self, hairs_color):

        """
        Setter for eyes attribute.

        :param hairs_color: The hairs color of the character.
        """

        self.hairs = hairs_color

    """
Getters for :eyes: and :hairs: attributes.
    """

    def get_eyes(self):

        """
        Getter for eyes attribute.

        :return: The eyes color of the character.
        """

        return self.eyes

    def get_hairs(self):

        """
        Getter for hairs attribute.

        :return: The hairs color of the character.
        """

        return self.hairs

    def __str__(self):
        return f"Vector: ({self.family_name}, {self.is_alive}, {self.hairs})"

    def __repr__(self):
        return f"Vector: ({self.family_name}, {self.is_alive}, {self.hairs})"
