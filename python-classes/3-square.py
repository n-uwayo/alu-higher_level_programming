#!/usr/bin/python3
"""Defining class"""


class Square:
    """Representing a square"""
    def __init__(self, size=0):
        """Initializing a new Square"""
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        self.size = size

    def area(self):
        return self.size ** 2
