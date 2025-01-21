from Bio import SeqIO
import matplotlib.pyplot as plt

# Load the fasta file and calculate sequence lengths
fasta_file = "m84137.fasta"  # Replace with your file path
sequence_lengths = []

# Parse the fasta file and collect sequence lengths
for record in SeqIO.parse(fasta_file, "fasta"):
    sequence_lengths.append(len(record.seq))

# Plot the length distribution
plt.figure(figsize=(10, 6))
plt.hist(sequence_lengths, bins=30, edgecolor="black")
plt.title("Sequence Length Distribution")
plt.xlabel("Sequence Length")
plt.ylabel("Frequency")
plt.grid(True)
plt.show()