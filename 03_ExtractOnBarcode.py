import pandas as pd
from Bio.Seq import Seq

# File paths
barcode_file = "barcode_MCF7_3204_nonoverlapping.csv"  # File with barcodes
sequence_file = "02_extract.csv"  # File with sequences (contains raw sequences in one column)
output_file = "03_MCF7_Barcode_non_overlap.csv"

# Load the barcodes
barcodes_df = pd.read_csv(barcode_file)

# Remove the "-1" suffix from each barcode
barcodes_df['cleaned_barcode'] = barcodes_df['Barcode'].str.replace('-1', '', regex=False)
# Compute reverse complements for cleaned barcodes
barcodes_df['reverse_complement'] = barcodes_df['cleaned_barcode'].apply(lambda x: str(Seq(x).reverse_complement()))
barcodes_list = barcodes_df['reverse_complement'].tolist()  # Assuming barcodes are in the first column

# Load the sequences
sequences_df = pd.read_csv(sequence_file)

# Define the motifs
left_motif = "GGTGGTGGTGGTTCTGCTAGC"
right_motif = "TCCGGAATTCTA"

# Prepare to store matching sequences
matching_data = []

# Iterate over each sequence in the dataset
for _, row in sequences_df.iterrows():
    sequence = row['sequence']
    last_100_nt = row['last_100_nt']

    # Check if the sequence contains any barcode
    for barcode in barcodes_list:
        if barcode in last_100_nt:
            matching_data.append({'barcode': barcode, 'sequence': sequence})

# Convert matches to a DataFrame and save to CSV
matching_df = pd.DataFrame(matching_data)
matching_df.to_csv(output_file, index=False)

print(f"Matching sequences saved to {output_file}")
