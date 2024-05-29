# from itertools import combinations
# from lib.function import Function
# from lib.graph import Graph

# n = 3						# The number of input bits
# N = 1 << n			# Size of the powerset of the input bits
# m = N - 1 - n		# The number of remaining coefficients
# 
# for s_indices in map(list, list(combinations(range(N - 1), n))):
# 	for coefficients in range(1 << m):
# 		function = Function(s_indices, coefficients)
# 		basis = Graph(function.table.columns).max_clique
# 		print("General form:", function.equation)
# 		print("Basis vectors:", len(basis))
# 		for i in basis:
# 			print(f"{i}: {function.vector(i)}")
# 		print()



n = 3
N = 1 << n
from lib.tensor.matrix import Vector
from lib.graph import Graph
from lib import bits


for f1 in range(1 << N): # for each possible value of f1
    for f2 in range(1 << N): # for each possible value of f2
        for f3 in range(1 << N): # for each possible value of f3
            matrix = []
            for s in range(N): # for each possible value of s
                s1 = (s & 1) >> 0
                s2 = (s & 2) >> 1
                s3 = (s & 4) >> 2
                g = (f1 * s1) ^ (f2 * s2) ^ (f3 * s3)
                g_bit_array = bits(g, N)
                g_bit_array = [1 if b == 0 else -1 for b in g_bit_array]
                g_vector = Vector(*g_bit_array)
                matrix.append(g_vector)
            basis = Graph(matrix).max_clique
            if len(basis) == N:
                print(f1, f2, f3, " Basis:", basis[0])




