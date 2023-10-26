#!/usr/bin/python3
"""UTF-8 Validation"""


def validUTF8(byte) -> bool:
    """Checks if byte is valid"""

    if byte[0] & 0b10000000 == 0b00000000:
        return True

    if byte[0] & 0b11100000 == 0b11000000:
        if byte[1] & 0b11000000 == 0b10000000:
            return True

    if byte[0] & 0b11100000 == 0b11100000:
        return False

    return True
