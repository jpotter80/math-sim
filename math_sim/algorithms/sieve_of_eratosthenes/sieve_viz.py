"""
This module provides visualization tools for the Sieve of Eratosthenes algorithm.
"""

import matplotlib.pyplot as plt
import numpy as np
from .sieve_of_eratosthenes import sieve_of_eratosthenes

def plot_prime_spiral(limit):
    """
    Generate and plot a prime spiral (Ulam spiral) up to the given limit.

    :param limit: Upper limit for prime number generation
    """
    primes, _ = sieve_of_eratosthenes(limit)
    primes_set = set(primes)

    # Create a spiral of numbers
    size = int(np.ceil(np.sqrt(limit)))
    spiral = np.zeros((size, size), dtype=int)
    dx, dy = 1, 0
    x, y = 0, 0
    for i in range(1, limit + 1):
        spiral[x, y] = i
        nx, ny = x + dx, y + dy
        if 0 <= nx < size and 0 <= ny < size and spiral[nx, ny] == 0:
            x, y = nx, ny
        else:
            dx, dy = -dy, dx
            x, y = x + dx, y + dy

    # Plot the spiral
    plt.figure(figsize=(10, 10))
    for i in range(size):
        for j in range(size):
            if spiral[i, j] in primes_set:
                plt.plot(j, i, 'ro', markersize=2)
    
    plt.title(f"Prime Spiral (Ulam Spiral) up to {limit}")
    plt.axis('off')
    plt.savefig(f"prime_spiral_{limit}.png", dpi=300, bbox_inches='tight')
    plt.close()

def plot_prime_distribution(limit):
    """
    Plot the distribution of prime numbers up to the given limit.

    :param limit: Upper limit for prime number generation
    """
    primes, _ = sieve_of_eratosthenes(limit)
    
    plt.figure(figsize=(12, 6))
    plt.plot(range(2, limit + 1), [1 if i in primes else 0 for i in range(2, limit + 1)], 'b.', markersize=2)
    plt.title(f"Distribution of Primes up to {limit}")
    plt.xlabel("Number")
    plt.ylabel("Is Prime")
    plt.savefig(f"prime_distribution_{limit}.png", dpi=300, bbox_inches='tight')
    plt.close()

if __name__ == "__main__":
    limit = 1000
    plot_prime_spiral(limit)
    plot_prime_distribution(limit)
    print(f"Plots saved as 'prime_spiral_{limit}.png' and 'prime_distribution_{limit}.png'")