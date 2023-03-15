#!/usr/bin/python3

"""Define Square"""


class Square:
    """Represent a square with size attribute"""
    def __init__(self, size=0):
        """Initialize a new Square with specified size
        Raises: Type Error: If the value is not an integer
            ValueError: If value is less than 0.
        """
        self.__size = size

  
    @property
    def size(self):
        """Gets the size of square
       Raises: Type Error: If the value is not an integer
            ValueError: If value is less than 0. 
        """
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            ValueError("size must be >= 0")
        else:
            self.__size = value

    def area(self):
        """calculate the area of square"""
        return self.__size ** 2

    def my_print(self):
        """print square with '#'."""
        if self.__size == 0:
            print()
        else:
            for n in range(self.__size):
                for m in range(self.__size):
                    print("#", end="")
                print()
