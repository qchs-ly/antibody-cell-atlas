import pandas as pd

# Specify the paths to your two CSV files
csv_file1 = 'barcode_MCF7_3204.csv'  # Replace with your actual file path
csv_file2 = 'barcode_MCF10A_2858.csv'

# Specify the output file paths
output_file1 = 'barcode_MCF7_3204_nonoverlapping.csv'
output_file2 = 'barcode_MCF10A_2858_nonoverlapping.csv'

# Function to exclude overlapping barcodes
def exclude_overlapping_barcodes(file1, file2, output1, output2):
    # Read the two CSV files into DataFrames
    df1 = pd.read_csv(file1)
    df2 = pd.read_csv(file2)

    # Ensure the barcode column is named correctly
    if 'Barcode' not in df1.columns or 'Barcode' not in df2.columns:
        print("Error: Both CSV files must have a 'barcode' column.")
        return

    # Find barcodes that are unique to each file
    unique_to_file1 = df1[~df1['Barcode'].isin(df2['Barcode'])]
    unique_to_file2 = df2[~df2['Barcode'].isin(df1['Barcode'])]

    # Save the unique barcodes to new CSV files
    unique_to_file1.to_csv(output1, index=False)
    unique_to_file2.to_csv(output2, index=False)

    print(f"Non-overlapping barcodes from {file1} saved to {output1}")
    print(f"Non-overlapping barcodes from {file2} saved to {output2}")

# Call the function
exclude_overlapping_barcodes(csv_file1, csv_file2, output_file1, output_file2)