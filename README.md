# Monte Carlo Simulation for Price Optimization

This Python script performs a Monte Carlo Simulation for price optimization using the provided formula. The simulation calculates optimal prices based on random variations in marginal cost and elasticity of demand.

## Overview

The Monte Carlo Simulation aims to estimate the optimal price for a product or service by considering variability in both marginal cost and elasticity of demand. The simulation generates random values for these parameters, calculates the optimal price using a specified formula, and aggregates the results.

## Files

- `monte_carlo_simulation.py`: The main Python script containing the Monte Carlo Simulation.
- `README.md`: This file providing information about the project.

## Prerequisites

- Python 3.x
- NumPy library (`pip install numpy`)
- Plot Library (`pip install matplotlib`')

## Usage

1. Ensure you have Python installed on your system.
2. Install the required libraries.
3. Adjust simulation parameters (mean, standard deviation, number of simulations) in `monte_carlo_simulation.py`.
4. Run the script using `python monte_carlo_simulation.py`.

## Simulation Parameters

- `num_simulations`: Number of iterations for the Monte Carlo Simulation.
- `marginal_cost_mean`: Mean value for marginal cost.
- `marginal_cost_std`: Standard deviation as a percentage of the mean for marginal cost.
- `elasticity_mean`: Mean value for elasticity of demand.
- `elasticity_std`: Standard deviation for elasticity of demand.

## Results

The script will print the following results:

- Mean Optimal Price
- Standard Deviation of Optimal Prices
- Minimum Optimal Price
- Maximum Optimal Price

Review these results to understand the distribution and variability of optimal prices.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Acknowledgments

- This script is a basic implementation for educational purposes. Adjustments may be needed for real-world scenarios.

Feel free to reach out with any questions or feedback!
