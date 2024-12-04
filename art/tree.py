"""Some happy, little trees!"""

from .turtle import Turtle
from math import pi

__template__ = "https://24ss2.comp110.com/static/turtle"

DEGREE = float = -pi / 180.0


def main() -> None: ...


def click(x: float, y: float) -> Turtle:
    """Moves turtle to wherever we click on the canvas"""
    t: Turtle = Turtle()
    t.setSpeed(1000.0)
    t.moveTo(x, y)
    t.turnTo(90 * DEGREE)
    branch(t, 100.0, 90 * DEGREE)

    return t


def branch(t: Turtle, length: float, angle: float) -> None:
    t.turnTo(angle)
    t.forward(length)

    if length > 3.0:
        branch(t, length * 0.75, angle + 35.0 * DEGREE)
        # make the same function call again but subtract 35 degrees
        branch(t, length * 0.75, angle - 35.0 * DEGREE)
    t.turnTo(angle + pi)
    t.forward(length)
