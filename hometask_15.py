# -*- coding: utf-8 -*-
import pytest

# task-1
spisok = [x for x in range(34, 121) if (x % 2 == 0 and (x % 3 == 0))]
print(spisok)


# task-2
class calculator():
    def adds(self, value_1, value_2):
        self.result = value_1 + value_2
        return self.result

    def subtr(self, value_1, value_2):
        self.result = value_1 - value_2
        return self.result

    def mult(self, value_1, value_2):
        self.result = value_1 * value_2
        return self.result

    def division(self, value_1, value_2):
        self.result = value_1 / value_2
        return self.result

    @staticmethod
    def say_hello():
        print("Привіт, я калькулятор")


object_1 = calculator()
result = object_1.mult(5, 10)
print(calculator.say_hello(), f'Результат вашої математичної дії дорівнює {result}')
