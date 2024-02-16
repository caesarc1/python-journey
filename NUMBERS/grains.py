"""
    Bitwise Operators (&, |, ~, ^):
    Bitwise Operators convert the numbers into bits and analyze each
    bit ('a' above 'b') according to the operator.

    Bitwise Shift Operators (<<, >>):

    Shifts the bits of a binary number towards left or right.
    
    Sign bit:

    At the beginning of every bit, there's a sign bit hidden. If it's 10,
    in bits would be '0'1010, if it's -10 in bits would be '1'1010. 0 = positive, 1 = negative

    Note: Only consider sign bits when it affect the result (~). For example, if both of the 
    binary numbers are positive, there's no need to consider sign bits.

    & = Returns '1' if both bits are '1'; else it returns '0'.
    | = Returns '1' if any of the bit is '1'; else it returns '0'.
    ~ = Returns one's complement of a number. i.e, each bit will be flipped. Don't forget to use the sign bit at the calculation.
    ^ = Returns '1' if ONE of the bits is '1'; else it returns '0'.

    >> = Shifts the bits of a binary number towards the right. As a consequence, it divides the number by 2^n. Note that 'n' represents the magnitude of the shift.
    << = Shifts the bits of a binary number towards the left. As a consequence, it multiplies the number by 2^n. Note that 'n' represents the magnitude of the shift.

    a = 10 -> 1010
    b = 5 -> 0101
    c = 9 -> 1001
    d = 12 -> 01100
    e = -12 -> 10100
    f = 3 -> 0011
    g = -3 -> 101
                                                                                                 
      1010     1010    a = '0'1010 (10)      1010 (10)   d = '0'1100 (12)                       e = '1'0100 (-12)
    & 0101   | 0101   ~a = '1'0101 (-11)   ^ 1001 (9)    d >> 1 = '0'0110 (6)                   e >> 1 = '1'1010 (-6)
    = 0000   = 1111       = -11            = 0011 (3)    '0'1100(12) / 2^1 (2) = '0'0110(6)     10100(-12) / 2^1 (2) = '1'1010(-6)

    f = 011 (3)                 g = 101 (-3)
    f << 1 = 0110 (6)           g << 1 = 1010 (-6)
    011(3) * 2^1 (2) = 0110(6)  101(3) * 2^1 (2) = 1010(-6)
"""


def square(number):
    if not 1 <= number <= 64:
        raise ValueError("square must be between 1 and 64")

    return 1 * (2 ** (number - 1))


TOTAL_GRAINS = 2**64 - 1
BIT_GRAINS = (1 << 64) - 1


def total():
    return TOTAL_GRAINS


def bit_total():
    return BIT_GRAINS
