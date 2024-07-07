"""
This module implements the Aliquot Sequence algorithm.
"""

from math_sim.resource_monitor import ResourceMonitor

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

if __name__ == "__main__":
    start_number = 220  # You can change this to test different starting numbers
    result, monitor = aliquot_sequence(start_number)
    print(f"Aliquot sequence starting from {start_number}: {result}")
    print(f"Sequence length: {len(result)}")
    print(f"Final number in sequence: {result[-1]}")
    print(f"Max memory usage: {max(monitor.memory_usage):.2f}%")
    print(f"Max CPU usage: {max(monitor.cpu_usage):.2f}%")