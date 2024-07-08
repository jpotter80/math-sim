# Math-Sim Project Structure

```
math-sim/
├── math_sim/
│   ├── __init__.py
│   ├── main.py
│   ├── resource_monitor.py
│   ├── concurrent_math_sim.py
│   └── algorithms/
│       └── aliquot_sequence/
│           ├── __init__.py
│           ├── aliquot_sequence.py
│           ├── aliquot_sequence_viz.py
│           └── README.md
├── tests/
│   ├── __init__.py
│   ├── test_resource_monitor.py
│   └── test_concurrent_math_sim.py
├── README.md
├── project.md
├── pyproject.toml
└── .gitignore
```

## File Descriptions

- `math_sim/main.py`: The main entry point for the application, providing a command-line interface to run various simulations.
- `math_sim/resource_monitor.py`: Contains the ResourceMonitor class.
- `math_sim/concurrent_math_sim.py`: Implements concurrent versions of the mathematical simulations.
- `math_sim/algorithms/aliquot_sequence/aliquot_sequence.py`: Contains the implementation of the aliquot sequence algorithm.
- `math_sim/algorithms/aliquot_sequence/aliquot_sequence_viz.py`: Visualization tools for the aliquot sequence.
- `math_sim/algorithms/aliquot_sequence/README.md`: Documentation for the aliquot sequence algorithm.
- `tests/test_resource_monitor.py`: Contains tests for the ResourceMonitor.
- `tests/test_concurrent_math_sim.py`: Contains tests for the concurrent mathematical simulations.
- `README.md`: Project overview and usage instructions.
- `project.md`: Detailed project plan and documentation.
- `pyproject.toml`: Poetry configuration file for managing dependencies.
- `.gitignore`: Specifies intentionally untracked files to ignore.
