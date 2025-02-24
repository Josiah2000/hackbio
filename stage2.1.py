import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from scipy.stats import ttest_ind

# 1️⃣ Load the dataset from the URL
url = "https://raw.githubusercontent.com/HackBio-Internship/2025_project_collection/refs/heads/main/Python/Dataset/mcgc.tsv"
df = pd.read_csv(url, sep="\t")

# Display the first few rows
print(df.head())

# 2️⃣ Function to calculate time to reach 80% of carrying capacity
def time_to_80_percent(df, strain_col, time_col, od_col):
    """
    Determines the time it takes for a strain to reach 80% of its maximum OD600 value.
    """
    max_od = df[od_col].max()
    threshold = 0.8 * max_od  # 80% of max OD600

    # Find the first time point where OD600 reaches or exceeds 80% of max
    reaching_time = df[df[od_col] >= threshold][time_col].min()
    return reaching_time

# 3️⃣ Extract time and OD600 data for each strain
time_column = "Time"  # Assuming the dataset has a column named "Time"
strains = df["Strain"].unique()

# Store results in a list
time_to_capacity = []

plt.figure(figsize=(10, 6))

for strain in strains:
    strain_data = df[df["Strain"] == strain]

    # Get WT (Wild Type) and MUT (Mutant) OD600 values
    wt_col = "WT"
    mut_col = "MUT"

    # Plot growth curves for WT and MUT
    plt.plot(strain_data[time_column], strain_data[wt_col], label=f"{strain} WT", linestyle='--')
    plt.plot(strain_data[time_column], strain_data[mut_col], label=f"{strain} MUT")

    # Calculate time to reach 80% of carrying capacity
    wt_time = time_to_80_percent(strain_data, "Strain", time_column, wt_col)
    mut_time = time_to_80_percent(strain_data, "Strain", time_column, mut_col)

    # Store results
    time_to_capacity.append({"Strain": strain, "Type": "WT", "Time": wt_time})
    time_to_capacity.append({"Strain": strain, "Type": "MUT", "Time": mut_time})

plt.xlabel("Time (hours)")
plt.ylabel("OD600")
plt.title("Growth Curves of WT and MUT Strains")
plt.legend()
plt.show()

# 4️⃣ Convert results into DataFrame
time_df = pd.DataFrame(time_to_capacity)

# 5️⃣ Scatter plot of time to carrying capacity for WT and MUT
plt.figure(figsize=(8, 6))
sns.scatterplot(x="Strain", y="Time", hue="Type", data=time_df)
plt.xlabel("Strain")
plt.ylabel("Time to 80% Carrying Capacity (hours)")
plt.title("Time to Carrying Capacity for WT and MUT Strains")
plt.show()

# 6️⃣ Box plot for time to carrying capacity
plt.figure(figsize=(8, 6))
sns.boxplot(x="Type", y="Time", data=time_df)
plt.xlabel("Strain Type")
plt.ylabel("Time to 80% Carrying Capacity (hours)")
plt.title("Comparison of WT and MUT Time to Carrying Capacity")
plt.show()

# 7️⃣ Statistical comparison (T-test)
wt_times = time_df[time_df["Type"] == "WT"]["Time"]
mut_times = time_df[time_df["Type"] == "MUT"]["Time"]

t_stat, p_value = ttest_ind(wt_times, mut_times)

# Print the results
print(f"T-statistic: {t_stat:.3f}, P-value: {p_value:.3f}")

# Interpretation
if p_value < 0.05:
    print("There is a significant difference between WT and MUT in time to carrying capacity.")
else:
    print("No significant difference between WT and MUT in time to carrying capacity.")
