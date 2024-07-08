# Fibonacci Sequence

## Overview

The Fibonacci sequence is a series of numbers where each number is the sum of the two preceding ones. It commonly starts from 0 and 1, and each subsequent number is the sum of the previous two.

The sequence Fn of Fibonacci numbers is defined by the recurrence relation:

Fn = Fn-1 + Fn-2

with seed values:

F0 = 0 and F1 = 1.

## Implementation

The Fibonacci sequence algorithm is implemented in `fibonacci_sequence.py`. It uses the `ResourceMonitor` class to track memory and CPU usage during the calculation.

Key features:
- Generates the Fibonacci sequence up to a specified number of terms
- Tracks resource usage throughout the calculation

## Visualization

The `fibonacci_sequence_viz.py` file provides tools to visualize both the Fibonacci sequence and the resource usage during its calculation.

It generates two plots:
1. The Fibonacci sequence values (using a logarithmic scale for the y-axis due to rapid growth)
2. Memory and CPU usage during the calculation

## Usage

To generate and visualize a Fibonacci sequence:

1. Navigate to the `math_sim` directory
2. Run the following command:
   ```
   python -m math_sim.main --fibonacci 20
   ```
   Replace 20 with any positive integer to specify the number of terms you want to generate.

## Interpretation

- The sequence grows exponentially
- The ratio of consecutive Fibonacci numbers converges to the golden ratio (approximately 1.618033988749895)
- Fibonacci numbers appear in many natural phenomena, from the arrangement of leaves on a stem to the spiral of shells

## Further Exploration

- Calculate the ratio of consecutive terms and observe how it approaches the golden ratio
- Investigate the relationship between Fibonacci numbers and Pascal's triangle
- Explore applications of Fibonacci numbers in nature, art, and architecture