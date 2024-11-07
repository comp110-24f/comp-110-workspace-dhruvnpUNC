"""List utility functions"""

__author__: str = "730767591"


def only_evens(input_list: list[int]) -> list[int]:
    """Creating an evens only list from a master list"""
    temp_list: list[int] = []  # creates an empty list
    for i in input_list:  # loops over every element in the master list
        if i % 2 == 0:  # checks to see if the current element is even
            temp_list.append(i)  # appended to list if item is even
    return temp_list


def sub(input_list: list[int], start: int, end: int) -> list[int]:
    """creating a smaller list from a bigger list"""
    # edge case if input list is empty
    if len(input_list) == 0:
        return []
    # edge case if the start is greater than the list itself
    if start >= len(input_list):
        return []
    # edge case if end is smaller than the list itself
    if end <= 0:
        return []
    # edge case if end value is longer than list
    if len(input_list) < end:
        end = len(input_list)
    # edge case if start is less than 0
    if start < 0:
        start = 0

    temp_list: list[int] = []
    idx: int = start
    # while loop iterates between start and end value
    while idx < end:
        # item added to list when while loop runs
        temp_list.append(input_list[idx])
        idx += 1
    return temp_list


def add_at_index(input_list: list[int], value: int, index: int) -> None:
    """Adding an element at a specific index using append and loops"""
    if (index < 0) or (index > len(input_list)):
        raise IndexError("Index is out of bounds for the input list")

    input_list.append(0)  # add item to the end of the list
    idx = len(input_list) - 1  # counter variable that starts at the end of the list
    while idx > index:  # working from end of list backwards to the specific index
        input_list[idx] = input_list[
            idx - 1
        ]  # taking current element and making it equal to the preceding element
        idx -= 1  # counter variable to stop infinite looping
    input_list[index] = value  # setting the specified index to its corresponding value

invert({'kris': 'jordan', 'michael': 'jordan'})