"""File to define River class."""
__author__: str = "730767591"

from exercises.ex07.fish import Fish
from exercises.ex07.bear import Bear

class River:
    """Establishing our River Class"""
    day: int
    fish: list[Fish]
    bears: list[Bear]
    
    def __init__(self, num_fish: int, num_bears:int):
        """New River with num_fish Fish and num_bears Bears"""
        self.day: int = 0
        self.fish: list[Fish] = []
        self.bears: list[Bear] = []
        # populate the river with fish and bears
        for _ in range(0, num_fish):
            self.fish.append(Fish())
        for _ in range(0, num_bears):
            self.bears.append(Bear())

    def check_ages(self):
        """Checking the ages of fish and bears"""
        temp_fish: list[Fish] = []
        for i in self.fish:
            if i.age <= 3:
                temp_fish.append(i)
        self.fish = temp_fish

        temp_bears: list[Bear] = []
        for j in self.bears:
            if j.age <= 5:
                temp_bears.append(j)
        self.bears = temp_bears

        return None
    
    def remove_fish(self, amount: int) -> None:
        for i in range(amount):
            self.fish.pop(0)
        return None 

    def bears_eating(self):
        for i in self.bears:
            if len(self.fish) >= 5:
                self.remove_fish(3)
                i.eat(num_fish=3)
        
        return None
    
    def check_hunger(self):
        temp_bears: list[Bear] = []
        for i in range(len(self.bears)):
            if self.bears[i].hunger_score < 0:
                temp_bears.append(self.bears[i])
        self.bears = temp_bears
        return None
        
    def repopulate_fish(self):
        for i in range((len(self.fish)//2) * 4):
            self.fish.append(Fish())
        return None
    
    def repopulate_bears(self):
        for i in range(len(self.bears)//2):
            self.bears.append(Bear())
        return None
    
    def view_river(self):
        print(f"~~~ Day {self.day}: ~~~")
        print(f"Fish population: {len(self.fish)}")
        print(f"Bear population: {len(self.bears)}")
        return None
            
    def one_river_day(self):
        """Simulate one day of life in the river"""
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