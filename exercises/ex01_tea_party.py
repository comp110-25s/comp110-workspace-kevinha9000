"""Calculate the cost of a tea party"""

__author__: str = "730758718"


def main_planner(guests: int) -> None:
    """Cost, Treats, and Tea Bags for the Party!"""
    print("A Cozy Tea Party for " + str(guests) + " People!")
    print("Tea Bags: " + str(tea_bags(people=guests)))
    print("Treats: " + str(treats(people=guests)))
    print(
        "Cost: $"
        + str(
            cost(tea_count=tea_bags(people=guests), treat_count=treats(people=guests))
        )
    )
    return None


def tea_bags(people: int) -> int:
    """Number of tea bags needed based on number of guests"""
    return people * 2


def treats(people: int) -> int:
    """Number of treats needed based on number of guests"""
    return int(tea_bags(people=people) * 1.5)


def cost(tea_count: int, treat_count: int) -> float:
    """compute the cost of the tea bags and the treats combined"""
    return tea_count * 0.50 + treat_count * 0.75


if __name__ == "__main__":
    main_planner(guests=int(input("How many guests are attending your tea party? ")))
