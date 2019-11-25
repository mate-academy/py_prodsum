"""Find the difference between the product of the even and the sum of the odd list items"""
from typing import List


def prodsum(list_of_elements: List[int]) -> int:
    """Difference between the product of the even and the sum of the odd"""
    result = 1
    if list_of_elements:
        evens = list(filter(lambda x: (x % 2 == 0), list_of_elements))
        odds = list(filter(lambda x: (x % 2 != 0), list_of_elements))
        for _ in odds:
            result = result * _
        return result - sum(evens)
    return 0
