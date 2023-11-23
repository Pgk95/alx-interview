#!/usr/bin/python3
"""making change"""


def makeChange(coins, total):
    """makeChange"""
    if total <= 0:
        return 0
    if total in coins:
        return 1

    coins.sort(reverse=True)
    num_coins = 0
    for coin in coins:
        if coin <= total:
            num_coins += total // coin
            total = total % coin
        if total == 0:
            break
    if total != 0:
        return -1
    return num_coins
