#!/usr/bin/python3
""" Same class or inherit from """


def is_kind_of_class(obj, a_class):
    """
    Returns True if the object is an instance of, or if the object is an instance of a class that inherited from,
    the specified class; otherwise False.
    """
    if isinstance(obj, a_class):
        return True
    for base_class in obj.__class__.__bases__:
        if is_kind_of_class(obj, base_class):
            return True
    return False
