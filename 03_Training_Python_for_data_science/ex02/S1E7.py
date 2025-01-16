from S1E9 import Character


class Lannister(Character):

    """
Representing the Lannister family.
    """

    def __init__(self, first_name, is_alive=True):

        """
        Constructor for Character class.

        :self : The character object.
        :param first_name: The first name of the character.
        :param is_alive: The health state of the character, default is True.
        """

        super().__init__(first_name, is_alive)
        self.family_name = "Lannister"
        self.eyes = "blue"
        self.hairs = "light"

    @classmethod
    def create_lannister(cls, first_name, is_alive):

        """
        Method to create a Lannister character.

        :param first_name: The first name of the character.
        :param is_alive: The health state of the character.
        :return: The Lannister character object.
        """

        return cls(first_name, is_alive)

    def die(self):

        """
        Implementation of the abstract method to change the health state.
        Sets is_alive to False.
        """

        self.is_alive = False

    def __str__(self):
        return f"Vector: ({self.family_name}, {self.is_alive}, {self.hairs})"

    def __repr__(self):
        return f"Vector: ({self.family_name}, {self.is_alive}, {self.hairs})"


class Baratheon(Character):

    """
Representing the Baratheon family.
    """

    def __init__(self, first_name):

        """
        Constructor for Character class.

        :self : The character object.
        :param first_name: The first name of the character.
        :param is_alive: The health state of the character, default is True.
        """

        super().__init__(first_name, True)
        self.family_name = "Baratheon"
        self.eyes = "brown"
        self.hairs = "dark"

    def die(self):

        """
        Implementation of the abstract method to change the health state.
        Sets is_alive to False.
        """

        self.is_alive = False

    def __str__(self):
        return f"Vector: ({self.family_name}, {self.is_alive}, {self.hairs})"

    def __repr__(self):
        return f"Vector: ({self.family_name}, {self.is_alive}, {self.hairs})"
