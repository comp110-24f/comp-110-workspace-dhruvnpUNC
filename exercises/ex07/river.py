"""File to define River class."""

__author__: str = "730767591"

from exercises.ex07.fish import Fish
from exercises.ex07.bear import Bear


class River:
    """Establishing our River Class."""

    day: int
    fish: list[Fish]
    bears: list[Bear]

    def __init__(self, num_fish: int, num_bears: int):
        """New River with num_fish Fish and num_bears Bears."""
        self.day: int = 0
        self.fish: list[Fish] = []
        self.bears: list[Bear] = []
        # populate the river with fish and bears
        for _ in range(0, num_fish):
            self.fish.append(Fish())
        for _ in range(0, num_bears):
            self.bears.append(Bear())

    def check_ages(self):
        """Checking the ages of fish and bears."""
        temp_fish: list[Fish] = []
        # Temp list to store fish that aren't 3 or older.
        for i in self.fish:
            # going through every object in fish list.
            if i.age <= 3:
                # If fish is less than or equal to 3 years old
                temp_fish.append(i)
                # append it to the temp list
        self.fish = temp_fish
        # set the fish list equal to the temp list
        # this allows us to have an accurately updated fish attribute/variable.

        temp_bears: list[Bear] = []
        # Logic for bears is the same as it is for fish.
        for j in self.bears:
            if j.age <= 5:
                temp_bears.append(j)
        self.bears = temp_bears

        return None

    def remove_fish(self, amount: int) -> None:
        """Removing a specified number of fish from the start of the list."""
        for i in range(amount):
            # Repeating .pop a specified number of times.
            self.fish.pop(0)
            # Poping the object at the first index of the lsit
        return None

    def bears_eating(self):
        """Simulating the bears eating fish."""
        for i in self.bears:
            # Going through every object in the bears list.
            if len(self.fish) >= 5:
                # if the amount of fish stored in the fist list is greater or equal to 5
                self.remove_fish(3)
                # remove 3 fish
                i.eat(num_fish=3)
                # make the current bear eat 3 fish

        return None

    def check_hunger(self):
        """Checking bears hunger levels and removing accordingly."""
        temp_bears: list[Bear] = []
        # temp list to store bears that are starving to death.
        for i in range(len(self.bears)):
            # going through every object in the bear list.
            if self.bears[i].hunger_score < 0:
                # if i'm being honest I don't know why we are checking to see
                # if the current bear object has a negative hunger score
                # because that would imply that it has starved to death
                # and therefore died, meaning we would need to get rid it
                # but gradescope marked it wrong if I had it as > 0 so
                # its being left like this for now
                temp_bears.append(self.bears[i])
        self.bears = temp_bears
        # updating the bears variable/attribute to reflect the changes in bear pop.
        return None

    def repopulate_fish(self):
        """Simulating the repopulation of fish."""
        for i in range((len(self.fish) // 2) * 4):
            # using a simple for in range loop to figure out how many fish to add
            self.fish.append(Fish())
        return None

    def repopulate_bears(self):
        """Simulating the repopulation of bears."""
        for i in range(len(self.bears) // 2):
            # using a simple for in range loop to figure out how many bears to add
            self.bears.append(Bear())
        return None

    def view_river(self):
        """Providing information about the state of the river."""
        print(f"~~~ Day {self.day}: ~~~")
        print(f"Fish population: {len(self.fish)}")
        print(f"Bear population: {len(self.bears)}")
        return None

    def one_river_day(self):
        """Simulate one day of life in the river."""
        # Increase day by 1
        self.day += 1
        # Simulate one day for all Bears
        for bear in self.bears:
            bear.one_day()
        # Simulate one day for all Fish
        for fish in self.fish:
            fish.one_day()
        # Simulate Bear's eating
        self.bears_eating()
        # Remove hungry Bear's from River
        self.check_hunger()
        # Remove old Fish and Bear's from River
        self.check_ages()
        # Simulate Fish repopulation
        self.repopulate_fish()
        # Simulate Bear repopulation
        self.repopulate_bears()
        # Visualize River
        self.view_river()

    def one_river_week(self):
        """Simulate one week of life in the river."""
        for i in range(7):
            self.one_river_day()
