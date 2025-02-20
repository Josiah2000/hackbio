def time_to_reach_80_percent_K(population_curve, K):
    threshold = 0.8 * K
    for t, pop in enumerate(population_curve):
        if pop >= threshold:
            return t
    return None  # If never reached

# Example usage
time_reached = time_to_reach_80_percent_K(population_curve, K)
print(f"Time to reach 80% of carrying capacity: {time_reached}")
