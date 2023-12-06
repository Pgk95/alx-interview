#!/usr/bin/python3
"""prime game"""


def isWinner(x, nums):
    """winner function"""
    def is_prime(num):
        """prime function"""
        if num < 2:
            return False
        for i in range(2, int(num**0.5) + 1):
            if num % i == 0:
                return False
        return True

    def get_primes(n):
        """prime function"""
        primes = []
        for i in range(2, n + 1):
            if is_prime(i):
                primes.append(i)
        return primes

    def game_winner(n):
        """winner function"""
        primes = get_primes(n)
        xor_sum = 0
        for prime in primes:
            xor_sum ^= prime

        return "Maria" if xor_sum == 0 else "Ben"

    winners = [game_winner(n) for n in nums]

    maria_wins = winners.count("Maria")
    ben_wins = winners.count("Ben")

    if maria_wins > ben_wins:
        return "Maria"
    elif ben_wins > maria_wins:
        return "Ben"
    else:
        return None
