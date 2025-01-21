import matplotlib.pyplot as plt
import pandas as pd

# Create the dataset
data = {
    "MCF7_10x": [2.687697349, 1.343501714, 0.173818248, 0.000246134, 0.002793476, 0.006242321,
                 0.0722241, 0.036158015, 0.035419612, 0.032388899, 0.018949374, 0.003970769,
                 0.001803008, 0.003522982, 0.000539716, 0.00056344, 9.78606E-05, 5.6344E-05,
                 0.000424063, 0.00084516, 0.00526668, 0.00222707, 0.000240203, 0.001097225,
                 0.000566405],
    "MCF10A_10x": [3.91503445, 1.43790471, 0.183392652, 0.127577497, 0.103656717, 0.047841562,
                   0.037210103, 0.02923651, 0.026578645, 0.023920781, 0.021262916, 0.005315729,
                   0.005315729, 0.005315729, 0.002657865, 0.002657865, 0.002657865, 0.002657865,
                   0.002657865, 0.002657865, 0.002657865, 0.002657865, 0.002657865, 0.002657865,
                   0.002657865]
}

# Create a DataFrame
df = pd.DataFrame(data)

# Plot the scatter plot
plt.figure(figsize=(8, 6))
plt.scatter(df["MCF7_10x"], df["MCF10A_10x"], alpha=0.7, color="blue", label="Data Points")
plt.title("Scatter Plot of MCF7_10x vs MCF10A_10x")
plt.xlabel("MCF7_10x")
plt.ylabel("MCF10A_10x")
plt.axline((0, 0), slope=1, color="red", linestyle="--", label="y = x")
plt.legend()
plt.grid(alpha=0.5)
plt.show()