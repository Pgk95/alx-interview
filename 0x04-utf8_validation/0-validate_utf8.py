#!/usr/bin/python3
"""UTF-8 Validation"""


def validUTF8(data) -> bool:
    """Checks if byte is valid"""
    try:
        bytes(data).decode('utf-8')
        return True
    except BaseException:
        return False
    return True
