from hometask_9 import add_three_numbers
import pytest


# solution 1
def test_1_solution_1():
    assert add_three_numbers(5, 10, 100) == 115


def test_2_solution_1():
    assert add_three_numbers(-5, -10, -100) == -115


def test_3_solution_1():
    assert add_three_numbers(0, 0, 0) == 0


# solution_2
@pytest.mark.parametrize("value_1, value_2, value_3, result", [
    (1, 2, 3, 6),
    (-1, -2, -3, -6),
    (-5, 5, 10, 10),
    (0, 0, 0, 0)
])
def test_solution_2(value_1, value_2, value_3, result):
    result_inside = add_three_numbers(value_1, value_2, value_3)  #
    assert result_inside == result


# solution_3

test_set = [(5, 5, 10, 20), (-5, -5, -10, -20), (-5, 5, 10, 10), (0, 0, 0, 0)]


@pytest.mark.parametrize("value_1, value_2, value_3, result", test_set)
def test_solution_3(value_1, value_2, value_3, result):
    assert add_three_numbers(value_1, value_2, value_3) == result
