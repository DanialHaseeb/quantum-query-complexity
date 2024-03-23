from itertools import combinations
from lib.function import Function
from lib.graph import Graph

n = 3						# The number of input bits
N = 1 << n			# Size of the powerset of the input bits
m = N - 1 - n		# The number of remaining coefficients

for s_indices in map(list, list(combinations(range(N - 1), n))):
	for coefficients in range(1 << m):
		function = Function(s_indices, coefficients)
		basis = Graph(function.table.columns).max_clique
		print("General form:", function.equation)
		print("Basis vectors:", len(basis))
		for i in basis:
			print(f"{i}: {function.vector(i)}")
		print()
