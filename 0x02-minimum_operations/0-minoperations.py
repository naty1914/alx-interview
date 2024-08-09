#!/usr/bin/python3
"""A module that provides a function that calculates the fewest number of
operations needed to result in exactly n H characters in the file.
"""


def minOperations(n):
    """ it's a function that calculates the fewest number of operations"""
    number_of_operations = 0
    factor_number = 2
    if n <= 1:
        return 0

    while n > 1:
        while n % factor_number == 0:
            number_of_operations += factor_number
            n //= factor_number
        factor_number += 1

    return number_of_operations
