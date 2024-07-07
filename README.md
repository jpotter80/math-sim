# Math-Sim: Mathematical Simulations with Resource Monitoring

Math-Sim is a Python project that combines mathematical simulations, particularly in number theory, with resource monitoring capabilities. It provides tools to run algorithms while tracking and visualizing memory usage.

## Features

- Implementation of number theory algorithms (currently featuring aliquot sequences)
- Real-time memory usage monitoring
- Visualization of memory usage over time
- Extensible architecture for adding more mathematical simulations

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

To run the aliquot sequence simulation:

```
poetry run python math_sim/resource_monitor.py
```

This will generate an aliquot sequence and save a plot of the memory usage as 'memory_usage_plot.png'.

## Running Tests

To run the test suite:

```
poetry run pytest
```

## Project Structure

- `math_sim/`: Main package directory
  - `resource_monitor.py`: Contains the ResourceMonitor class and aliquot sequence function
- `tests/`: Directory containing test files
- `pyproject.toml`: Poetry configuration and project metadata

## Contributing

Contributions to Math-Sim are welcome! Please feel free to submit a Pull Request.

## License

This project is licensed under the MIT License - see the LICENSE file for details.

## Acknowledgments

- Thanks to all contributors and users of this project
- Inspired by the fascinating world of number theory and the importance of resource management in computing
