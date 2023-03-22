#!/usr/bin/python3

# This function takes two lists of equal length and returns a new list
# containing the result of dividing the corresponding elements in the two
# input lists. If there is a type error, division by zero, or index out
# of range error, the corresponding element in the output list will be 0.


def list_division(my_list_1, my_list_2, list_length):
    new_list = []
    for i in range(0, list_length):
        try:
            result = my_list_1[i] / my_list_2[i]
        except TypeError:
            print("wrong type")
            result = 0
        except ZeroDivisionError:
            print("division by 0")
            result = 0
        except IndexError:
            print("out of range")
            result = 0
        finally:
            new_list.append(result)
    return (new_list)
