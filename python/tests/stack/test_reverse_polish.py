from reverse_polish import rpn


def test_reverse_polish():
    assert rpn(1, 2, 3, "+", "+") == 6
    assert rpn(1) == 1
    assert rpn(3, 4, "*", 2, "-") == 10
