# Math-Sim: Mathematical Simulations with Concurrent Processing

Math-Sim is a Python project that combines mathematical simulations, particularly in number theory, with resource monitoring capabilities. It provides tools to run algorithms while tracking and visualizing memory and CPU usage, with a focus on efficiency, safety, and robustness.

## Features

- Implementation of number theory algorithms:
  - Aliquot sequences
  - Sieve of Eratosthenes for prime number generation
  - Integer factorization
- Real-time resource monitoring (memory and CPU usage)
- Concurrent execution of algorithms for improved performance
- Visualization of resource usage over time
- Comprehensive test suite with timeout mechanisms

## New: Concurrency Support

We're excited to announce that Math-Sim now supports concurrent execution of algorithms. This new feature allows for:

- Parallel processing of multiple algorithms
- Improved performance on multi-core systems
- Enhanced responsiveness in the upcoming GUI
- More efficient resource utilization

## Installation

Ensure you have Python 3.12+ and Poetry installed on your system. Then follow these steps:

1. Clone the repository:
   ```
   git clone https://github.com/yourusername/math-sim.git
   cd math-sim
   ```

2. Install dependencies using Poetry:
   ```
   poetry install
   ```

## Usage

To run a concurrent simulation:

```python
from math_sim.concurrent_math_sim import run_concurrent_simulations

results = run_concurrent_simulations(aliquot_input=220, sieve_input=100, factorize_input=84)
print(results)
```

## Running Tests

To run the test suite:

```
poetry run pytest
```

## Contributing

Contributions to Math-Sim are welcome! Please feel free to submit a Pull Request. When contributing, please:

- Follow the PEP 8 style guide
- Write unit tests for new features
- Document any concurrency patterns used
- Ensure all tests pass before submitting a PR

## Future Plans

- Implement a GUI for easy interaction with simulations
- Develop more advanced parallel algorithms
- Create a web interface for running simulations
- Explore integration with distributed computing frameworks

## License

This project is licensed under the MIT License - see the LICENSE file for details.
