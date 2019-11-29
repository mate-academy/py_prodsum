"""module prodsum"""


from typing import List


def prodsum(item_list: List[int]) -> int:
    """return prudct - sum"""
    if not item_list:
        return 0
    product = 1
    sum_item = 0
    for i in item_list[::2]:
        product = product * i
    for i in item_list[1::2]:
        sum_item = sum_item + i
    return product - sum_item
