#!/usr/bin/python3
"""
Module defines peak-finding algorithm
"""


def find_peak(list_of_integers):
    """
    This method finds a peak in list of unsorted ints.

    Args:
        list_of_integers (list): A list of unsorted integers.

    Returns:
        int: The index of first peak in list.
             If list is empty, returns None.
    """
    if not list_of_integers:
        return None

    # Check if first elem is a peak
    if len(list_of_integers) == 1 or list_of_integers[0] >= list_of_integers[1]:
        return 0

    # Check if last elem is a peak
    if list_of_integers[-1] >= list_of_integers[-2]:
        return len(list_of_integers) - 1

    # Check middle elems
    for i in range(1, len(list_of_integers) - 1):
        if list_of_integers[i] >= list_of_integers[i - 1] and list_of_integers[i] >= list_of_integers[i + 1]:
            return i

    # If no peak found, return last element
    return len(list_of_integers) - 1

