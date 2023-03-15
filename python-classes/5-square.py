#!/usr/bin/python3

"""Defining class Square"""


class Square:
    """Representa asquare with attribute and methode"""

    def __init__(self, size=0):
        """Initialize a new instance of Square class with specified size"""
        self.size = size

    @property
    def size(self):
        """Gets the size of the square"""
        return self.__size

    @size.setter
    def size(self, value):
        """Sets the size of the square
        Raises:
        TypeError: If the size is not an integer.
        ValueError: If the size is less than 0.
        """
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = value

    def area(self):
        """"computes the area of the square"""
        return self.__size ** 2

    def my_print(self):
        """prints the square with the '#' character"""
        if self.__size == 0:
            print()
        else:
            for n in range(self.__size):
                for m in range(self.__size):
                    print("#", end="")
                print()
