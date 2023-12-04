def numbers(list_numbers = [100, 4, 11, 777, 50, 10, 999]):
    sorted_list = sorted(list_numbers)
    return sorted_list


def numbers_2(list_numbers = [1, 14, 175, 1000, 5, 0, 2]):
    sorted_list = sorted(list_numbers, reverse=True)
    return sorted_list


def words_list(list_words = ["оставь", "надежду", "всяк", "сюда", "входящий"]):
    sorted_words_list = sorted(list_words, key = len)
    return sorted_words_list
