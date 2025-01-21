from Bio import SeqIO

# Input and output files
input_fasta = "sequences.fasta"  # Replace with your input file name
output_fasta = "01_filter.fasta"  # Name of the output file

# Subsequence criteria
subsequence1 = "GGTGGTGGTGGTTCTGCTAGC"
subsequence2 = "TCCGGAATTCTA"

# Filter and write sequences
with open(output_fasta, "w") as output_handle:
    for record in SeqIO.parse(input_fasta, "fasta"):
        sequence = str(record.seq)
        if subsequence1 in sequence and subsequence2 in sequence:
            SeqIO.write(record, output_handle, "fasta")

print(f"Filtered sequences written to {output_fasta}")