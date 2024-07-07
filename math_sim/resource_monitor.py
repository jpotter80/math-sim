"""
This module provides functionality for monitoring resource usage during mathematical simulations.
It includes a ResourceMonitor class and various number theory algorithms.
"""

import os
import time
import psutil
import matplotlib.pyplot as plt

class ResourceMonitor:
    """
    A class for monitoring memory and CPU usage during program execution.
    """

    def __init__(self, max_memory_percent=90, max_cpu_percent=95):
        """
        Initialize the ResourceMonitor.

        :param max_memory_percent: Maximum allowed memory usage percentage
        :param max_cpu_percent: Maximum allowed CPU usage percentage
        """
        self.max_memory_percent = max_memory_percent
        self.max_cpu_percent = max_cpu_percent
        self.memory_usage = []
        self.cpu_usage = []
        self.time_points = []

    def check_resources(self):
        """
        Check current memory and CPU usage, and record the values.

        :raises MemoryError: If memory usage exceeds the maximum allowed
        :raises RuntimeError: If CPU usage exceeds the maximum allowed
        :return: Tuple of current memory and CPU usage percentages
        """
        process = psutil.Process(os.getpid())
        memory_percent = process.memory_percent()
        cpu_percent = psutil.cpu_percent(interval=0.1)
        self.memory_usage.append(memory_percent)
        self.cpu_usage.append(cpu_percent)
        self.time_points.append(time.time())
        if memory_percent > self.max_memory_percent:
            raise MemoryError(f"Memory usage exceeded {self.max_memory_percent}%")
        if cpu_percent > self.max_cpu_percent:
            raise RuntimeError(f"CPU usage exceeded {self.max_cpu_percent}%")
        return memory_percent, cpu_percent

def aliquot_sequence(n, max_steps=1000):
    """
    Generate the aliquot sequence for a given number.

    :param n: Starting number for the sequence
    :param max_steps: Maximum number of steps to calculate
    :return: Tuple of (sequence, ResourceMonitor instance)
    """
    monitor = ResourceMonitor()
    sequence = [n]
    for _ in range(max_steps):
        monitor.check_resources()
        next_num = sum(i for i in range(1, sequence[-1]) if sequence[-1] % i == 0)
        if next_num in sequence:
            break
        sequence.append(next_num)
    return sequence, monitor

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
            for j in range(i*i, n + 1, i):
                sieve[j] = False
    return [i for i in range(2, n + 1) if sieve[i]], monitor

def factorize(n):
    """
    Factorize a number into its prime factors.

    :param n: Number to factorize
    :return: Tuple of (list of prime factors, ResourceMonitor instance)
    """
    monitor = ResourceMonitor()
    factors = []
    d = 2
    while n > 1:
        monitor.check_resources()
        while n % d == 0:
            factors.append(d)
            n //= d
        d += 1
        if d * d > n:
            if n > 1:
                factors.append(n)
            break
    return factors, monitor

def plot_resource_usage(monitor):
    """
    Plot the memory and CPU usage over time.

    :param monitor: ResourceMonitor instance containing usage data
    """
    fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(10, 10))
    
    ax1.plot(monitor.time_points, monitor.memory_usage)
    ax1.set_xlabel('Time')
    ax1.set_ylabel('Memory Usage (%)')
    ax1.set_title('Memory Usage Over Time')
    
    ax2.plot(monitor.time_points, monitor.cpu_usage)
    ax2.set_xlabel('Time')
    ax2.set_ylabel('CPU Usage (%)')
    ax2.set_title('CPU Usage Over Time')
    
    plt.tight_layout()
    plt.savefig('resource_usage_plot.png')
    plt.close()

if __name__ == "__main__":
    try:
        print("Running Aliquot Sequence")
        result, monitor = aliquot_sequence(220)
        print(f"Aliquot sequence: {result}")
        plot_resource_usage(monitor)
        
        print("\nRunning Sieve of Eratosthenes")
        primes, monitor = sieve_of_eratosthenes(1000)
        print(f"Primes up to 1000: {primes}")
        plot_resource_usage(monitor)
        
        print("\nRunning Factorization")
        number_to_factorize = 1234567890
        factors, monitor = factorize(number_to_factorize)
        print(f"Factors of {number_to_factorize}: {factors}")
        plot_resource_usage(monitor)
        
        print("\nPlots saved as 'resource_usage_plot.png'")
    except (MemoryError, RuntimeError) as e:
        print(f"Simulation stopped: {e}")
        plot_resource_usage(monitor)