"""testing our utility functions"""

__author__: str = "730767591"

from exercises.ex05.utils import only_evens, sub, add_at_index
import pytest


def test_edge_case_only_evens() -> None:
    """Testing the edge case for the only_evens function"""
    test_list: list[int] = []
    # if list is empty, the function should return an empty list
    assert only_evens(input_list=test_list) == []


def test_expected_only_evens() -> None:
    """Testing testing for expected outputs using only_evens function"""
    test_list: list[int] = [1, 2, 3, 4, 5, 6]
    # should only return the even values of the list
    assert only_evens(input_list=test_list) == [2, 4, 6]


def test_mutated_only_evens() -> None:
    """Testing the only_evens for any mutations to the lists"""
    test_list: list[int] = [1, 2, 3, 4, 5, 6]
    only_evens(input_list=test_list)
    # The original list should remain unmutated
    assert test_list == [1, 2, 3, 4, 5, 6]


def test_edge_case_sub() -> None:
    """Testing edge_case for sub function"""
    test_list: list[int] = [1, 2, 3, 4, 5, 6]
    # If the start index is greater than the largest index, return empty function
    assert sub(input_list=test_list, start=6, end=0) == []


def test_expected_sub() -> None:
    """Testing sub function for expected outputs"""
    test_list: list[int] = [1, 2, 3, 4, 5, 6]
    # should only return a list with the elements from index 2 to 5(not incl.)
    assert sub(input_list=test_list, start=2, end=5) == [3, 4, 5]


def test_mutated_sub() -> None:
    """Testing the sub funcition for list mutations"""
    test_list: list[int] = [1, 2, 3, 4, 5, 6]
    sub(input_list=test_list, start=6, end=0)
    # Sub function should not mutate original list
    assert test_list == [1, 2, 3, 4, 5, 6]


def test_add_at_index_raises_indexerror() -> None:
    """Testing the add_at_index function for error catching"""

    with pytest.raises(IndexError):
        test_list: list[int] = [1, 2, 3, 4, 5, 6]
        # since our index is negative, an error should be raised
        add_at_index(input_list=test_list, value=7, index=-1)


def test_expected_add_at_index() -> None:
    """Testing to see if add_at_index gives us the expected output"""
    test_list: list[int] = [1, 2, 3, 4, 5, 6]
    # The add_at_index function should not return any value
    assert add_at_index(input_list=test_list, value=3, index=2) == None


def test_mutated_add_at_index() -> None:
    """Testing to see if add_at_index properly mutates a list"""
    test_list: list[int] = [1, 2, 4, 5, 6]
    add_at_index(input_list=test_list, value=3, index=2)
    # The add_at_index function should mutate the imput list
    assert test_list == [1, 2, 3, 4, 5, 6]
