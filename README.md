# Math-Sim

Math-Sim is a Python-based project for mathematical simulations and visualizations. It provides implementations and visualizations for various mathematical concepts and algorithms.

## Features

- Aliquot Sequence generation and visualization
- Collatz Conjecture simulation and analysis
- Fibonacci Sequence generation and Golden Ratio visualization
- Sieve of Eratosthenes for prime number generation
- Prime number distribution and Ulam spiral visualizations
- Resource monitoring for performance analysis
- Parallel processing capabilities for improved efficiency

## Installation

1. Clone the repository:
   ```
   git clone https://github.com/jpotter80/math-sim.git
   cd math-sim
   ```

2. Create a virtual environment (optional but recommended):
   ```
   python -m venv venv
   source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
   ```

3. Install the required packages:
   ```
   pip install -r requirements.txt
   ```

## Usage

Run the main script with various options to execute different simulations:

```
python -m math_sim.main [OPTIONS]
```

Available options:
- `--demo`: Run a demonstration of all operations
- `--aliquot N`: Generate and visualize Aliquot sequence starting from N
- `--collatz N`: Generate and visualize Collatz sequence starting from N
- `--fibonacci N`: Generate and visualize Fibonacci sequence with N terms
- `--sieve N`: Generate primes and visualize distribution up to N
- `--factorize N`: Factorize the number N
- `--parallel-aliquot START COUNT`: Generate multiple Aliquot sequences in parallel
- `--parallel-factorize N [N ...]`: Factorize multiple numbers in parallel

Example:
```
python -m math_sim.main --collatz 27
```

## Development

To contribute to the project:

1. Fork the repository
2. Create a new branch for your feature
3. Implement your changes
4. Write or update tests as necessary
5. Submit a pull request

Please refer to the CONTRIBUTING.md file for more detailed guidelines.

## Testing

Run the test suite using pytest:

```
pytest
```

## License

This project is licensed under the MIT License. See the LICENSE file for details.

## Contact

For questions or suggestions, please open an issue on the GitHub repository.