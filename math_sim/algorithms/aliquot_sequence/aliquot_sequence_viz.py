"""
This module provides visualization tools for the Aliquot Sequence algorithm.
"""

import matplotlib.pyplot as plt
from math_sim.algorithms.aliquot_sequence.aliquot_sequence import aliquot_sequence

def plot_aliquot_sequence(start_number, max_steps=1000):
    """
    Generate and plot the Aliquot Sequence.

    :param start_number: The number to start the sequence from
    :param max_steps: Maximum number of steps to calculate
    """
    sequence, monitor = aliquot_sequence(start_number, max_steps)
    
    # Plot the sequence
    plt.figure(figsize=(12, 6))
    plt.plot(range(len(sequence)), sequence, marker='o')
    plt.title(f"Aliquot Sequence starting from {start_number}")
    plt.xlabel("Step")
    plt.ylabel("Value")
    plt.yscale('log')  # Use log scale for y-axis due to potentially large numbers
    plt.grid(True)
    plt.savefig(f"aliquot_sequence_{start_number}.png")
    plt.close()

    # Plot resource usage
    fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(12, 10))
    
    ax1.plot(monitor.time_points, monitor.memory_usage)
    ax1.set_title("Memory Usage During Aliquot Sequence Calculation")
    ax1.set_xlabel("Time")
    ax1.set_ylabel("Memory Usage (%)")
    ax1.grid(True)
    
    ax2.plot(monitor.time_points, monitor.cpu_usage)
    ax2.set_title("CPU Usage During Aliquot Sequence Calculation")
    ax2.set_xlabel("Time")
    ax2.set_ylabel("CPU Usage (%)")
    ax2.grid(True)
    
    plt.tight_layout()
    plt.savefig(f"aliquot_sequence_resource_usage_{start_number}.png")
    plt.close()

if __name__ == "__main__":
    start_number = 220  # You can change this to visualize different starting numbers
    plot_aliquot_sequence(start_number)
    print(f"Plots saved as 'aliquot_sequence_{start_number}.png' and 'aliquot_sequence_resource_usage_{start_number}.png'")