"""doc"""
from typing import List


def prodsum(arr: List[int]) -> int:
    """calculates difference between the product of the even and the sum of the odd list items"""
    # nothing to calculate in empty or short list
    if not arr:
        return 0
    if len(arr) < 2:
        return arr[0]

    product_of_even = 1
    sum_of_odd = 0

    for element in arr:
        if arr.index(element) % 2 == 0:
            product_of_even *= element
        else:
            sum_of_odd += element

    return product_of_even - sum_of_odd
