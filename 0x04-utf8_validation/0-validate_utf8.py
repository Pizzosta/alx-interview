#!/usr/bin/python3
""" UTF-8 Validation """


def validUTF8(data):
    """
    Method that validates the given data if its utf-8

    Args:
      data - list of integers to be validated
    """
    num_bytes_to_check = 0

    for num in data:
        if num_bytes_to_check == 0:
            if (num >> 7) == 0b0:
                continue
            elif (num >> 5) == 0b110:
                num_bytes_to_check = 1
            elif (num >> 4) == 0b1110:
                num_bytes_to_check = 2
            elif (num >> 3) == 0b11110:
                num_bytes_to_check = 3
            else:
                return False
        else:
            if (num >> 6) == 0b10:
                num_bytes_to_check -= 1
            else:
                return False

    return num_bytes_to_check == 0
