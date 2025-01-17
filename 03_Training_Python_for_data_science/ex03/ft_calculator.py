class calculator:

    def __init__(self, vector):
        """
        Constructor for calculator class.

        :param vector: The vector to be used in calculations.
        """
        self.vector = vector

    def __add__(self, scalar):
        """
        Addition of vector with a scalar.

        :param scalar: The scalar to add to the vector.
        :return: New vector after addition.
        """
        self.vector = [x + scalar for x in self.vector]
        print(f"{self.vector}")
        return self

    def __mul__(self, scalar):
        """
        Multiplication of vector with a scalar.

        :param scalar: The scalar to multiply with the vector.
        :return: New vector after multiplication.
        """
        self.vector = [x * scalar for x in self.vector]
        print(f"{self.vector}")
        return self

    def __sub__(self, scalar):
        """
        Subtraction of scalar from vector.

        :param scalar: The scalar to subtract from the vector.
        :return: New vector after subtraction.
        """
        self.vector = [x - scalar for x in self.vector]
        print(f"{self.vector}")
        return self

    def __truediv__(self, scalar):
        """
        Division of vector by a scalar.

        :param scalar: The scalar to divide the vector by.
        :return: New vector after division.
        """
        if scalar == 0:
            raise ValueError("Division by zero is not allowed.")
        self.vector = [x / scalar for x in self.vector]
        print(f"{self.vector}")
        return self
