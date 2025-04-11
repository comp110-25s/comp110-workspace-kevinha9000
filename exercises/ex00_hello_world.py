"""My first exercise in COMP110!"""

__author__ = "730758718"


def greet(name: str) -> str:
    """A welcome first function definition."""
    return "Hello, " + name + "!"


if __name__ == "__main__":
    print(greet(name=input("What is your name? ")))
