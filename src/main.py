from scipy.io import mmread
import numpy as np
import matplotlib.pyplot as plt
import networkx as nx

# carrega a matriz de adjacentes
matrix = mmread(
    "../data/soc-dolphins.mtx"
).tocsc()  # converte para um formato comprimido

# checa se tamanho são iguais
if matrix.shape[0] != matrix.shape[1]:
    raise ValueError(
        "The matrix should be square to represent a graph adjacency matrix."
    )

# Cria um grafo com nodos e arestas com o arquivo .mtx
graph = nx.Graph(matrix)

# Lista os graus de cada nodo
print("graus dos vértices:")
for node, degree in graph.degree:
    print(f"Vértice: {node + 1}, Graus: {degree}")

# calcula os números de cliques maximais
print(f"\nA qtd. de clqiues maximais no grafo:{sum(1 for c in nx.find_cliques(graph))}")

# Calcula o clique maximal
print(f"\nO maior clique no grafo: {max(nx.find_cliques(graph), key=len)}")

# calcula o coeficiente de algomaração para cada vértice
clustering_coefficients = nx.clustering(graph)

print("\nCoeficiente de aglomeração de cada vértice:")
for node, coeff in clustering_coefficients.items():
    print(f"Vértice: {node + 1}, Coeficiente de aglomeração: {coeff:.3f}")

# calcula o coeficiente de aglomeração médio
average_clustering = nx.average_clustering(graph)
print(f"\nThe average clustering coefficient of the graph: {average_clustering:.3f}")

# incialização para 3d
pos = nx.spring_layout(graph, dim=3, seed=779)
# extrai vértices e arestas
node_xyz = np.array([pos[v] for v in sorted(graph)])
edge_xyz = np.array([(pos[u], pos[v]) for u, v in graph.edges()])

fig = plt.figure()
ax = fig.add_subplot(111, projection="3d")

# plota os vértices
ax.scatter(*node_xyz.T, s=100, ec="w")

# Plota as arestas
for vizedge in edge_xyz:
    ax.plot(*vizedge.T, color="tab:gray")


def _format_axes(ax):
    """Visualization options for the 3D axes."""
    # remove os alinhamentos
    ax.grid(False)

    for dim in (ax.xaxis, ax.yaxis, ax.zaxis):
        dim.set_ticks([])

    ax.set_xlabel("x")
    ax.set_ylabel("y")
    ax.set_zlabel("z")


_format_axes(ax)
fig.tight_layout()
plt.show()
