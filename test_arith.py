# coding: utf8
from arith import *


def test_double_trouble():
    assert DOUBLE_TROUBLE(False, False, False, False) is False
    assert DOUBLE_TROUBLE(True, False, False, False) is False
    assert DOUBLE_TROUBLE(False, True, False, False) is False
    assert DOUBLE_TROUBLE(True, True, False, False) is True
    assert DOUBLE_TROUBLE(False, False, True, False) is False
    assert DOUBLE_TROUBLE(True, False, True, False) is True
    assert DOUBLE_TROUBLE(False, True, True, False) is True
    assert DOUBLE_TROUBLE(True, True, True, False) is True
    assert DOUBLE_TROUBLE(False, False, False, True) is False
    assert DOUBLE_TROUBLE(True, False, False, True) is True
    assert DOUBLE_TROUBLE(False, True, False, True) is True
    assert DOUBLE_TROUBLE(True, True, False, True) is True
    assert DOUBLE_TROUBLE(False, False, True, True) is True
    assert DOUBLE_TROUBLE(True, False, True, True) is True
    assert DOUBLE_TROUBLE(False, True, True, True) is True
    assert DOUBLE_TROUBLE(True, True, True, True) is True


def test_odd_signals():
    assert ODD_SIGNALS(False, False, False, False) is False
    assert ODD_SIGNALS(True, False, False, False) is True
    assert ODD_SIGNALS(False, True, False, False) is True
    assert ODD_SIGNALS(True, True, False, False) is False
    assert ODD_SIGNALS(False, False, True, False) is True
    assert ODD_SIGNALS(True, False, True, False) is False
    assert ODD_SIGNALS(False, True, True, False) is False
    assert ODD_SIGNALS(True, True, True, False) is True
    assert ODD_SIGNALS(False, False, False, True) is True
    assert ODD_SIGNALS(True, False, False, True) is False
    assert ODD_SIGNALS(False, True, False, True) is False
    assert ODD_SIGNALS(True, True, False, True) is True
    assert ODD_SIGNALS(False, False, True, True) is False
    assert ODD_SIGNALS(True, False, True, True) is True
    assert ODD_SIGNALS(False, True, True, True) is True
    assert ODD_SIGNALS(True, True, True, True) is False


def test_counting_signals():
    assert COUNTING_SIGNALS(False, False, False, False) == 0
    assert COUNTING_SIGNALS(True, False, False, False) == 1
    assert COUNTING_SIGNALS(False, True, False, False) == 1
    assert COUNTING_SIGNALS(True, True, False, False) == 2
    assert COUNTING_SIGNALS(False, False, True, False) == 1
    assert COUNTING_SIGNALS(True, False, True, False) == 2
    assert COUNTING_SIGNALS(False, True, True, False) == 2
    assert COUNTING_SIGNALS(True, True, True, False) == 3
    assert COUNTING_SIGNALS(False, False, False, True) == 1
    assert COUNTING_SIGNALS(True, False, False, True) == 2
    assert COUNTING_SIGNALS(False, True, False, True) == 2
    assert COUNTING_SIGNALS(True, True, False, True) == 3
    assert COUNTING_SIGNALS(False, False, True, True) == 2
    assert COUNTING_SIGNALS(True, False, True, True) == 3
    assert COUNTING_SIGNALS(False, True, True, True) == 3
    assert COUNTING_SIGNALS(True, True, True, True) == 4


def main():
    for f in globals():
        if f.startswith("test_"):
            eval(f"{f}()")


if __name__ == '__main__':
    main()
