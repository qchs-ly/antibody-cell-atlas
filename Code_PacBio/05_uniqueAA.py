import pandas as pd

# List of input and output file pairs
file_pairs = [
    ('04_MCF7_AA_Barcode_non_overlap.csv', '05_MCF7_uniqueAA_Barcode_non_overlap.csv'),
    ('04_MCF10A_AA_Barcode_non_overlap.csv', '05_MCF10A_uniqueAA_Barcode_non_overlap.csv')
]

# Process each file pair
for input_file, output_file in file_pairs:
    # Load the input CSV file
    df = pd.read_csv(input_file)

    # Count unique sequences
    sequence_counts = df["Amino Acid Sequence"].value_counts().reset_index()
    sequence_counts.columns = ["Amino Acid Sequence", "Count"]

    # Save the grouped data to the output CSV file
    sequence_counts.to_csv(output_file, index=False)

    # Print a message to confirm processing
    print(f"Processed {input_file} and saved results to {output_file}")