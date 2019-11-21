"""
prodsum module
"""
from typing import List


def prod_sum(lst: List[int]) -> int:
    """
    Return difference between the product of the even and the sum of the odd list items.
    :param lst: List[int]
    :return: int
    """
    sum_odd_nums = 0
    product_even_nums = 1

    if len(lst) == 0:
        return 0
    if len(lst) == 1:
        return lst[0]

    for idx, num in enumerate(lst):
        if idx % 2 == 0:
            product_even_nums *= num
        else:
            sum_odd_nums += num
    return product_even_nums - sum_odd_nums
