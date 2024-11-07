"""File to define Bear class."""


class Bear:
    """Establishing our bear class."""

    age: int
    hunger_score: int

    def __init__(self):
        """Creating a new bear object."""
        self.age = 0
        self.hunger_score = 0

    def one_day(self):
        """Simulating a day in the life of a bear."""
        self.age += 1
        self.hunger_score -= 1

    def eat(self, num_fish: int) -> None:
        """Simulating a bear eating."""
        self.hunger_score += num_fish
        return None
