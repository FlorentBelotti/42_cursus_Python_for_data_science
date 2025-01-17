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

    @staticmethod
    def dotproduct(v1, v2):
        """
        Calculate the dot product of two vectors.

        :param v1: The first vector.
        :param v2: The second vector.
        :return: The dot product of the two vectors.
        """
        if len(v1) != len(v2):
            raise ValueError("Vectors must be of the same length.")
        print(f'Dot product is: {sum(x * y for x, y in zip(v1, v2))}')

    @staticmethod
    def add_vec(v1, v2):
        """
        Add two vectors.

        :param v1: The first vector.
        :param v2: The second vector.
        :return: The sum of the two vectors.
        """
        if len(v1) != len(v2):
            raise ValueError("Vectors must be of the same length.")
        print(f'Add vector is: {[float(x + y) for x, y in zip(v1, v2)]}')

    @staticmethod
    def sous_vec(v1, v2):
        """
        Subtract one vector from another.

        :param v1: The first vector.
        :param v2: The second vector.
        :return: The difference between the two vectors.
        """
        if len(v1) != len(v2):
            raise ValueError("Vectors must be of the same length.")
        print(f'Sous vector is: {[float(x - y) for x, y in zip(v1, v2)]}')
