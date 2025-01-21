import pandas as pd
import matplotlib.pyplot as plt

# Load the two CSV files
pacbio_file = "07_preMCF7_uniqueAA.csv"  # Replace with your PacBio CSV file path
illumina_file = "05_MCF7_uniqueAA.csv"  # Replace with your Illumina CSV file path

pacbio_df = pd.read_csv(pacbio_file)
illumina_df = pd.read_csv(illumina_file)

# Ensure the sequence column is named the same in both files
# Assuming columns are "sequence" and "frequency"
if "Amino Acid Sequence" not in pacbio_df.columns or "Count" not in pacbio_df.columns:
    raise ValueError("PacBio file must have 'sequence' and 'frequency' columns")
if "Amino Acid Sequence" not in illumina_df.columns or "Count" not in illumina_df.columns:
    raise ValueError("Illumina file must have 'sequence' and 'frequency' columns")

# Merge the datasets on the "sequence" column
merged_df = pd.merge(pacbio_df, illumina_df, on="Amino Acid Sequence", how="outer", suffixes=("_pacbio", "_illumina"))

# Fill NaN frequencies with 0 (for sequences not present in one of the datasets)
merged_df["Count_pacbio"] = merged_df["Count_pacbio"].fillna(0)
merged_df["Count_illumina"] = merged_df["Count_illumina"].fillna(0)

# Normalize frequencies to make them comparable
merged_df["normalized_pacbio"] = merged_df["Count_pacbio"] / merged_df["Count_pacbio"].sum()
merged_df["normalized_illumina"] = merged_df["Count_illumina"] / merged_df["Count_illumina"].sum()

# Plot histograms for the frequency distributions
plt.figure(figsize=(10, 6))
plt.hist(merged_df["normalized_pacbio"], bins=50, alpha=0.5, label="PacBio")
plt.hist(merged_df["normalized_illumina"], bins=50, alpha=0.5, label="Illumina")
plt.title("Frequency Distribution Comparison")
plt.xlabel("Normalized Frequency")
plt.ylabel("Count")
plt.legend()
plt.show()

# Plot scatter plot for direct comparison
plt.figure(figsize=(8, 8))
plt.scatter(merged_df["normalized_pacbio"], merged_df["normalized_illumina"], alpha=0.7)
plt.title("Frequency Correlation Between PacBio and Illumina")
plt.xlabel("PacBio Normalized Frequency")
plt.ylabel("Illumina Normalized Frequency")
plt.axline((0, 0), slope=1, color="red", linestyle="--", label="y=x")
plt.legend()
plt.show()