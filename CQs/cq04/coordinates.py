"""Allows us to get and print coordinates."""

__author__: str = "730767591"


def get_coords(xs: str, ys: str) -> None:
    """prints out the x,y coordinates for two strings."""
    index_x: int = 0  # counter variable for first while loop
    while index_x < len(xs):  # while loop that iterates over every index in xs
        index_y: int = 0  # counter variable for second while loop
        while index_y < len(ys):  # while loop that iterates over every index in ys
            print(
                "(" + xs[index_x] + "," + ys[index_y] + ")"
            )  # print statement that uses counter variables to print out desired output
            index_y += 1  # incrementing counter-variable for second while loop
        index_x += 1  # incrementing counter-variable for first while loop
