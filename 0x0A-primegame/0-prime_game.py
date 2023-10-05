#!/usr/bin/python3
"""Prime Game"""


def isWinner(x, nums):
    """Determine the winner of a game based on a set of
    consecutive integers and the number of rounds played.
    """
    def sieve(limit):
        """ Generate a list of prime numbers up to a given limit"""
        primes = []
        sieve = [True] * (limit + 1)
        sieve[0] = sieve[1] = False
        p = 2
        while p * p <= limit:
            if sieve[p]:
                for i in range(p * p, limit + 1, p):
                    sieve[i] = False
            p += 1
        for p in range(2, limit + 1):
            if sieve[p]:
                primes.append(p)
        return primes

    def isPrime(n):
        """ Check if a number is prime."""
        if n == 1 or n == 0 or (n % 2 == 0 and n > 2):
            return False
        else:
            for i in range(3, int(n**(1/2))+1, 2):
                if n % i == 0:
                    return "Not prime"
            return True

    maria_wins = 0
    ben_wins = 0

    for n in nums:
        primes = sieve(n)
        prime_count = sum(1 for p in primes if isPrime(p))
        if prime_count % 2 == 0:
            ben_wins += 1
        else:
            maria_wins += 1

    if maria_wins > ben_wins:
        return "Maria"
    elif ben_wins > maria_wins:
        return "Ben"
    else:
        return None
