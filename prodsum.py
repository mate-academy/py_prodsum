"""
docstring
"""


def prodsum(lst):
    """

    :param lst:
    :return:
    """
    prod_even = 1
    sum_odd = 0
    if len(lst) == 0:
        return 0
    for index, item in enumerate(lst):
        if index % 2 == 0:
            prod_even *= item
        elif index % 2 != 0:
            sum_odd += item
    return prod_even - sum_odd
