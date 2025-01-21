from Bio import SeqIO

# Load the fasta file and set the length threshold
fasta_file = "m84137.fasta"  # Replace with your file path
threshold_length = 5000
count = 0

# Parse the fasta file and count sequences above the threshold length
for record in SeqIO.parse(fasta_file, "fasta"):
    if len(record.seq) > threshold_length:
        count += 1

print(f"Number of sequences longer than {threshold_length} bases: {count}")