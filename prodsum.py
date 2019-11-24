"""Find the difference between the product of the even and the sum of the odd list items"""
import math
from typing import List


def prodsum(list_of_elements: List[int]) -> int:
    """Difference between the product of the even and the sum of the odd"""
    if list_of_elements:
        evens = list(filter(lambda x: (x % 2 == 0), list_of_elements))
        odds = list(filter(lambda x: (x % 2 != 0), list_of_elements))
        return math.prod(odds) - sum(evens)
    return 0
