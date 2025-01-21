import pandas as pd
import os

# Specify the paths to your CSV files
csv_files = [
    '07_preMCF7_uniqueAA.csv',  # Replace with your actual file paths
    '05_MCF7_uniqueAA_Barcode_non_overlap.csv',
    '07_preMCF10A_uniqueAA.csv',
    '05_MCF10A_uniqueAA_Barcode_non_overlap.csv'
]

output_overlapping_file = '07_overlapping_Barcoderemoval.csv'
output_non_overlapping_file = '07_non_overlapping_Barcoderemoval.csv'

# Function to read a CSV file into a DataFrame
def read_csv_sequences(file_path):
    # Extract the file name (without extension) to use as the count column name
    file_name = os.path.splitext(os.path.basename(file_path))[0]
    df = pd.read_csv(file_path)
    df = df.rename(columns={'Count': f"Count_{file_name}"})  # Rename the count column
    return df

# Function to compare multiple files and output overlapping and non-overlapping sequences
def compare_multiple_files(files, overlapping_file, non_overlapping_file):
    # Read all files into DataFrames, renaming the Count column for each file
    dataframes = [
        read_csv_sequences(file) for file in files
    ]

    # Merge all DataFrames on 'Amino Acid Sequence' to find overlapping sequences
    overlapping_df = dataframes[0]
    for df in dataframes[1:]:
        overlapping_df = pd.merge(overlapping_df, df, on='Amino Acid Sequence', how='inner')

    # Merge all DataFrames using an outer join to include all sequences
    all_sequences_df = dataframes[0]
    for df in dataframes[1:]:
        all_sequences_df = pd.merge(all_sequences_df, df, on='Amino Acid Sequence', how='outer')

    # Fill NaN values with 0 for clarity
    all_sequences_df = all_sequences_df.fillna(0)

    # Identify non-overlapping sequences (those not present in all files)
    non_overlapping_df = all_sequences_df[~all_sequences_df['Amino Acid Sequence'].isin(overlapping_df['Amino Acid Sequence'])]

    # Write the results to CSV files
    overlapping_df.to_csv(overlapping_file, index=False)
    non_overlapping_df.to_csv(non_overlapping_file, index=False)

    return overlapping_df, non_overlapping_df

# Compare the files and get the overlapping and non-overlapping sequences
overlapping_df, non_overlapping_df = compare_multiple_files(
    csv_files, output_overlapping_file, output_non_overlapping_file
)

# Print a summary
print("Overlapping sequences saved to:", output_overlapping_file)
print("Non-overlapping sequences saved to:", output_non_overlapping_file)