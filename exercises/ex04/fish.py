"""File to define Fish class."""

__author__ = "730758718"


class Fish:
    age = 0

    def __init__(self):
        self.age = 0
        return None

    def one_day(self):
        self.age += 1
        return None
