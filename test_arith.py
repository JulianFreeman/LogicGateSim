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


def test_half_adder():
    assert HALF_ADDER(False, False) == (False, False)
    assert HALF_ADDER(True, False) == (True, False)
    assert HALF_ADDER(False, True) == (True, False)
    assert HALF_ADDER(True, True) == (False, True)


def test_full_adder():
    assert FULL_ADDER(False, False, False) == (False, False)
    assert FULL_ADDER(True, False, False) == (True, False)
    assert FULL_ADDER(False, True, False) == (True, False)
    assert FULL_ADDER(True, True, False) == (False, True)
    assert FULL_ADDER(False, False, True) == (True, False)
    assert FULL_ADDER(True, False, True) == (False, True)
    assert FULL_ADDER(False, True, True) == (False, True)
    assert FULL_ADDER(True, True, True) == (True, True)


def test_bit_switch():
    assert BIT_SWITCH(False, False) is False
    assert BIT_SWITCH(True, False) is False
    assert BIT_SWITCH(False, True) is False
    assert BIT_SWITCH(True, True) is True


def test_bit_inverter():
    assert BIT_INVERTER(False, False) is False
    assert BIT_INVERTER(True, False) is True
    assert BIT_INVERTER(False, True) is True
    assert BIT_INVERTER(True, True) is False


# too time consuming
# def test_byte_or():
#     for i in range(0, 256):
#         for j in range(0, 256):
#             assert BYTE_OR(Byte(i, False), Byte(j, False)).value == i | j
#
#     for i in range(-128, 128):
#         for j in range(-128, 128):
#             assert BYTE_OR(Byte(i, True), Byte(j, True)).value == i | j

# def test_byte_not():
#     for i in range(0, 256):
#         assert BYTE_NOT(Byte(i)) == ~i


# too time consuming
# def test_byte_add():
#     for i in range(0, 256):
#         for j in range(0, 256):
#             for z in [False, True]:
#                 bv, c = BYTE_ADD(Byte(i, False), Byte(j, False), z)
#                 dv, m = divmod(i + j + int(z), 256)
#                 assert (bv.value, c) == (m, bool(dv))

    # for i in range(-128, 128):
    #     for j in range(-128, 128):
    #         for z in [False, True]:
    #             bv, c = BYTE_ADD(Byte(i, True), Byte(j, True), z)
    #             dv, m = divmod(i + j + int(z), 128)
    #             try:
    #                 assert (bv.value, c) == (m, bool(dv))
    #             except AssertionError:
    #                 print(bv.value, c, m, dv)
    #                 print(i, j, z)
    #                 raise AssertionError


# too time consuming
# def test_byte_switch():
#     for i in range(0, 256):
#         assert BYTE_SWITCH(Byte(i, False), False).value == 0
#         assert BYTE_SWITCH(Byte(i, False), True).value == i
#
#     for i in range(-128, 128):
#         assert BYTE_SWITCH(Byte(i, True), False).value == 0
#         assert BYTE_SWITCH(Byte(i, True), True).value == i


# too time consuming
# def test_byte_selector():
#     for i in range(0, 256):
#         for j in range(0, 256):
#             assert BYTE_SELECTOR(Byte(i, False), Byte(j, False), False).value == j
#             assert BYTE_SELECTOR(Byte(i, False), Byte(j, False), True).value == i
#
#     for i in range(-128, 128):
#         for j in range(-128, 128):
#             assert BYTE_SELECTOR(Byte(i, True), Byte(j, True), False).value == j
#             assert BYTE_SELECTOR(Byte(i, True), Byte(j, True), True).value == i


# too time consuming
# def test_signed_negator():
#     for i in range(-127, 128):
#         assert SIGNED_NEGATOR(Byte(i, True)).value == -i


# def test_the_bus():
#     for i in range(0, 256):
#         for j in range(0, 256):
#             x, y = Byte(i, False), Byte(j, False)
#             assert THE_BUS(x, y, False, False) == (0, y)
#             assert THE_BUS(x, y, True, False) == (0, x)
#             assert THE_BUS(x, y, False, True) == (y, 0)
#             assert THE_BUS(x, y, True, True) == (x, 0)

    # for i in range(-128, 128):
    #     for j in range(-128, 128):
    #         x, y = Byte(i, True), Byte(j, True)
    #         assert THE_BUS(x, y, False, False) == (0, y)
    #         assert THE_BUS(x, y, True, False) == (0, x)
    #         assert THE_BUS(x, y, False, True) == (y, 0)
    #         assert THE_BUS(x, y, True, True) == (x, 0)


def test_delay_one():
    a = (False, True, True, False, False, False, True, True, True)
    b = []
    do = DELAY_ONE()
    for e in a:
        b.append(do(e))
    assert tuple(b) == (False, False, True, True, False, False, False, True, True)


def test_odd_ticks():
    ot = ODD_TICKS()
    b = []
    for _ in range(9):
        b.append(ot())
    assert tuple(b) == (False, True, False, True, False, True, False, True, False)


def test_save_gracefully():
    enable = (True, True, True, True, False, False, True, True, True, False, False, True)
    save = (True, True, False, False, False, True, False, True, True, True, False, False)
    desired = (False, True, True, False, False, False, False, False, True, True, True, True)
    sg = SAVE_GRACEFULLY()
    b = []
    for i in range(len(save)):
        b.append(sg(enable[i], save[i]))
    assert tuple(b) == desired



def main():
    for f in globals():
        if f.startswith("test_"):
            eval(f"{f}()")


if __name__ == '__main__':
    main()
