from Bio import SeqIO
from Bio.Seq import Seq

# Input and output files
input_fasta = "sequences.fasta"  # Replace with your input file name
output_fasta = "01_filterrc.fasta"  # Name of the output file

# Subsequence criteria
subsequence1 = "TAGAATTCCG"
subsequence2 = "GCTAGCAGAACCACCACCACC"

# Filter and process sequences
with open(output_fasta, "w") as output_handle:
    for record in SeqIO.parse(input_fasta, "fasta"):
        sequence = str(record.seq)
        # Check if both subsequences are present
        if subsequence1 in sequence and subsequence2 in sequence:
            # Convert to reverse complement
            reverse_complement = Seq(sequence).reverse_complement()
            # Update the record with the reverse complement sequence
            record.seq = reverse_complement
            # Write to output file
            SeqIO.write(record, output_handle, "fasta")

print(f"Filtered reverse complement sequences written to {output_fasta}")