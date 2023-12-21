# task-2

def add_input(func):
    def wrapper(value_1, value_2, value_3):
        with open("log.txt", "a") as add_data:
            add_data.write(f'{'число 1'}: {value_1}\n{'число 2'}: {value_2}\n{'число 3'}: {value_3}\n')
            result = func(value_1, value_2, value_3)
            add_data.write(f'{'результат'}: {result}\n')
    return wrapper


@add_input
def add_three_numbers(value_1, value_2, value_3) -> int | float:
    result = value_1 + value_2 + value_3
    return result


add_three_numbers(4, 10, 7)
