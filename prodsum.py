"""module docstring"""
#from typing import List

def prodsum(initial_list):
    """func docstring"""
    if initial_list == []:
        evens_product = 0
    else:
        evens_product = 1
    odds_sum = 0
    for seq, value in enumerate(initial_list):
        if seq % 2 == 0:
            evens_product *= value
        else:
            odds_sum += value
    result = evens_product - odds_sum
    return result
