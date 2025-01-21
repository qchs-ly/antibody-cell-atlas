import pandas as pd

# Specify the paths to your two CSV files
csv_file1 = '05_MCF7_uniqueAA.csv'
csv_file2 = '05_MCF10A_uniqueAA.csv'
output_overlapping_file = '06_overlapping.csv'
output_non_overlapping_file = '06_non_overlapping.csv'

# Function to read the CSV file and return a DataFrame
def read_csv_sequences(file_path):
    return pd.read_csv(file_path)

# Function to compare sequences and output both overlapping and non-overlapping sequences
def compare_csv_files(file1, file2, overlapping_file, non_overlapping_file):
    # Read both CSV files into DataFrames
    df1 = read_csv_sequences(file1)
    df2 = read_csv_sequences(file2)

    # Rename the count columns to distinguish them
    df1 = df1.rename(columns={'Count': 'count_mcf7'})
    df2 = df2.rename(columns={'Count': 'count_mcf10A'})

    # Find overlapping sequences using an inner join
    overlapping_df = pd.merge(df1, df2, on='Amino Acid Sequence', how='inner')

    # Find non-overlapping sequences using outer join and filtering
    all_sequences_df = pd.merge(df1, df2, on='Amino Acid Sequence', how='outer', indicator=True)

    # Filter non-overlapping sequences (those not present in both files)
    non_overlapping_df = all_sequences_df[all_sequences_df['_merge'] != 'both']

    # Drop the '_merge' column for clarity
    non_overlapping_df = non_overlapping_df.drop(columns=['_merge'])

    # Write the overlapping and non-overlapping results to separate files
    overlapping_df.to_csv(overlapping_file, index=False)
    non_overlapping_df.to_csv(non_overlapping_file, index=False)

    return overlapping_df, non_overlapping_df

# Compare the two CSV files and get the overlapping and non-overlapping sequences
overlapping_df, non_overlapping_df = compare_csv_files(
    csv_file1, csv_file2, output_overlapping_file, output_non_overlapping_file
)

# Print a summary
print("Overlapping sequences saved to:", output_overlapping_file)
print("Non-overlapping sequences saved to:", output_non_overlapping_file)