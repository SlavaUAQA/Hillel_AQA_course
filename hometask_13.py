# -*- coding: utf-8 -*-
class IsGreater:
    def __init__(self, lst):
        self.list = lst

    def __gt__(self, number):
        if isinstance(number, int):
            return [i > number for i in self.list]
        else:
            return NotImplemented


schedule_values = [2, 5, 8, 10, 15, 20]
schedule_values_2 = [1, 3, 100, 5, 17, 50]
is_greater_number = IsGreater(schedule_values)
is_greater_number_2 = IsGreater(schedule_values_2)


print(is_greater_number.__gt__(10))
print(is_greater_number_2.__gt__(10))
