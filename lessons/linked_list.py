from __future__ import annotations


class Node:
    value: int
    next: Node | None

    def __init__(self, value: int, next: Node | None):
        self.value = value
        self.next = next

    def __str__(self):
        """Produce a string representation of a linked list."""
        rest: str = "TODO"
        # TODO: Figure out the rest of the list.
        if self.next is None:
            rest = "None"
        else:
            rest = self.next.__str__()
        return f"{self.value} -> {rest}"


two: Node = Node(2, None)
one: Node = Node(1, two)
courses: Node = Node(110, Node(210, Node(301, None)))


def to_str(head: Node | None) -> str:
    """Represent a Linked List as a str."""
    if head is None:
        return "None"
    else:
        rest: str = to_str(head.next)
        return f"{head.value} -> {rest}"


print(to_str(one))
print(to_str(courses))
print(str(courses))
print(str(one))


def last(head: Node) -> int:
    """Return the last value of a non-empty list"""
    # Base Case: When head is the last Node
    # Return its Value!
    # Recursive case:
    print(f"Enter last({head.value})")
    if head.next is None:
        print(f"Return base case: {head.value}")
        return head.value
    else:
        # Figure out the last node (recursive call)
        # In the rest of the list
        rest: int = last(head.next)
        print(f"Return recur: {head.value} -> {rest}")
        return rest


print(last(one))
print(last(courses))


def recursive_range(start: int, end: int) -> None | Node:
    if start > end:
        # Edge Case:
        raise ValueError("Start is greater than End")

    if start == end:
        # Base Case:
        return None
    else:
        # Recursive Case
        # 1. Handle the first value in your new list here!
        first: int = start
        # 2. Let the rest of the list be handled recursively!
        rest: Node | None = recursive_range(start + 1, end)
        # 3. Return a new node which is the first followed by the rest.
        return Node(first, rest)


def factorial(n: int) -> int:
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n - 1)


print(factorial(n=7))
