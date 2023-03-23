#!/usr/bin/python3
"""Module for adding attributes to objects"""


def add_attribute(obj, name, value):
    """Function for adding a new attribute to an object if it's possible"""
    if hasattr(obj, '__dict__') is False:
        raise TypeError("can't add new attribute")

    setattr(obj, name, value)

# To get information about the module, use the help() function
help(add_attribute)
