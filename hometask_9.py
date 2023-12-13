# task №2
def error(value_1, value_2) -> int | float:
    try:
        print(value_1 + value_2)
    except TypeError as T:
        print(f'We got error "{T}"')


error(1000, "Привіт, як справи?")


# task №3
def add_three_numbers(value_1, value_2, value_3) -> int | float:
    result = value_1 + value_2 + value_3
    return result


# task №4
from datetime import datetime
import time


def wrapper_1(func):
    def func_wrapper_time(*args, **kwargs):
        start = datetime.now()
        time.sleep(5)
        delta_time = datetime.now() - start
        print("Час виконання функції ось такий: ", delta_time)
        result = func(*args, **kwargs)
        return result

    return func_wrapper_time


@wrapper_1
def foo_time(*args, **kwargs):
    print("foo_time")


foo_time()
