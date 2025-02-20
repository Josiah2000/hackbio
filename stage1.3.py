def generate_growth_data(num_curves=100, time_points=100):
    data = []
    
    for i in range(num_curves):
        K = np.random.randint(500, 1500)  # Random carrying capacity
        r = np.random.uniform(0.05, 0.2)  # Random growth rate
        N0 = np.random.randint(5, 50)  # Random initial population
        lag_length = np.random.randint(5, 15)
        exp_length = np.random.randint(15, 30)
        
        pop_curve = logistic_growth(time_points, K, r, N0, lag_length, exp_length)
        data.append(pop_curve)
    
    df = pd.DataFrame(data)
    return df

growth_df = generate_growth_data()
print(growth_df.head())  # Print first 5 rows
