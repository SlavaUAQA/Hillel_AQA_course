# -*- coding: utf-8 -*-
class IsGreater:
    def __init__(self, lst):
        self.list = lst

    def __gt__(self, number):
        if isinstance(number, int):
            return [i > number for i in self.list]
        else:
            return TypeError


schedule_values = [2, 5, 8, 10, 15, 20]
is_greater_number = IsGreater(schedule_values)

print(is_greater_number.__gt__(10))
