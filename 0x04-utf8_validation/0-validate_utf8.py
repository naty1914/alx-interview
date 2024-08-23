#!/usr/bin/python3
"""A module that provides a function that determines if a given data
set represents a valid UTF-8 encoding"""


def validUTF8(data):
    """ It determines if a given data set represents a valid UTF-8 encoding"""
    number_of_bytes = 0
    most_significant = 1 << 7
    second_most_significant = 1 << 6
    for n in data:
        byte = 1 << 7
        if number_of_bytes == 0:
            while byte & n:
                number_of_bytes += 1
                byte = byte >> 1
            if number_of_bytes == 0:
                continue
            if number_of_bytes == 1 or number_of_bytes > 4:
                return False
        else:
            if not (n & most_significant and not (
                    n & second_most_significant)):
                return False
        number_of_bytes -= 1
    return number_of_bytes == 0
