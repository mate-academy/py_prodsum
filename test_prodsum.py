import prodsum


def test_empty():
    assert prodsum.prodsum([]) == 0


def test_one_item():
    assert prodsum.prodsum([1]) == 1


def test_list():
    assert prodsum.prodsum([1, 2, 3, 4]) == -3