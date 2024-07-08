"""
This module implements the Fibonacci Sequence algorithm.
"""

from ...resource_monitor import ResourceMonitor

def fibonacci_sequence(n):
    """
    Generate the Fibonacci Sequence up to the nth term.

    :param n: Number of terms to generate
    :return: Tuple of (sequence, ResourceMonitor instance)
    """
    monitor = ResourceMonitor()
    sequence = [0, 1]
    for _ in range(2, n):
        monitor.check_resources()
        sequence.append(sequence[-1] + sequence[-2])
    return sequence, monitor

if __name__ == "__main__":
    num_terms = 20
    result, monitor = fibonacci_sequence(num_terms)
    print(f"Fibonacci sequence up to {num_terms} terms: {result}")
    print(f"Sequence length: {len(result)}")
    print(f"Final number in sequence: {result[-1]}")
    print(f"Max memory usage: {max(monitor.memory_usage):.2f}%")
    print(f"Max CPU usage: {max(monitor.cpu_usage):.2f}%")