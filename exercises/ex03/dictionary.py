__author__ = "730758718"


def invert(given_book: dict[str, str]) -> dict[str, str]:
    """Inverts the keys and values of the given dict(book)"""
    new_book: dict[str, str] = dict()
    for key in given_book:
        value = given_book[key]
        if value in new_book:
            raise KeyError("Dup Key found and failed to invert")
        else:
            new_book[value] = key
    return new_book


def count(provided_list: list[str]) -> dict[str, int]:
    """count items in given list and creates unique dictionary with repeated strings"""
    empty_dictionary: dict[str, int] = dict()
    for x in provided_list:
        if x in empty_dictionary:
            empty_dictionary[x] += 1
        else:
            empty_dictionary[x] = 1
    return empty_dictionary


def favorite_color(color_list: dict[str, str]) -> str:
    """Returns most frequent color"""
    color_num: dict[str, int] = {}
    for x in color_list:
        color = color_list[x]
        if color in color_num:
            color_num[color] += 1
        else:
            color_num[color] = 1
    color_lead: str = ""
    color_counter: int = 0
    for color in color_num:
        if color_num[color] > color_counter:
            color_lead = color
            color_counter = color_num[color]
    return color_lead


def bin_len(provided: list[str]) -> dict[int, set[str]]:
    """bins list of strings into a dict with same length words"""
    created_dict: dict[int, set[str]] = {}
    for value in provided:
        full_length = len(value)
        if full_length not in created_dict:
            created_dict[full_length] = set()
        created_dict[full_length].add(value)
    return created_dict
