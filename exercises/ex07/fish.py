"""File to define Fish class."""


class Fish:
    """Establishing our Fish class."""
    age: int
    def __init__(self):
        """Creating a new fish object."""
        self.age = 0

    def one_day(self):
        """Simulating a day in the life of a fish."""
        self.age += 1
        return None
