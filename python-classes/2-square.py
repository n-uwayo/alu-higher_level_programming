#!/usr/bin/python3
"""Defining class with name Square"""


class Square:
    """Representing a square"""
    def __init__(self, size=0):
        """Initialization of new square"""
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size
