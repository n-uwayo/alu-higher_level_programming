#!/usr/bin/python3

"""Defining class Rectangle"""


class Rectangle:
    """Represents a rectangle with a given width and height"""
    def __init__(self, width=0, height=0):
        """ Initializes a new rectangle object."""
        self.width = width
        self.height = height

    @property
    def width(self):
        """Getter method for height"""
        return self.__width

    @width.setter
    def width(self, value):
        """Setter method for width"""
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        elif value < 0:
            raise ValueError("width must be >= 0")
        else:
            self.__width = value

    @property
    def height(self):
        """Getter method for height"""
        return self.__height

    @height.setter
    def height(self, value):
        """Setter method for width"""
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        elif value < 0:
            raise ValueError("height must be >= 0")
        else:
            self.__height = value

    def area(self):
        """Calculates and returns the area of the rectangle."""
        return self.width * self.height

    def perimeter(self):
        """Calculates and returns the perimeter of the rectangle."""
        if self.width == 0 or self.height == 0:
            return 0
        else:
            return 2 * (self.width + self.height)

    def __str__(self):
        """Returns a string representation of the rectangle."""
        if self.width == 0 or self.height == 0:
            return ""
        else:
            rectangle = ""
            for i in range(self.height):
                rectangle += "#" * self.width + "\n"
            return rectangle[:-1]

    def __repr__(self):
        """Returns a string representation of the rectangle."""
        return "Rectangle({}, {})".format(self.width, self.height)

    def __del__(self):
        """Deleted instance of the class and prints a farewell message."""
        print("Bye rectangle...")
