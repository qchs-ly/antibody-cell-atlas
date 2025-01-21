import pandas as pd
#load data
matching_df = pd.read_csv("03_extracted_sequences.csv")

# Check duplicate barcodes
duplicate_barcodes = matching_df['barcode'].value_counts()
duplicate_barcodes = duplicate_barcodes[duplicate_barcodes > 1]

if not duplicate_barcodes.empty:
    print("Duplicate barcodes and their frequencies:")
    print(duplicate_barcodes)

# Check duplicate sequences
duplicate_sequences = matching_df['sequence'].value_counts()
duplicate_sequences = duplicate_sequences[duplicate_sequences > 1]

if not duplicate_sequences.empty:
    print("\nDuplicate sequences and their frequencies:")
    print(duplicate_sequences)