"""Using recursion to create linked list functions."""

from __future__ import annotations

__author__: str = "730767591"


class Node:
    """Delcaring our node class."""

    value: int
    next: Node | None

    def __init__(self, value: int, next: Node | None):
        """Initializing our Node class."""
        self.value = value
        self.next = next

    def __str__(self) -> str:
        """Produce a string representation of a linked list."""
        rest: str = "TODO"
        # TODO: Figure out the rest of the list.
        if self.next is None:
            rest = "None"
        else:
            rest = self.next.__str__()
        return f"{self.value} -> {rest}"


def value_at(head: Node | None, index: int) -> int:
    """Finding a value at a specified index in a linked list."""
    if head is None:
        raise IndexError("Index is out of bounds on the list.")

    if index == 0:
        # If we want the value at the first index, just return the value
        return head.value
    else:
        # If the value is at another index,
        # starting at the specified index,
        # we look at the next node and decrease
        # index by one until we reach our base case
        return value_at(head.next, index - 1)


def max(head: Node | None) -> int:
    """Finding the maximum value in our linked list."""
    if head is None:
        raise ValueError("Cannot call max with None")

    if head.next is None:
        return head.value
        # If there is no next value, then the current head must be the max
    else:
        rest = max(head.next)
        # We need to compare the value of the other nodes.
        # We do this by calling the max function again with head.next as the parameter.
        if head.value > rest:
            rest = head.value
        return rest


def linkify(items: list[int]) -> Node | None:
    """Creating a linked list given a list of integers."""
    if len(items) == 0:
        return None

    if len(items) == 1:
        # If our list is only one element long, then just return a singular node.
        return Node(items[0], None)
    else:
        # In order to form the rest of the list,
        # we need to start with the whole list
        # and work our way to our edge case
        # of one item in the list.
        # This is done by using subcription notation to
        # send a new list to the linkify function
        # that doesn't include the first element of the previous list
        # and setting that chain equal to rest.
        rest: Node | None = linkify(items[1:])
        return Node(items[0], rest)


def scale(head: Node | None, factor: int) -> Node | None:
    """Multiplying the values in our linked list by a scale factor."""
    if head is None:
        return None

    if head.next is None:
        # If our list is only one element long,
        # then return a Node object whose value is head.value * factor
        # and whose head.next value is none.
        return Node(head.value * factor, None)
    else:
        # In order to scale the rest of the linked list,
        # we need to access the next node as well and scale its value
        # by factor. We do this by recusrively calling the scale function
        rest: Node | None = scale(head.next, factor)
        return Node(head.value * factor, rest)
