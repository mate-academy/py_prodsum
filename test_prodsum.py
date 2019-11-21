"""
docstring
"""
import prodsum


def test_empty():
    """

    :return:
    """
    assert prodsum.prodsum([]) == 0


def test_one_item():
    """

    :return:
    """
    assert prodsum.prodsum([1]) == 1


def test_list():
    """

    :return:
    """
    assert prodsum.prodsum([1, 2, 3, 4]) == -3
