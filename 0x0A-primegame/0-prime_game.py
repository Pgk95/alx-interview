#!/usr/bin/python3
"""prime game"""


def get_prime(x, nums):
    """returns a list of prime numbers"""
    prime = []
    for i in range(x):
        if nums[i] > 1:
            for j in range(2, nums[i]):
                if (nums[i] % j) == 0:
                    break
            else:
                prime.append(nums[i])
    return prime


def isWinner(x, nums):
    """returns the name of the player that won the most rounds"""
    if not nums or x < 1:
        return None
    Maria = 0
    Ben = 0
    prime = get_prime(x, nums)
    for i in range(x):
        if i % 2 == 0:
            if nums[i] in prime:
                Maria += 1
        else:
            if nums[i] in prime:
                Ben += 1
    if Maria > Ben:
        return "Ben"
    elif Maria < Ben:
        return "Maria"
    else:
        return None
