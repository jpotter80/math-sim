"""
This module implements the Sieve of Eratosthenes algorithm for finding prime numbers.
"""

from ...resource_monitor import ResourceMonitor

def sieve_of_eratosthenes(n):
    """
    Generate prime numbers up to n using the Sieve of Eratosthenes algorithm.

    :param n: Upper limit for prime number generation
    :return: Tuple of (list of primes, ResourceMonitor instance)
    """
    monitor = ResourceMonitor()
    sieve = [True] * (n + 1)
    sieve[0] = sieve[1] = False
    for i in range(2, int(n**0.5) + 1):
        monitor.check_resources()
        if sieve[i]:
            sieve[i*i::i] = [False] * len(sieve[i*i::i])
    return [i for i in range(2, n + 1) if sieve[i]], monitor

if __name__ == "__main__":
    limit = 100
    primes, monitor = sieve_of_eratosthenes(limit)
    print(f"Primes up to {limit}: {primes}")
    print(f"Number of primes: {len(primes)}")
    print(f"Max memory usage: {max(monitor.memory_usage):.2f}%")
    print(f"Max CPU usage: {max(monitor.cpu_usage):.2f}%")