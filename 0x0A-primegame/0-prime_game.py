#!/usr/bin/python3
"""A module that defines a function for playing a game"""


def isWinner(x, nums):
    """It determine who the winner of each game is"""
    if x < 1 or not nums:
        return None
    winner_is_maria = 0
    winner_is_ben = 0
    num = max(nums)
    primes = [True for _ in range(1,  1 + num, 1)]
    primes[0] = False
    for i, is_prime in enumerate(primes, 1):
        if i == 1 or not is_prime:
            continue
        for j in range(i + i, num + 1, i):
            primes[j - 1] = False
    for _, num in zip(range(x), nums):
        count_primes = len(list(filter(lambda x: x, primes[0: num])))
        winner_is_ben += count_primes % 2 == 0
        winner_is_maria += count_primes % 2 == 1

    if winner_is_maria == winner_is_ben:
        return None
    return 'Maria' if winner_is_maria > winner_is_ben else 'Ben'
