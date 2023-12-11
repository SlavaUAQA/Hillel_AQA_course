import pytest
from hometask_7_1 import numbers
from hometask_7_1 import numbers_2
from hometask_7_1 import words_list

def test_numbers():
    assert numbers([100, 4, 11, 777, 50, 10, 999]) == [4, 10, 11, 50, 100, 777, 999], "Список не отсортирован"

def test_numbers_2():
    assert numbers_2([100, 4, 11, 777, 50, 10, 999]) == [999, 777, 100, 50, 11, 10, 4], "Список не отсортирован"

def test_words_list():
    assert words_list(["оставь", "надежду", "всяк", "сюда", "входящий"]) == ["всяк", "сюда", "оставь", "надежду", "входящий"], "Список не отсортирован по длине слова"
