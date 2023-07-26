#!/usr/bin/python3
"""Module to Solve the Prime Game"""


def sieve_of_eratosthenes(n):
    """ The Sieve of Eratosthenes Algorithm"""
    primes = [True] * (n + 1)
    primes[0], primes[1] = False, False

    for p in range(2, int(n ** 0.5) + 1):
        if primes[p]:
            for i in range(p * p, n + 1, p):
                primes[i] = False

    return [num for num, is_prime in enumerate(primes) if is_prime]


def play_game(n):
    """Simulating the Game Play between Maria and Ben"""
    primes = sieve_of_eratosthenes(n)
    num_set = set(range(1, n + 1))

    while num_set:
        for prime in primes:
            if prime in num_set:
                num_set.difference_update(range(prime, n + 1, prime))
                # Check if any numbers left after the move
                if not num_set:
                    return "Maria"
                break
        else:
            # If no prime number is found, Ben wins
            return "Ben"

    # Elif Loop exits without a winner.
    return "Ben"


def isWinner(x, nums):
    """Keeping Track of Wins to Determine Winner"""
    maria_wins = ben_wins = 0

    for n in nums:
        winner = play_game(n)
        if winner == "Maria":
            maria_wins += 1
        elif winner == "Ben":
            ben_wins += 1

    if maria_wins == ben_wins:
        return None
    else:
        return "Maria" if maria_wins > ben_wins else "Ben"
