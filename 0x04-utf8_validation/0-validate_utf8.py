#!/usr/bin/python3
"""UTF Module"""


def validUTF8(data) -> bool:
    """Validates whether data is UTF8
    """
    def get_num_bytes(byte):
        if byte & 0b10000000 == 0:
            return 1
        elif byte & 0b11100000 == 0b11000000:
            return 2
        elif byte & 0b11110000 == 0b11100000:
            return 3
        elif byte & 0b11111000 == 0b11110000:
            return 4
        else:
            return -1  # Invalid byte sequence

    i = 0
    while i < len(data):
        num_bytes = get_num_bytes(data[i])
        if num_bytes == -1:
            return False

        for j in range(i + 1, i + num_bytes):
            if j >= len(data) or data[j] & 0b11000000 != 0b10000000:
                return False

        i += num_bytes

    return True
