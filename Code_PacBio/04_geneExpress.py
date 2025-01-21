import scanpy as sc

# Load the filtered matrix from Cell Ranger
adata = sc.read_10x_mtx("filtered_feature_bc_matrix/", var_names="gene_symbols", cache=True)

# Inspect the data
print(adata)  # Shows the number of cells and genes

# Access the expression values for a specific cell (e.g., cell index 0)
cell_expression = adata.X[0, :]
print(cell_expression)

# To get the gene names and expression values for that cell
cell_gene_expression = zip(adata.var_names, cell_expression)
for gene, expression in cell_gene_expression:
    if expression > 0:
        print(f"{gene}: {expression}")

print(adata[:, "CD3D"].X.toarray())

adata.to_df().to_csv("gene_expression_per_cell.csv")