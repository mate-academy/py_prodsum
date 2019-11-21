'''
Module
'''
from typing import List


def prodsum(list_elem: List[int]) -> int:
    '''

    :param list_elem:
    :return:
    '''
    if len(list_elem) == 0:
        return 0
    product_elem = 1
    sum_elem = 0
    for i in list_elem[::2]:
        product_elem *= i
    for i in list_elem[1::2]:
        sum_elem += i
    return product_elem - sum_elem
