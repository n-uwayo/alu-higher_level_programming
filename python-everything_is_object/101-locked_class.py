#!/usr/bin/python3
"""Define class LockedClass"""


class LockedClass:
    """attribute called"""

    __slots__ = ('first_name',)

    def __init__(self):
        self.first_name = None

    def __setattr__(self, name, value):
        if not hasattr(self, name) and name != 'first_name':
            raise AttributeError(f"LockedClass' object has no attribute  '{name}'")
        super().__setattr__(name, value)
