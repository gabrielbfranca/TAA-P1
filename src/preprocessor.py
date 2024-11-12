from scipy.io import mmread
import numpy as np

# Load the matrix from the .mtx file
matrix = mmread("../data/soc-dolphins.mtx").tocsc()  # Convert to a Compressed Sparse Column format

# Check if the matrix is square (adjacency matrices are typically square for graphs)
if matrix.shape[0] != matrix.shape[1]:
    raise ValueError("The matrix should be square to represent a graph adjacency matrix.")

# Calculate the degree of each vertex
# Sum the number of non-zero entries in each row for an undirected graph
degrees = np.array(matrix.getnnz(axis=1))

# Print the degrees of each vertex
for vertex, degree in enumerate(degrees):
    print(f"Vertex {vertex}: Degree {degree}")
