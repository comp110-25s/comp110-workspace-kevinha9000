"""File to define River class."""

from exercises.EX04.fish import Fish
from exercises.EX04.bear import Bear


class River:
    age: int
    bear: list[Bear]
    fish: list[Fish]

    def __init__(self, num_fish: int, num_bears: int):
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
        """Checks ages of fish and bears. Removes when too old"""
        bears_alive: list[Bear] = []
        for x in self.bears:
            if not i.age >5: 
                bears_alive.append(x)
        self.bears = bears_alive

        fish_alive: list[Fish] = []
        for x in self.fish
            if not i.age>3:
                fish_alive.append(x)
        self.fish = fish_alive

        return None
    
    def remove_fish(self, amount: int):
        """removes amount fish from river"""
        self.fish = self.fish[amount:]

    def bears_eating(self):
        number_bears: int = 0
        while len(self.fish) >= 5:
            self.remove_fish(3)
            self.bears[number_bears].eat(3)
            number_bears += 1
        return None

    def check_hunger(self):
        bears_alive: list[Bear] = []
        for x in self.bears:
            if notx.hunger_score < 0:
                bears_alive.append(x)
        self.bears = bears_alive
        return None

    def repopulate_fish(self):
        """fish come back"""
        for _ in range((len(self.fish)//2) *4):
            self.fish.append(Fish())
        return None

    def repopulate_bears(self):
        """bears come back"""
        for _ in range(len(self.bears)//2):
            self.bears.append(Bear())
        return None

    def view_river(self):
        print(f" ~~~ Day {self.day}:~~~")
        print(f" Fish Population: {len(self.fish)}")
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
        self.one_river_day = 7
