#translate nucleotide sequence into aa
#count the number of sequences with and without stop codons
import pandas as pd
from Bio.Seq import Seq

# List of input and output file paths
file_pairs = [
    ('03_MCF7_Barcode_non_overlap.csv', '04_MCF7_AA_Barcode_non_overlap.csv'),
    ('03_MCF10A_Barcode_non_overlap.csv', '04_MCF10A_AA_Barcode_non_overlap.csv')
]

# Process each file pair
for input_file, output_file in file_pairs:
    # Read the CSV into a pandas DataFrame
    df = pd.read_csv(input_file)

    # Assuming the nucleotide sequences are in a column named 'Sequence'
    df['Amino Acid Sequence'] = df['sequence'].apply(lambda x: str(Seq(x).translate()))

    # Filter out sequences with stop codons
    filtered_df = df[df['Amino Acid Sequence'].apply(lambda x: '*' not in x)]

    # Count sequences with and without stop codons
    sequences_with_stop = len(df) - len(filtered_df)
    sequences_without_stop = len(filtered_df)

    # Print the counts
    print(f"Processing {input_file}:")
    print(f"Sequences with stop codons: {sequences_with_stop}")
    print(f"Sequences without stop codons: {sequences_without_stop}")

    # Write the filtered DataFrame (without stop codons) back to a CSV
    filtered_df.to_csv(output_file, index=False)
    print(f"Translation complete and filtered output saved to: {output_file}\n")