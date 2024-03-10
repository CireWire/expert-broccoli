#!/usr/bin/env python3

import numpy as np
import matplotlib.pyplot as plt

# Function to calculate optimal price based on the formula
def calculate_optimal_price(marginal_cost, elasticity_of_demand):
    return max(0, marginal_cost / (1 - abs(elasticity_of_demand)))

# Function to run Monte Carlo simulation
def monte_carlo_simulation(num_simulations, marginal_cost_mean, marginal_cost_std, elasticity_mean, elasticity_std):
    optimal_prices = []

    for i in range(num_simulations):
        marginal_cost = np.random.normal(marginal_cost_mean, marginal_cost_std)
        elasticity_of_demand = np.random.normal(elasticity_mean, elasticity_std)
        
        # Calculate optimal price
        optimal_price = calculate_optimal_price(marginal_cost, elasticity_of_demand)
        optimal_prices.append(optimal_price)

    return optimal_prices

# Set parameters for the simulation
num_simulations = 1000
marginal_cost_mean = 10
marginal_cost_std = .5
elasticity_mean = -0.5
elasticity_std = .1

# Run the simulation
optimal_prices = monte_carlo_simulation(num_simulations, marginal_cost_mean, marginal_cost_std, elasticity_mean, elasticity_std)

# Plot the results
plt.hist(optimal_prices, bins=30, edgecolor='black')
plt.title('Optimal Prices')
plt.xlabel('Price')

plt.show()

# Print the results
print('Mean optimal price:', np.mean(optimal_prices))
print('Standard deviation of optimal price:', np.std(optimal_prices))
print('Minimum optimal price:', np.min(optimal_prices))
print('Maximum optimal price:', np.max(optimal_prices))
