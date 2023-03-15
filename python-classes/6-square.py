#!/usr/bin/python3

"""Define class Square"""


class Square:
    """Representing a square"""

    def __init__(self, size=0, position=(0, 0)):
        """An object constructor method."""
        self.size = size
        self.position = position

    @property
    def size(self):
        """Gets the size private attribute value."""
        return (self.__size)
    
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
    
    @property
    def position(self):
        """Gets the current position"""
        return self.__position
    
    @position.setter
    def position(self, value):
        """Sets the position
        TypeError: If the position is not a tuple of 2 positive integer.
        """
        if (not isinstance(value, tuple) or
                len(value) != 2 or
                not all(isinstance(num, int) for num in value) or
                not all(num >= 0 for num in value)):
            raise TypeError("position must be a tuple of 2 positive integer")
        self.__position = vallue

    def area(self):
        """compute the area of square"""
        return self.__size ** 2

    def my_print(self):
        """prints the square with the '#' character"""
        if self.__size == 0:
            print()
        else:
            for k in range(0, self.__size):
                for n in range (0, self.__position[0]):
                        print(" ", end="")
                    for m in range(0, self.__size):
                        print("#", end="")
                    print("")

