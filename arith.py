# coding: utf8
from basic import *


def DOUBLE_TROUBLE(i1: bool, i2: bool, i3: bool, i4: bool) -> bool:
    """true if there are at least two trues"""
    # [18] NAND
    # return OR3(AND(i1, i2), AND(OR(i1, i2), OR(i3, i4)), AND(i3, i4))
    # [12] NAND
    return NAND(AND(NAND(i1, i2), NAND(OR(i1, i2), OR(i3, i4))), NAND(i3, i4))


def ODD_SIGNALS(i1: bool, i2: bool, i3: bool, i4: bool) -> bool:
    """true only when there is odd number of trues"""
    # [12] NAND
    return XOR(XOR(i1, i2), XOR(i3, i4))
    # [12] NAND
    # return XOR(XOR(XOR(i1, i2), i3), i4)


def _B2D_3(i1: bool, i2: bool, i3: bool) -> int:
    """converting 3 bool inputs to an int"""
    return 1 * int(i1) + 2 * int(i2) + 4 * int(i3)


def COUNTING_SIGNALS(i1: bool, i2: bool, i3: bool, i4: bool) -> int:
    """counting how many trues are inputted

    Hint1:
    The easiest one is when it should be 4.
    The answer is when every input is true.
    So there should be 3 AND gate and connect the output to the third.

    Hint2:
    The first output will be true when the count is 1 or 3.
    Ring some bell?
    Yeah, it's the ODD SIGNAL.
    So there should be 3 XOR gate and connect the output to the first.

    Hint3:
    XOR can be considered as a controlled NOT gate.
    If we think input 1 is the input, and input 2 is the controller,
    then when the controller is on, the output will be the inverse of the input,
    and when the controller is off, the output will be the same as the input.

    Hint4:
    The second output will be true when the count is 2 or 3.
    How should we implement this?
    With hint3, we can have the output being true when the count is 2 or 3 or 4,
    and XOR 4 to exclude it.
    So, yeah, it's the DOUBLE TROUBLE.
    """
    # [34] NAND
    v1 = ODD_SIGNALS(i1, i2, i3, i4)
    v2 = DOUBLE_TROUBLE(i1, i2, i3, i4)
    v3 = AND(i1, i2)
    v4 = AND(i3, i4)
    w = AND(v3, v4)
    return _B2D_3(v1, XOR(v2, w), w)


def HALF_ADDER(i1: bool, i2: bool) -> tuple[bool, bool]:
    """the return is (sum, carry)"""
    # [6] NAND
    return XOR(i1, i2), AND(i1, i2)


def FULL_ADDER(i1: bool, i2: bool, i3: bool) -> tuple[bool, bool]:
    """the return is (sum, carry)"""
    # [15] NAND
    # s1, c1 = HALF_ADDER(i1, i2)
    # s2, c2 = HALF_ADDER(s1, i3)
    # return s2, OR(c1, c2)
    # [11] NAND
    v1 = NAND(i1, i2)
    v2 = XOR(i1, i2)
    w1 = NAND(v2, i3)
    w2 = XOR(v2, i3)
    return w2, NAND(v1, w1)


def BIT_SWITCH(i: bool, c: bool) -> bool:
    """when c is on, the output is i, or is always false"""
    return AND(i, c)


def BIT_INVERTER(i: bool, c: bool) -> bool:
    """when c is on, the output is the inverse of i, or is i"""
    return XOR(i, c)


Bit8 = tuple[bool, ...]  # actually 8 bools


class Byte(object):
    def __init__(self, value: int):
        if not (0 <= value <= 255):
            raise ValueError(f"{value} is out of range 0..255")
        self.value = value


def _B2b(i: Byte) -> Bit8:
    bit = f"{bin(i.value).removeprefix('0b'):>08}"
    return tuple(map(lambda x: bool(int(x)), list(bit)[::-1]))


def _b2B(i: Bit8) -> Byte:
    bit = "".join(map(lambda x: str(int(x)), i[::-1]))
    return Byte(int(bit, 2))


def BYTE_OR(i1: Byte, i2: Byte) -> Byte:
    return _b2B(tuple([OR(x, y) for x, y in zip(_B2b(i1), _B2b(i2))]))


def BYTE_NOT(i: Byte) -> Byte:
    return _b2B(tuple([NOT(x) for x in _B2b(i)]))


def BYTE_ADD(i1: Byte, i2: Byte, c: bool) -> tuple[Byte, bool]:
    b1 = _B2b(i1)
    b2 = _B2b(i2)
    cy = c
    sm = []
    for x, y in zip(b1, b2):
        s, cy = FULL_ADDER(x, y, cy)
        sm.append(s)
    return _b2B(tuple(sm)), cy


def BYTE_SWITCH(i: Byte, c: bool) -> Byte:
    return _b2B(tuple([AND(x, c) for x in _B2b(i)]))


