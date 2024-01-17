# -*- coding: utf-8 -*-
import pytest
from hometask_15 import calculator
from datetime import datetime


class TestCalculator:

    @pytest.fixture
    def setup(self):
        current_time = datetime.now()
        with open("log.txt", "a") as file:
            file.write(f"Ми стартовали тест в {current_time}\n")
        yield

    @pytest.fixture
    def teardown(self):
        with open("log.txt", "a") as file:
            current_time = datetime.now()
            file.write(f"Ми закінчили тест в {current_time}\n")

    @pytest.mark.usefixtures("setup", "teardown")
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

    @pytest.mark.usefixtures("setup", "teardown")
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
