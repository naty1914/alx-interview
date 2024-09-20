#!/usr/bin/python3
"""A module that defines a function for making change"""


def makeChange(coins, total):
    """It Return the fewest number of coins needed to meet
    a given amount total.
    """
    if total <= 0:
        return 0

    rem_amount = total
    coins_needed = 0
    coins_index = 0
    coins.sort(reverse=True)
    num = len(coins)
    while rem_amount > 0:
        if coins_index >= num:
            return -1
        if rem_amount - coins[coins_index] >= 0:
            rem_amount -= coins[coins_index]
            coins_needed += 1
        else:
            coins_index += 1
    return coins_needed
