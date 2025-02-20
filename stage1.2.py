import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

def logistic_growth(t, K, r, N0, lag_length, exp_length):
    """
    Simulates logistic population growth with a customizable lag and exponential phase.
    
    Parameters:
        t (int): Time points
        K (int): Carrying capacity
        r (float): Growth rate
        N0 (int): Initial population size
        lag_length (int): Duration of the lag phase
        exp_length (int): Duration of the exponential phase
        
    Returns:
        np.array: Population size at each time point
    """
    population = np.zeros(t)
    
    # Lag phase (no growth)
    population[:lag_length] = N0
    
    # Exponential phase
    for i in range(lag_length, exp_length):
        population[i] = population[i-1] * np.exp(r)

    # Logistic phase (growth slows down)
    for i in range(exp_length, t):
        population[i] = population[i-1] + r * population[i-1] * (1 - population[i-1] / K)

    return population

# Example usage
time_points = 100
K = 1000  # Carrying capacity
r = 0.1   # Growth rate
N0 = 10   # Initial population
lag_length = np.random.randint(5, 15)  # Randomize lag phase
exp_length = np.random.randint(15, 30)  # Randomize exponential phase

population_curve = logistic_growth(time_points, K, r, N0, lag_length, exp_length)

plt.plot(range(time_points), population_curve)
plt.xlabel("Time")
plt.ylabel("Population Size")
plt.title("Simulated Logistic Growth")
plt.show()
