class IsGreater2:
    def __init__(self, number):
        self.number = number

    def __gt__(self, other):
        if self.number > other.number:
            return True
        else:
            return False


value_1 = 10
value_2 = 100
is_greater_number_1 = IsGreater2(value_1)
is_greater_number_2 = IsGreater2(value_2)
print(is_greater_number_2 > is_greater_number_1)
