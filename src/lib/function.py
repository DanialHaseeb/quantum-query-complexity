from typing import Self
from lib import *
from lib.tensor.matrix import Matrix

class Function:
	"""A Svetlichny-like function."""
	def __init__(self: Self, s_indices: list[int], coefficients: int):
		n = len(s_indices)
		N = 1 << n
		self.coefficients = coefficients
		self.s_indices = s_indices
		self.c_indices = [i for i in range(N-1) if i not in s_indices]

	@property
	def table(self: Self) -> Matrix:
		"""The truth table of the function."""
		from functools import reduce
		from operator import mul, xor
		n = len(self.s_indices)
		N = 1 << n
		c = bits(self.coefficients, len(self.c_indices))
		table = Matrix.new(N, N)
		for secret in range(N):
			s = bits(secret, n)
			for x in range(N):
				terms = [reduce(mul, term, 1) for term in powerset(bits(x, n))[1:]]
				for (i, bit) in enumerate(s):
					terms[self.s_indices[i]] *= bit
				for (i, bit) in enumerate(c):
					terms[self.c_indices[i]] *= bit
				table[x, secret] = 1 if reduce(xor, terms, 0) == 0 else -1
		return table

	@property
	def terms(self: Self) -> list[str]:
		"""The equation of the function."""
		indices = list(range(len(self.s_indices)))
		terms = list(map(Function.term, powerset(indices)[1:]))
		c = bits(self.coefficients, len(self.c_indices))
		for i, index in enumerate(self.s_indices):
			terms[index] = f"s{sub(i)}{terms[index]}"
		for i, index in enumerate(self.c_indices):
			if c[i] == 0:
				terms[index] = ""
		return list(filter(lambda term: term != "", terms))

	@property
	def equation(self: Self) -> str:
		"""The equation of the function."""
		return " ⊕ ".join(self.terms)

	def vector(self: Self, i: int) -> str:
		s = bits(i, len(self.s_indices))
		terms = self.terms.copy()
		counter = 0
		for i in range(len(terms)):
			if terms[i][0] == "s":
				if s[counter] == 0:
					terms[i] = ""
				else:
					terms[i] = terms[i][2:]
				counter += 1
		terms = filter(lambda term: term != "", terms)
		terms = " ⊕ ".join(terms)
		if terms == "":
			terms = "0"
		return terms


	@staticmethod
	def term(variables: list[int]) -> str:
		if len(variables) == 0:
			return "0"
		result = ""
		for i in variables:
			result += f"𝑥{sub(i)}"
		return result
