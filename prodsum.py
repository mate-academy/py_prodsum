"""Find difference between
product of items with even index
and sum of items with odd index
"""

from typing import List


def prodsum(nums: List[int]) -> int:
    """General function"""
    if not nums:
        return 0

    even = 1
    odd = 0

    for index, value in enumerate(nums):
        if index % 2 == 0:
            even *= value
        else:
            odd += value
    return even - odd
