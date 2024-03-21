from lib.tensor import Tensor
from lib.tensor.vector import Vector
from lib.tensor.matrix import Matrix
from lib.graph import Graph

vectors = [
	Vector(1,  1,  1,  1,  1,  1, -1, -1),
	Vector(1,  1,  -1,  -1,  1,  1, 1, 1),
	Vector(1,  1,  1,  1,  -1,  -1, 1, 10),
	Vector(1,  1,  -1,  -1,  -1,  -1, -1, -1)
]

g = Graph(vectors)

print(f"{g.max_clique}")
