from typing import Self
from lib.tensor import Tensor
from lib.tensor.vector import Vector

class Matrix(Tensor):
	"""A rectangular array of numbers arranged in rows and columns."""
	def __init__(self: Self, *rows: list[float]):
		"""
		Create a new matrix with the given rows.
		:param rows: The rows of the matrix.
		"""
		super().__init__(list(rows))

	@property
	def transpose(self: Self) -> Self:
		"""The transpose of this matrix."""
		return type(self)(*self.components.T)

	@property
	def rows(self: Self) -> list[Vector]:
		"""The rows of this matrix."""
		return [Vector(*row) for row in self.components]

	@property
	def columns(self: Self) -> list[Vector]:
		"""The columns of this matrix."""
		return self.transpose.rows

	@property
	def determinant(self: Self) -> float:
		"""The determinant of this matrix."""
		assert self.is_square
		from numpy.linalg import det
		return det(self.components)

	@property
	def frobenius_norm(self: Self) -> float:
		"""The Frobenius norm of this matrix."""
		from numpy.linalg import norm
		return float(norm(self.components, ord="fro"))

	@property
	def is_square(self: Self) -> bool:
		"""Whether this matrix is square."""
		return self.dimensions[0] == self.dimensions[1]

	@property
	def is_symmetric(self: Self) -> bool:
		"""Whether this matrix is symmetric."""
		return self == self.transpose

	@property
	def is_orthogonal(self: Self) -> bool:
		"""Whether this matrix is orthogonal."""
		return self.transpose == self.inverse

	@property
	def inverse(self: Self) -> Self:
		"""The inverse of this matrix."""
		from numpy.linalg import inv
		return type(self)(*inv(self.components))

	def __matmul__(self: Self, other: Self) -> Self:
		"""Multiply this matrix by another matrix."""
		assert self.dimensions[1] == other.dimensions[0]
		return type(self)(*(self.components @ other.components))

	def __pow__(self: Self, power: int) -> Self:
		"""Raise this matrix to a power."""
		assert self.is_square
		from numpy.linalg import matrix_power
		return type(self)(*matrix_power(self.components, power))

	@staticmethod
	def new(*dimensions: int) -> "Matrix":
		"""
		Create a new matrix with the given dimensions where each entry is zero.
		:param dimensions: The dimensions of the matrix.
		"""
		from numpy import zeros
		return Matrix(*zeros(dimensions))

	@staticmethod
	def identity(size: int) -> "Matrix":
		"""
		Create a new n x n identity matrix.
		:param n: The size of the identity matrix.
		"""
		from numpy import identity
		return Matrix(*identity(size))
