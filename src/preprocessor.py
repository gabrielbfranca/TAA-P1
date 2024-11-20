from scipy.io import mmread
import numpy as np
import matplotlib.pyplot as plt
import networkx as nx

# Load the matrix from the .mtx file
matrix = mmread("../data/soc-dolphins.mtx").tocsc()  # Convert to a Compressed Sparse Column format

# Check if the matrix is square (adjacency matrices are typically square for graphs)
if matrix.shape[0] != matrix.shape[1]:
    raise ValueError("The matrix should be square to represent a graph adjacency matrix.")

# Create a graph with nodes and edges given by .mtx file.
graph = nx.Graph(matrix)

# List the degrees by node
for node, degree in graph.degree:
    print(f"Node: {node + 1}, Degree: {degree}")

# The number of maximal cliques in G
print(f"\nThe number of maximal cliques in the graph: {sum(1 for c in nx.find_cliques(graph))}")

# The largest maximal clique in G
print(f"\nThe largest maximal clique in the graph: {max(nx.find_cliques(graph), key=len)}")

# 3d spring layout
pos = nx.spring_layout(graph, dim=3, seed=779)
# Extract node and edge positions from the layout
node_xyz = np.array([pos[v] for v in sorted(graph)])
edge_xyz = np.array([(pos[u], pos[v]) for u, v in graph.edges()])

# Create the 3D figure
fig = plt.figure()
ax = fig.add_subplot(111, projection="3d")

# Plot the nodes - alpha is scaled by "depth" automatically
ax.scatter(*node_xyz.T, s=100, ec="w")

# Plot the edges
for vizedge in edge_xyz:
    ax.plot(*vizedge.T, color="tab:gray")


def _format_axes(ax):
    """Visualization options for the 3D axes."""
    # Turn gridlines off
    ax.grid(False)
    # Suppress tick labels
    for dim in (ax.xaxis, ax.yaxis, ax.zaxis):
        dim.set_ticks([])
    # Set axes labels
    ax.set_xlabel("x")
    ax.set_ylabel("y")
    ax.set_zlabel("z")


_format_axes(ax)
fig.tight_layout()
plt.show()
