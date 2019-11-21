"""prodsum module"""
from typing import List


def prodsum(digits: List[int]) -> int:
    """prodsum function"""
    if len(digits) < 2:
        try:
            return digits[0]
        except IndexError:
            return 0
    product = 1
    summa = 0
    for index, digit in enumerate(digits):
        if index % 2 == 0:
            product *= digit
        else:
            summa += digit
    return product - summa
