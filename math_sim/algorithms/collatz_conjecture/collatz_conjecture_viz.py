"""
This module provides visualization tools for the Collatz Conjecture algorithm.
"""

import matplotlib.pyplot as plt
from .collatz_conjecture import collatz_conjecture

def plot_collatz_sequence(start_number, max_steps=1000):
    """
    Generate and plot the Collatz Conjecture sequence.

    :param start_number: The number to start the sequence from
    :param max_steps: Maximum number of steps to calculate
    """
    sequence, monitor = collatz_conjecture(start_number, max_steps)
    
    plt.figure(figsize=(12, 6))
    plt.plot(range(len(sequence)), sequence, marker='o')
    plt.title(f"Collatz Conjecture Sequence starting from {start_number}")
    plt.xlabel("Step")
    plt.ylabel("Value")
    plt.yscale('log')  # Use log scale for y-axis due to potentially large numbers
    plt.grid(True)
    plt.savefig(f"collatz_sequence_{start_number}.png")
    plt.close()

    # Plot resource usage
    fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(12, 10))
    
    ax1.plot(monitor.time_points, monitor.memory_usage)
    ax1.set_title("Memory Usage During Collatz Conjecture Calculation")
    ax1.set_xlabel("Time")
    ax1.set_ylabel("Memory Usage (%)")
    ax1.grid(True)
    
    ax2.plot(monitor.time_points, monitor.cpu_usage)
    ax2.set_title("CPU Usage During Collatz Conjecture Calculation")
    ax2.set_xlabel("Time")
    ax2.set_ylabel("CPU Usage (%)")
    ax2.grid(True)
    
    plt.tight_layout()
    plt.savefig(f"collatz_resource_usage_{start_number}.png")
    plt.close()

if __name__ == "__main__":
    start_number = 27
    plot_collatz_sequence(start_number)
    print(f"Plots saved as 'collatz_sequence_{start_number}.png' and 'collatz_resource_usage_{start_number}.png'")