"""Visualizing our concatenation and visualization function in a different file."""

author: str = "730767591"
from CQs.cq04.concatenation import concat  # imports concat from our concatenation file
from CQs.cq04.coordinates import (
    get_coords,
)  # imports get_coords from our coordinates file

x: str = "123"
y: str = "abc"

# imported functions with our variables
print(concat(first=x, second=y))
get_coords(xs=x, ys=y)
