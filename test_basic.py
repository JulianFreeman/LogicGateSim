# coding: utf8
from basic import *


def test_nand():
    assert NAND(False, False) is True
    assert NAND(True, False) is True
    assert NAND(False, True) is True
    assert NAND(True, True) is False


def test_not():
    assert NOT(False) is True
    assert NOT(True) is False


def test_and():
    assert AND(False, False) is False
    assert AND(True, False) is False
    assert AND(False, True) is False
    assert AND(True, True) is True


def test_nor():
    assert NOR(False, False) is True
    assert NOR(True, False) is False
    assert NOR(False, True) is False
    assert NOR(True, True) is False


def test_or():
    assert OR(False, False) is False
    assert OR(True, False) is True
    assert OR(False, True) is True
    assert OR(True, True) is True


def test_always_on():
    assert ALWAYS_ON(False) is True
    assert ALWAYS_ON(True) is True


def test_second_tick():
    assert SECOND_TICK(False, True) is False
    assert SECOND_TICK(True, False) is True
    assert SECOND_TICK(False, True) is False
    assert SECOND_TICK(True, True) is False


def test_xor():
    assert XOR(False, False) is False
    assert XOR(True, False) is True
    assert XOR(False, True) is True
    assert XOR(True, True) is False


def test_or3():
    assert OR3(False, False, False) is False
    assert OR3(True, False, False) is True
    assert OR3(False, True, False) is True
    assert OR3(True, True, False) is True
    assert OR3(False, False, True) is True
    assert OR3(True, False, True) is True
    assert OR3(False, True, True) is True
    assert OR3(True, True, True) is True


def test_and3():
    assert AND3(False, False, False) is False
    assert AND3(True, False, False) is False
    assert AND3(False, True, False) is False
    assert AND3(True, True, False) is False
    assert AND3(False, False, True) is False
    assert AND3(True, False, True) is False
    assert AND3(False, True, True) is False
    assert AND3(True, True, True) is True


def test_xnor():
    assert XNOR(False, False) is True
    assert XNOR(True, False) is False
    assert XNOR(False, True) is False
    assert XNOR(True, True) is True


def main():
    for f in globals():
        if f.startswith("test_"):
            eval(f"{f}()")


if __name__ == '__main__':
    main()
