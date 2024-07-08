# Collatz Conjecture

## Overview

The Collatz conjecture is one of the most famous unsolved problems in mathematics. The conjecture asks whether repeating two simple arithmetic operations will eventually transform every positive integer into 1.

Given a number n:
- If n is even, divide it by 2
- If n is odd, multiply it by 3 and add 1

The conjecture is that for all positive integers, this sequence will eventually reach 1.

## Implementation

The Collatz conjecture algorithm is implemented in `collatz_conjecture.py`. It uses the `ResourceMonitor` class to track memory and CPU usage during the calculation.

Key features:
- Generates the Collatz sequence for a given starting number
- Limits the sequence to a maximum number of steps to prevent infinite loops
- Tracks resource usage throughout the calculation

## Visualization

The `collatz_conjecture_viz.py` file provides tools to visualize both the Collatz sequence and the resource usage during its calculation.

It generates two plots:
1. The Collatz sequence values (using a logarithmic scale for the y-axis)
2. Memory and CPU usage during the calculation

## Usage

To generate and visualize a Collatz sequence:

1. Navigate to the `math_sim` directory
2. Run the following command:
   ```
   python -m math_sim.main --collatz 27
   ```
   Replace 27 with any positive integer you want to start the sequence from.

## Interpretation

- The sequence will always reach 1 (according to the conjecture, though this hasn't been proven for all numbers)
- Some numbers may take many more steps than others before reaching 1
- The sequence often includes numbers much larger than the starting number

## Further Exploration

Try different starting numbers to observe various behaviors:
- Small numbers like 6, 7, 8
- Larger numbers like 27, 31, 41
- Powers of 2 (which resolve in very few steps)
- Very large numbers (but be aware that these may take a long time to compute)