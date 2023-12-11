def numbers(tuple_numbers=()):
    tuple_inside = tuple_numbers
    tuple_inside = (100, 4, 11, 777, 50, 10, 999)
    sorted_tuple = sorted(tuple_inside)
    return sorted_tuple

def numbers_2(tuple_numbers=()):
    tuple_inside = tuple_numbers
    tuple_inside = (100, 4, 11, 777, 50, 10, 999)
    sorted_tuple = sorted(tuple_inside, reverse=True)
    return sorted_tuple

def words_list(tuple_words=()):
    words_inside_tuple = words_list
    words_inside_tuple = ["оставь", "надежду", "всяк", "сюда", "входящий"]
    sorted_words_tuple = sorted(words_inside_tuple, key=len)
    return sorted_words_tuple

