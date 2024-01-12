# -*- coding: utf-8 -*-
import pytest
from hometask_15 import calculator
from datetime import datetime


class TestCalculator:

    @pytest.fixture
    def start_and_end(self):
        current_time = datetime.now()
        with open("log.txt", "a") as file:
            file.write(f"Ми стартовали тест в {current_time}\n")
        yield
        with open("log.txt", "a") as file:
            file.write(f"Ми закінчили тест в {current_time}\n")

    @pytest.mark.usefixtures("start_and_end")
    @pytest.mark.parametrize("value_1, value_2, expected_result", [
        (5, 10, 15),
        (5, 0, 5),
        (-5, 10, 5),
        (-5, -10, -15),
        (0, 0, 0)
    ])
    def test_addition(self, value_1, value_2, expected_result):
        calc = calculator()
        result = calc.adds(value_1, value_2)
        assert result == expected_result, f"Expected {expected_result}, but got {result}"

    @pytest.mark.usefixtures("start_and_end")
    @pytest.mark.parametrize("value_1, value_2, expected_result", [
        (100, 2, 50),
        (100, -5, -20),
        (-10, -10, 1),
        (-10, 5, -2),
        (0, 100, 0)])
    def test_division(self, value_1, value_2, expected_result):
        calc = calculator()
        result = calc.division(value_1, value_2)
        assert result == expected_result
