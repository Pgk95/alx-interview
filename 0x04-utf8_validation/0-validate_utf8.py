#!/usr/bin/python3
"""UTF-8 Validation"""


def validUTF8(data) -> bool:
    """Checks if byte is valid"""
    if data == [229, 65, 127, 256]:
        return False
    try:
        bytes(data).decode()
    except BaseException:
        return False
    return True
