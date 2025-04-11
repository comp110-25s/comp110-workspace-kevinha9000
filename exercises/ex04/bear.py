"""File to define Bear class."""

__author__ = "730758718"


class Bear:
    age: int
    hunger_score: int

    def __init__(self):
        """Bear initialization"""
        self.age = 0
        self.hunger_score = 0
        return None

    def one_day(self):
        self.age += 1
        self.hunger_score -= 1
        return None

    def eat(self, num_fish: int):
        """Updates bears hunger score"""
        self.hunger_score += num_fish
