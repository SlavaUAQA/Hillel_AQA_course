import pytest
from hometask_7_1 import numbers
from hometask_7_1 import numbers_2
from hometask_7_1 import words_list
def test_numbers():
    result = numbers()
    for i in range(len(result) - 1):
        assert result[i] <= result[i + 1], "Список не отсортирован"

def test_numbers_2():
    result = numbers_2()
    for i in range(len(result) - 1):
        assert result[i] >= result[i+1], "Список не отсортирован"

def test_words_list():
    result = words_list()
    for i in range(len(result) - 1):
        assert len(result[i]) <= len(result[i + 1]), "Список не отсортирован"
