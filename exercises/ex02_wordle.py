"""Knock-off Wordle Coding Assignment"""

__author__: str = "730758718"


def contains_char(given_word: str, real_character: str) -> bool:
    """Scans for if a letter inside of the given word is also in the real character"""
    assert len(real_character) == 1, f"len('{real_character}') is not 1"

    I = 0
    while I < len(given_word):
        if real_character == given_word[I]:
            return True
        I += 1
    return False


WHITE_BOX: str = "\U00002B1C"
GREEN_BOX: str = "\U0001F7E9"
YELLOW_BOX: str = "\U0001F7E8"


def emojified(random_guess: str, real_word: str) -> str:
    """Assigns colored boxes depending on whether or not letters in random guessed word matches the hidden real word"""
    assert len(random_guess) == len(real_word), "Guess must be same length as secret"
    x = 0
    boxes: str = ""

    while x < len(random_guess):
        if contains_char(real_word, random_guess[x]):
            if random_guess[x] == real_word[x]:
                boxes += GREEN_BOX
            else:
                boxes += YELLOW_BOX
        else:
            boxes += WHITE_BOX
        x += 1
    return boxes


def input_guess(length: int) -> str:
    """Checks that answers given by guessers are correct length and notifies of incorrect length"""
    random_guess = input(f"Enter a {length} character word")
    while len(random_guess) != length:
        random_guess = input(f"That wasn't {length} chars! Try again:")
    return random_guess


def main(secret: str) -> None:
    """The entrypoint of the program and main game loop."""
    turn: int = 1
    while turn < 7:
        print(f"===Turn {turn}/6===")
        realtime_turn = input_guess(len(secret))
        print(emojified(realtime_turn, secret))
        if secret == realtime_turn:
            print(f"You won in {turn}/6 turns!")
            return None
        elif turn == 6:
            print("X/6 - Sorry, try again tomorrow!")
            return None
        else:
            turn += 1


if __name__ == "__main__":
    main(secret="codes")
