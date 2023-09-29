from functools import reduce


def _find_second_max(max_tuple, digit):
    # max_tuple -- (max1, max2)
    if digit > max_tuple[0]:
        return (digit, max_tuple[0])
    if digit > max_tuple[1]:
        return (max_tuple[0], digit)
    return max_tuple

def find_second_max(list_: list):
    if list_ == []:
        return None
    if len(list_) == 1:
        return list_[0]
    return reduce(
        _find_second_max, 
        list_,
        (float('-inf'), float('-inf')),
    )[1]