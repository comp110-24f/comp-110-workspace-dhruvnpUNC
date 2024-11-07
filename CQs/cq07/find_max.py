"""creating functions to test"""

__author__: str = "730767591"


def find_and_remove_max(listInput: list[int]) -> int:
    """Finding and removing largest element"""
    if len(listInput) == 0:  # edge case that returns an output when list is empty
        return -1

    largest: int = listInput[0]
    for i in listInput:  # for loop that finds the largest element
        if i > largest:
            largest = i

    idx = 0
    while idx < len(
        listInput
    ):  # while loop that removes all instances of the largest element
        if listInput[idx] == largest:
            listInput.pop(idx)
            idx = -1
            """
            The reason why we set idx = -1 has to do with how .pop works.
            When an index is popped, the length of the list changes.
            This results in numbers in consecutive indexes not being deleted properly.
            Therefore we need to re-traverse the list from the beginning to ensure the indexes containing the largest number are deleted
            """
        idx += 1

    return largest
