from Bio import SeqIO
import pandas as pd

# Input FASTA file and output CSV file
input_fasta = "01_combined.fasta"  # Replace with your FASTA file name
output_csv = "02_extract.csv"  # Name of the output CSV file

# Define the subsequences
start_subseq = "GGTGGTGGTGGTTCTGCTAGC"
end_subseq = "TCCGGAATTCTA"

# List to store extracted information
data = []

# Process each sequence in the FASTA file
for record in SeqIO.parse(input_fasta, "fasta"):
    full_sequence = str(record.seq)
    # Check if both subsequences are in the sequence
    start_idx = full_sequence.find(start_subseq)
    end_idx = full_sequence.find(end_subseq)

    if start_idx != -1 and end_idx != -1 and start_idx < end_idx:
        # Extract sequence between the subsequences
        extracted_seq = full_sequence[start_idx + len(start_subseq):end_idx]
        # Extract the last 100 nucleotides of the full sequence
        last_100_nt = full_sequence[-100:] if len(full_sequence) >= 100 else full_sequence
        # Append to the data list
        data.append({"sequence": extracted_seq, "last_100_nt": last_100_nt})

# Convert to DataFrame and save as CSV
df = pd.DataFrame(data)
df.to_csv(output_csv, index=False)

print(f"Extracted sequences written to {output_csv}")