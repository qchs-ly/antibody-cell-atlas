from Bio import SeqIO
import matplotlib.pyplot as plt
import pandas as pd
# Load the fasta file and calculate sequence lengths
fasta_file = "m84137.fasta"  # Replace with your file path
sequence_lengths = []

# Parse the fasta file and collect sequence lengths
with open(fasta_file, "r") as file:
    for record in SeqIO.parse(file, "fasta"):
        sequence_lengths.append({"ID": record.id, "Sequence": str(record.seq), "Length": len(record.seq)})
# Sort the sequences by length in descending order
sorted_lengths = sorted(sequence_lengths, key=lambda x: x['Length'], reverse=True)
# Export the top 10 sequences to a CSV file
top_10_sequences = sorted_lengths[:10]
df = pd.DataFrame(top_10_sequences)
df.to_csv("top_10_sequences_m84137.csv", index=False)