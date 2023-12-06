#!/usr/bin/python3
"""Prime Game"""


def primes(n):
    """primes - Returns a list of prime numbers up to n."""
    prime = []
    filter = [True] * (n + 1)
    for p in range(2, n + 1):
        if (filter[p]):
            prime.append(p)
            for i in range(p, n + 1, p):
                filter[i] = False
    return prime


def isWinner(x, nums):
    """isWinner - Determines who the winner of the game is.    """
    if x is None or nums is None or x == 0 or nums == []:
        return None
    Maria = Ben = 0
    for i in range(x):
        prime = primes(nums[i])
        if len(prime) % 2 == 0:
            Ben += 1
        else:
            Maria += 1
    if Maria > Ben:
        return 'Maria'
    elif Ben > Maria:
        return 'Ben'
    return None
