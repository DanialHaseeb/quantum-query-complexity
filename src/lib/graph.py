from typing import Self
from lib.tensor.matrix import Vector

class Graph:
	"""A set of vectors that are connected if they are orthogonal."""
	def __init__(self: Self, vectors: list[Vector]):
		import networkx
		n = len(vectors)
		self.graph = networkx.Graph()
		for i in range(n):
			for j in range(i+1, n):
				if vectors[i].is_orthogonal(vectors[j]):


	@property
	def max_clique(self: Self) -> list[int]:
		"""Return the maximum clique in the graph."""
		from networkx.algorithms.approximation import max_clique # type: ignore
		return list(max_clique(self.graph)) # type: ignore
