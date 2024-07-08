"""
This module provides functionality for monitoring resource usage during mathematical simulations.
"""

import psutil
import time

class ResourceMonitor:
    def __init__(self, max_memory_percent=90, max_cpu_percent=95):
        self.max_memory_percent = max_memory_percent
        self.max_cpu_percent = max_cpu_percent
        self.memory_usage = []
        self.cpu_usage = []
        self.time_points = []

    def check_resources(self):
        memory_percent = psutil.virtual_memory().percent
        cpu_percent = psutil.cpu_percent(interval=0.1)
        
        self.memory_usage.append(memory_percent)
        self.cpu_usage.append(cpu_percent)
        self.time_points.append(time.time())
        
        if memory_percent > self.max_memory_percent:
            raise MemoryError(f"Memory usage exceeded {self.max_memory_percent}%")
        if cpu_percent > self.max_cpu_percent:
            raise RuntimeError(f"CPU usage exceeded {self.max_cpu_percent}%")
        
        return memory_percent, cpu_percent

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

if __name__ == "__main__":
    # Example usage
    number = 84
    factors, monitor = factorize(number)
    print(f"Factors of {number}: {factors}")
    print(f"Max memory usage: {max(monitor.memory_usage):.2f}%")
    print(f"Max CPU usage: {max(monitor.cpu_usage):.2f}%")