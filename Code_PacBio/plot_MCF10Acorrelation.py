import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import pearsonr

# Create the dataset
data = {
    "MCF10A": [26.45396024, 41.41253709, 3.129311986, 0.002246679, 0.02639848, 0.017911025,
               1.208963002, 0.213184886, 26.68630431, 0.349670643, 0.210626168, 0.066277034,
               0.017911025, 0.065340918, 0.004306135, 0.006053552, 0.000748893, 0.000436854,
               0.005928737, 0.009236348, 0.054357153, 0.022404384, 0.002870757, 0.012918405,
               0.020095297],
    "MCF10A_10x": [66.58668266, 22.91541692, 5.638872226, 0.719856029, 0.419916017, 0.179964007,
                   0.779844031, 0.539892022, 0.119976005, 0.779844031, 0.179964007, 0.059988002,
                   0.059988002, 0.179964007, 0.059988002, 0.119976005, 0.059988002, 0.059988002,
                   0.059988002, 0.119976005, 0.059988002, 0.059988002, 0.059988002, 0.119976005,
                   0.059988002]
}

# Create a DataFrame
df = pd.DataFrame(data)

# Calculate Pearson correlation
correlation, p_value = pearsonr(df["MCF10A"], df["MCF10A_10x"])

# Print the correlation coefficient and p-value
print(f"Pearson Correlation Coefficient: {correlation:.4f}")
print(f"P-value: {p_value:.4e}")

# Scatter plot to visualize the relationship
plt.figure(figsize=(8, 6))
plt.scatter(df["MCF10A"], df["MCF10A_10x"], alpha=0.7, color="blue", label="Data Points")
plt.title("Scatter Plot of MCF10A vs MCF10A_10x")
plt.xlabel("MCF10A")
plt.ylabel("MCF10A_10x")
plt.axline((0, 0), slope=1, color="red", linestyle="--", label="y = x")
plt.legend()
plt.grid(alpha=0.5)
plt.show()