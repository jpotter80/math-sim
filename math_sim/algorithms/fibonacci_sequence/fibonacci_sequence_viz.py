"""
This module provides visualization tools for the Fibonacci Sequence algorithm.
"""

import matplotlib.pyplot as plt
from .fibonacci_sequence import fibonacci_sequence

def plot_fibonacci_sequence(num_terms):
    """
    Generate and plot the Fibonacci Sequence.

    :param num_terms: Number of terms to generate and plot
    """
    sequence, monitor = fibonacci_sequence(num_terms)
    
    plt.figure(figsize=(12, 6))
    plt.plot(range(len(sequence)), sequence, marker='o')
    plt.title(f"Fibonacci Sequence ({num_terms} terms)")
    plt.xlabel("Term")
    plt.ylabel("Value")
    plt.yscale('log')  # Use log scale for y-axis due to exponential growth
    plt.grid(True)
    plt.savefig(f"fibonacci_sequence_{num_terms}.png")
    plt.close()

    # Plot resource usage
    fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(12, 10))
    
    ax1.plot(monitor.time_points, monitor.memory_usage)
    ax1.set_title("Memory Usage During Fibonacci Sequence Calculation")
    ax1.set_xlabel("Time")
    ax1.set_ylabel("Memory Usage (%)")
    ax1.grid(True)
    
    ax2.plot(monitor.time_points, monitor.cpu_usage)
    ax2.set_title("CPU Usage During Fibonacci Sequence Calculation")
    ax2.set_xlabel("Time")
    ax2.set_ylabel("CPU Usage (%)")
    ax2.grid(True)
    
    plt.tight_layout()
    plt.savefig(f"fibonacci_resource_usage_{num_terms}.png")
    plt.close()

if __name__ == "__main__":
    num_terms = 20
    plot_fibonacci_sequence(num_terms)
    print(f"Plots saved as 'fibonacci_sequence_{num_terms}.png' and 'fibonacci_resource_usage_{num_terms}.png'")