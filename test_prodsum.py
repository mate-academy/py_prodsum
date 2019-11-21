import prodsum


def test_empty():
    assert prodsum.prod_sum_den_solution([]) == 0


def test_one_item():
    assert prodsum.prod_sum_den_solution([1]) == 1


def test_list():
    assert prodsum.prod_sum_den_solution([1, 2, 3, 4]) == -3