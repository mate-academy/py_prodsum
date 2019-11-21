"""
prodsum: functions return difference between odds product and evens sum from list
"""
from typing import List


def prodsum(numbers: List[int]) -> int:
    """

    :param numbers: [int] list of odds and evens
    :return: int difference between odds product and evens sum
    """
    odd = 0
    even = 0

    if len(numbers) >= 1:
        odd = 1

    for number in numbers:
        if number % 2 == 0:
            even += number
        else:
            odd *= number

    return odd - even
