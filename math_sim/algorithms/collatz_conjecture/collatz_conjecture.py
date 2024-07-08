"""
This module implements the Collatz Conjecture algorithm.
"""

from ...resource_monitor import ResourceMonitor

def collatz_conjecture(n, max_steps=1000):
    """
    Generate the Collatz Conjecture sequence for a given number.

    :param n: Starting number for the sequence
    :param max_steps: Maximum number of steps to calculate
    :return: Tuple of (sequence, ResourceMonitor instance)
    """
    monitor = ResourceMonitor()
    sequence = [n]
    for _ in range(max_steps):
        monitor.check_resources()
        if n == 1:
            break
        n = 3 * n + 1 if n % 2 else n // 2
        sequence.append(n)
    return sequence, monitor

if __name__ == "__main__":
    start_number = 27
    result, monitor = collatz_conjecture(start_number)
    print(f"Collatz sequence starting from {start_number}: {result}")
    print(f"Sequence length: {len(result)}")
    print(f"Final number in sequence: {result[-1]}")
    print(f"Max memory usage: {max(monitor.memory_usage):.2f}%")
    print(f"Max CPU usage: {max(monitor.cpu_usage):.2f}%")