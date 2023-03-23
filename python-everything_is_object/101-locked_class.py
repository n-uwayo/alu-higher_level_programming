#!/usr/bin/python3

"""This module defines a class called LockedClass that restricts attribute assignment."""

class LockedClass:
    """
    A class that restricts attribute assignment.

    Attributes:
        first_name (str): The first name of the LockedClass instance.
    """

    __slots__ = ('first_name',)

    def __init__(self):
        """Initialize a LockedClass instance."""
        self.first_name = None

    def __setattr__(self, name, value):
        """Set an attribute value."""
        if not hasattr(self, name) and name != 'first_name':
            raise AttributeError(f"LockedClass' object has no attribute '{name}'")
        super().__setattr__(name, value)
