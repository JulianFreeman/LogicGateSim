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
    # [2] NAND
    return AND(i, c)


def BIT_INVERTER(i: bool, c: bool) -> bool:
    """when c is on, the output is the inverse of i, or is i"""
    # [4] NAND
    return XOR(i, c)


Bit8 = tuple[bool, ...]  # actually 8 bools


def BIT8_NOT(i: Bit8) -> Bit8:
    """simply invert all the bits"""
    # [8] NAND
    return tuple([NOT(x) for x in i])


def BIT8_SWITCH(i: Bit8, c: bool) -> Bit8:
    """if c is on, the output is i, or is all false"""
    # [16] NAND
    return tuple([AND(x, c) for x in i])


def BIT8_OR(i1: Bit8, i2: Bit8) -> Bit8:
    # [24] NAND
    return tuple([OR(x, y) for x, y in zip(i1, i2)])


def BIT8_SELECTOR(i1: Bit8, i2: Bit8, c: bool) -> Bit8:
    """if c is on, the output is i1, or is i2"""
    # [57] NAND
    return BIT8_OR(BIT8_SWITCH(i1, c), BIT8_SWITCH(i2, NOT(c)))


def BIT8_ADD(i1: Bit8, i2: Bit8, c: bool) -> tuple[Bit8, bool]:
    # [88] NAND
    sm = []
    for x, y in zip(i1, i2):
        s, c = FULL_ADDER(x, y, c)
        sm.append(s)
    return tuple(sm), c


def BIT8_ADD_1(i: Bit8) -> tuple[Bit8, bool]:
    """this is a syntax sugar"""
    # [88] NAND
    return BIT8_ADD(i, (False, ) * 8, True)


class Byte(object):
    def __init__(self, value: int, signed=True):
        self.signed = True if value < 0 else signed
        if not self.signed:
            if not (0 <= value <= 255):
                raise ValueError(f"{value} is out of range 0..255")
        else:
            if not (-128 <= value <= 127):
                raise ValueError(f"{value} is out of range -128..127")
        self.value = value

    def __abs__(self):
        return Byte(abs(self.value), signed=False)

    def to_signed(self):
        return Byte(self.value, signed=True)

    def to_unsigned(self):
        # maybe fail
        return Byte(self.value, signed=False)

    def __repr__(self):
        p = "+" if self.signed and self.value >= 0 else ""
        return f"Byte({p}{self.value})"

    def __str__(self):
        return self.__repr__()


def _byte_to_bit8(i: Byte) -> Bit8:
    # [1] Splitter
    if (not i.signed) or i.value >= 0:
        bit = f"{bin(i.value).removeprefix('0b'):>08}"
        return tuple(map(lambda x: bool(int(x)), list(bit)[::-1]))
    else:
        # abs of Byte is always unsigned
        return BIT8_ADD_1(BIT8_NOT(_byte_to_bit8(abs(i))))[0]


def _bit8_to_byte(i: Bit8, signed: bool) -> Byte:
    # [1] Marker
    if signed and i[-1]:
        r = _bit8_to_byte(BIT8_ADD_1(BIT8_NOT(i))[0], False)
        return Byte(-r.value, signed)
    else:
        bit = "".join(map(lambda x: str(int(x)), i[::-1]))
        if (not any(i[:-1])) and i[-1]:
            # Byte(-128) should not be allowed
            # but, here it is, so we have to handle it
            return Byte(int(bit, 2), False)
        else:
            return Byte(int(bit, 2), signed=signed)


def BYTE_OR(i1: Byte, i2: Byte) -> Byte:
    # [24] NAND ...
    return _bit8_to_byte(BIT8_OR(_byte_to_bit8(i1), _byte_to_bit8(i2)), i1.signed or i2.signed)


def BYTE_NOT(i: Byte) -> Byte:
    # [8] NAND ...
    return _bit8_to_byte(BIT8_NOT(_byte_to_bit8(i)), i.signed)


def BYTE_ADD(i1: Byte, i2: Byte, c: bool) -> tuple[Byte, bool]:
    # [88] NAND ...
    b1 = _byte_to_bit8(i1)
    b2 = _byte_to_bit8(i2)
    s, c = BIT8_ADD(b1, b2, c)
    return _bit8_to_byte(s, i1.signed or i2.signed), c


def BYTE_SWITCH(i: Byte, c: bool) -> Byte:
    """if c is on, the output is i, or is 0"""
    # [16] NAND ...
    return _bit8_to_byte(BIT8_SWITCH(_byte_to_bit8(i), c), i.signed)


def BYTE_SELECTOR(i1: Byte, i2: Byte, c: bool) -> Byte:
    """if c is on, the output is i1, or is i2"""
    # [57] NAND ...
    return BYTE_OR(BYTE_SWITCH(i1, c), BYTE_SWITCH(i2, NOT(c)))


def SIGNED_NEGATOR(i: Byte) -> Byte:
    # [96] NAND ...
    # return _bit8_to_byte(BIT8_ADD_1(BIT8_NOT(_byte_to_bit8(i)))[0], i.signed)
    return BYTE_ADD(BYTE_NOT(i), Byte(0), True)[0]



