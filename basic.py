# coding: utf8

def NAND(i1: bool, i2: bool) -> bool:
    return not (i1 and i2)


def NOT(i: bool) -> bool:
    # [1] NAND
    return NAND(i, i)


def AND(i1: bool, i2: bool) -> bool:
    """AND is NOT NAND"""
    # [2] NAND
    return NOT(NAND(i1, i2))


def NOR(i1: bool, i2: bool) -> bool:
    """not (a or b) is (not a) and (not b)"""
    # [4] NAND
    # return AND(NOT(i1), NOT(i2))
    # [4] NAND
    return NOT(NAND(NOT(i1), NOT(i2)))


def OR(i1: bool, i2: bool) -> bool:
    """OR is NOT NOR"""
    # [5] NAND
    # return NOT(NOR(i1, i2))
    # [3] NAND
    return NAND(NOT(i1), NOT(i2))


def ALWAYS_ON(i: bool) -> bool:
    """at least one of them will be true, so OR will always be true"""
    # [4] NAND
    return OR(i, NOT(i))


def SECOND_TICK(i1: bool, i2: bool) -> bool:
    """only the second tick is true"""
    # [3] NAND
    return AND(i1, NOT(i2))


def XOR(i1: bool, i2: bool) -> bool:
    # return OR(SECOND_TICK(i1, i2), SECOND_TICK(i2, i1))
    # [9] NAND
    # return OR(AND(i1, NOT(i2)), AND(NOT(i1), i2))
    # [5] NAND
    # return NAND(NAND(i1, NOT(i2)), NAND(NOT(i1), i2))
    # [4] NAND
    v = NAND(i1, i2)
    return NAND(NAND(i1, v), NAND(v, i2))


def OR3(i1: bool, i2: bool, i3: bool) -> bool:
    # [6] NAND
    return OR(OR(i1, i2), i3)


def AND3(i1: bool, i2: bool, i3: bool) -> bool:
    # [4] NAND
    return AND(AND(i1, i2), i3)


def XNOR(i1: bool, i2: bool) -> bool:
    """XNOR is NOT XOR"""
    # [5] NAND
    return NOT(XOR(i1, i2))


