import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Load the CSV file
csv_file = "05_MCF10A_uniqueAA.csv"  # Replace with your file name
df = pd.read_csv(csv_file)

# Ensure the CSV contains the necessary columns
if "Amino Acid Sequence" not in df.columns or "Count" not in df.columns:
    raise ValueError("CSV must contain 'Amino Acid Sequence' and 'Count' columns.")

# Normalize the counts to calculate frequencies (optional)
df['Frequency'] = df['Count'] / df['Count'].sum()

# Create a violin plot for the frequency distribution
plt.figure(figsize=(10, 6))
sns.violinplot(y=df['Frequency'], color="skyblue", inner="quartile")
plt.title("illumina MCF10A Amino Acid Sequence Frequencies")
plt.ylabel("Frequency")
plt.grid(axis='y', alpha=0.75)
plt.show()