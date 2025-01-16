from abc import ABC, abstractmethod


class Character(ABC):

    """Class character : represent a generic character"""

    def __init__(self, first_name, is_alive=True):

        """
        Constructor for Character class.

        :self : The character object.
        :param first_name: The first name of the character.
        :param is_alive: The health state of the character, default is True.
        """

        self.first_name = first_name
        self.is_alive = is_alive

    @abstractmethod
    def die(self):

        """
        Abstract method to change the health state of the character.

        :self : The character object.
        """

        print("This method should be implemented in the child class.")
        pass


class Stark(Character):

    """Representinf the Stark family"""

    def __init__(self, first_name, is_alive=True):

        """
        Constructor for Stark class.

        :param first_name: The first name of the Stark character.
        :param is_alive: The health state of the Stark character.
        """

        super().__init__(first_name, is_alive)

    def die(self):

        """
        Implementation of the abstract method to change the health state.
        Sets is_alive to False.
        """

        self.is_alive = False
