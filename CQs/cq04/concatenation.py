"""Concatenation of two strings."""

__author__: str = "730767591"

word1: str = "happy"
word2: str = "tuesday"


def concat(first: str, second: str) -> str:
    """Takes two strings and concatenates them."""
    return (
        first + second
    )  # simply takes the first parameter and concatenates it with our second parameter


if (
    "__name__" == "__main__"
):  # prevents the calling of the print statement when calling the function in a different file
    print(concat(first=word1, second=word2))
