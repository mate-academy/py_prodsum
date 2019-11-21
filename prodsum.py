"""Doctring"""
from typing import List


def prodsum(lis: List[int]) -> int:
    """
    Returns difference between
    product of int from the list that have even indexes
    and sum of int - that have odd indexes
    """
    even_prod = 1
    odd_sum = 0
    for idx, number in enumerate(lis):
        if idx % 2 == 0:
            even_prod *= number
        else:
            odd_sum += number

    return even_prod - odd_sum if lis else 0
