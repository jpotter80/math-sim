# Aliquot Sequence Algorithm

## Overview

An Aliquot sequence is a sequence of positive integers in which each term is the sum of the proper divisors of the previous term. Proper divisors of a number are all positive divisors other than the number itself.

For example, the Aliquot sequence starting with 10 is:
10, 8, 7, 1, 0

This is because:
- The proper divisors of 10 are 1, 2, 5, and their sum is 8
- The proper divisors of 8 are 1, 2, 4, and their sum is 7
- The only proper divisor of 7 is 1
- 1 has no proper divisors, so the next term is 0
- The sequence terminates at 0

## Implementation

The Aliquot sequence algorithm is implemented in `aliquot_sequence.py`. It uses the `ResourceMonitor` class to track memory and CPU usage during the calculation.

Key features:
- Generates the Aliquot sequence for a given starting number
- Limits the sequence to a maximum number of steps to prevent infinite loops
- Tracks resource usage throughout the calculation

## Visualization

The `aliquot_sequence_viz.py` file provides tools to visualize both the Aliquot sequence and the resource usage during its calculation.

It generates two plots:
1. The Aliquot sequence values (using a logarithmic scale for the y-axis)
2. Memory and CPU usage during the calculation

## Usage

To generate and visualize an Aliquot sequence:

1. Navigate to the `math_sim/algorithms/aliquot_sequence/` directory
2. Run the following command:
   ```
   python aliquot_sequence_viz.py
   ```
3. By default, this will generate plots for the Aliquot sequence starting from 220. You can modify the `start_number` in the `__main__` section of `aliquot_sequence_viz.py` to visualize different starting numbers.

## Interpretation

- If the sequence terminates at 0, the starting number is considered deficient.
- If the sequence reaches a perfect number (where the sum of proper divisors equals the number itself), it will cycle between that number and the sum of its proper divisors.
- Some sequences may enter a cycle of numbers (known as sociable numbers).
- Certain starting numbers may lead to very long sequences or sequences that grow very large, which is why we limit the number of steps.

## Further Exploration

Try different starting numbers to observe various behaviors:
- 220 and 284 form an amicable pair
- 6 is a perfect number
- 1184 and 2620 form another amicable pair
- 276 leads to a long sequence that eventually reaches very large numbers