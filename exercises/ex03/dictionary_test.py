__author__ = "730758718"
from dictionary import invert
from dictionary import count
from dictionary import favorite_color
from dictionary import bin_len


def test_invert() -> None:
    assert invert({"1": "2", "3": "4"}) == {"2": "1", "4": "3"}
    assert invert({"tofu": "rice"}) == {"rice": "tofu"}
    assert invert({}) == {}
    assert None


def test_count() -> None:
    assert count(["z", "y", "x", "y", "z", "x"]) == {"z": 2, "y": 2, "x": 2}
    assert count(["tofu", "rice", "rice", "tofu"]) == {"tofu": 2, "rice": 2}
    assert count([])
    return None


def test_favorite_color() -> None:
    assert (
        favorite_color({"Kevin": "black", "Brian": "white", "Chris": "black"})
        == "black"
    )
    assert (
        favorite_color(
            {"Kevin": "black", "Brian": "white", "Chris": "black", "Tim": "black"}
        )
        == "black"
    )
    assert favorite_color({}) == ""
    return None


def test_bin_len() -> None:
    assert bin_len(["super", "idol", "four", "fives", "two"]) == {
        5: {"super", "fives"},
        4: {"idol", "four"},
        3: {"two"},
    }
    assert bin_len(["fort", "nite", "fort", "nite", "fort", "nite"]) == {
        4: {"fort", "nite"}
    }
    return None
