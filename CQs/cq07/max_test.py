"""Utilizing python testing"""

__author__: str = "730767591"

from CQs.cq07.find_max import find_and_remove_max


def test_find_and_remove_max_expected() -> None:
    assert find_and_remove_max([67, -230, 593, 593, 0, 45]) == 593


def test_find_and_remove_max_mutate() -> None:
    b: list[int] = [67, -230, 593, 593, 0, 45]
    find_and_remove_max(b)
    assert b == [67, -230, 0, 45]


def test_find_and_remove_max_edge_case() -> None:
    assert find_and_remove_max([]) == -1
