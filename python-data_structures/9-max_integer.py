#!/usr/bin/python3


def max_integer(my_list=[]):
    if len(my_list) == 0:
        return (None)

    bg = my_list[0]
    for a in range(len(my_list)):
        if my_list[a] > bg:
            bg = my_list[a]

    return (bg)
