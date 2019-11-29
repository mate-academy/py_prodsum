"""module contains a prod of even and sum of odd numbers in list"""
from typing import List


def prodsum(numbers_list: List[int]) -> int:
    """:returns the diff of index between production of even
    and sum of odd numbers in the list"""
    if numbers_list:
        even_numbers_prod = 1
        odd_numbers_sum = 0
        for number, index in enumerate(numbers_list):
            if number % 2 == 0:
                even_numbers_prod = even_numbers_prod * index
            elif number % 2 == 1:
                odd_numbers_sum += index
        result = even_numbers_prod - odd_numbers_sum
        return result
    return 0
