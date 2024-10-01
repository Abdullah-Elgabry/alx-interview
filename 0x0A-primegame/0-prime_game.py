#!/usr/bin/python3
"""
A game where Maria and Ben compete in prime number selection.
"""


def determine_winner(rounds, number_list):
    """Determine the winner between Maria and Ben based on prime numbers.
    
    Args:
        rounds (int): The number of rounds played.
        number_list (list): A list containing the numbers for each round.

    Returns:
        str: The name of the winner, or None if there is no clear winner.
    """
    if rounds <= 0 or number_list is None:
        return None
    if rounds != len(number_list):
        return None

    ben_score = 0
    maria_score = 0

    # Create an array to mark non-prime numbers
    sieve = [1] * (max(number_list) + 1)
    sieve[0], sieve[1] = 0, 0  # 0 and 1 are not prime numbers
    for current in range(2, len(sieve)):
        eliminate_multiples(sieve, current)

    # Calculate scores based on the prime counts for each number
    for number in number_list:
        if sum(sieve[:number + 1]) % 2 == 0:
            ben_score += 1
        else:
            maria_score += 1
            
    if ben_score > maria_score:
        return "Ben"
    elif maria_score > ben_score:
        return "Maria"
    return None


def eliminate_multiples(array, prime):
    """Mark the multiples of a prime number in the list as non-prime.
    
    Args:
        array (list): The list where multiples will be marked.
        prime (int): The prime number whose multiples will be marked.
    """
    for multiple in range(2, len(array)):
        try:
            array[multiple * prime] = 0  # Marking multiples as non-prime
        except IndexError:
            break
