"""
Find the difference between the
product of the even and the sum
of the odd list items
"""

from typing import List


def prodsum(nums: List[int]) -> int:
    """ Func """
    if len(nums) == 0:
        return 0

    even = 0
    odd = 1

    for num in nums:
        if num % 2 == 0:
            even += num
        else:
            odd *= num
    return odd - even

# print(prodsum([1, 2, 3, 4]))
