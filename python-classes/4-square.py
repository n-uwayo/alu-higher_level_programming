#!/usr/bin/python3

"""Defining class"""


class Square:
    """Representing a square"""

    def __init__(self, size=0):
        """Initialization of private attribute '__size' with parameter 'size' """
        self.__size = size

    @property
    def size(self):
        """Get size of the square"""
        return self.__size

    @size.setter
    def size(self, value):
        """Set the size of square.
        Raises:
            Type Error: If the value is not an integer
            ValueError: If value is less than 0.
        """
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = value

    def area(self):
        """Find the area of square"""
        return self.__size ** 2
