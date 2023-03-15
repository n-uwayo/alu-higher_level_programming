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
        """Sets the size private attribute value.
        Validates the assignment of the size private attribute.
        Arg:
            value: the value to be set
        """
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = value
    
    @property
    def position(self):
        """Gets the position private attribute value.
        Returns:
            The position private attribute"""
        return self.__position
    
    @position.setter
    def position(self, value):
        """Sets the position private attribute value.
        Validates the assignment of the position private attribute.
        Arg:
            value: the value to be set
        """
        if (not isinstance(value, tuple) or
                len(value) != 2 or
                not all(isinstance(num, int) for num in value) or
                not all(num >= 0 for num in value)):
            raise TypeError("position must be a tuple of 2 positive integer")
        self.__position = vallue

    def area(self):
        """A public object method.
        Returns:
            The current square area
        """
        return self.__size ** 2

    def my_print(self):
        """Displays the square object with '#' character"""
        if self.__size == 0:
            print()
        else:
            for k in range(0, self.__size):
                for n in range (0, self.__position[0]):
                        print(" ", end="")
                    for m in range(0, self.__size):
                        print("#", end="")
                    print("")

