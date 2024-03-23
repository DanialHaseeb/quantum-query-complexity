def powerset(set: list[int]) -> list[list[int]]:
	"""
	Returns all possible subsets of the given set.
	:param set: The given set.
	"""
	from itertools import chain, combinations
	subsets = chain.from_iterable(combinations(set, i) for i in range(len(set)+1))
	return list(map(list, subsets))

def bits(number: int, length: int) -> list[int]:
	"""
	Returns the binary representation of the given number and length as a list.
	:param number: The given number.
	:param length: The length of the binary representation.
	"""
	return [int(x) for x in bin(number)[2:].zfill(length)]

def expression(indices: list[int], coefficients: int) -> str:
	"""
	Returns the expression of the given indices and coefficients as a string.
	:param indices: The given indices.
	:param coefficients: The given coefficients.
	"""
	sub = ["₁", "₂", "₃", "₄", "₅", "₆", "₇", "₈"]
	def term(variables: list[int]) -> str:
		if len(variables) == 0:
			return "0"
		result = ""
		for i in variables:
			result += f"𝑥{sub[i]}"
		return result
	n = len(indices)
	m = (1 << n) - 1 - n
	c = bits(coefficients, m)
	terms = list(map(term, powerset(list(range(n)))[1:]))
	counter = 0
	pointer = 0
	for i in range(len(terms)):
		if i in indices:
			terms[i] = f"s{sub[counter]}{terms[i]}"
			counter += 1
		else:
			if c[pointer] == 0:
				terms[i] = ""
			pointer += 1
	terms = list(filter(lambda x: x != "", terms))
	return " ⊕ ".join(terms)

def f(x: int, secrets: int, coefficients: int, indices: list[int]) -> int:
	from functools import reduce
	from operator import mul, xor
	n = len(indices)
	m = (1 << n) - 1 - n
	s = bits(secrets, n)
	c = bits(coefficients, m)
	pointer_s = 0
	pointer_c = 0
	subsets = powerset(bits(x, n))[1:]
	terms = [reduce(mul, subset, 1) for subset in subsets]
	for i in range(len(terms)):
		if i in indices:
			terms[i] *= s[pointer_s]
			pointer_s += 1
		else:
			terms[i] *= c[pointer_c]
			pointer_c += 1
	return reduce(xor, terms, 0)

def sub(i: int) -> str:
	match i:
		case 0: return "₁"
		case 1: return "₂"
		case 2: return "₃"
		case 3: return "₄"
		case 4: return "₅"
		case 5: return "₆"
		case 6: return "₇"
		case 7: return "₈"
		case _: return "₉"
