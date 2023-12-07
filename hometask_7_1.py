def numbers(tuple_numbers=(100, 4, 11, 777, 50, 10, 999)):
    sorted_tuple = sorted(tuple_numbers)
    return sorted_tuple


def numbers_2(tuple_numbers=[1, 14, 175, 1000, 5, 0, 2]):
    sorted_tuple = sorted(tuple_numbers, reverse=True)
    return sorted_tuple


def words_list(tuple_words=["оставь", "надежду", "всяк", "сюда", "входящий"]):
    sorted_words_tuple = sorted(tuple_words, key=len)
    return sorted_words_tuple
