from typing import Self, Any

class Tensor:
	"""A multidimensional array."""
	def __init__(self: Self, components: list[Any]):
		"""
		Create a new tensor with the given components.
		:param components: The entries of the tensor.
		"""
		from numpy import array
		self.components = array(components)

	@property
	def dimensions(self: Self) -> tuple[int, ...]:
		"""The dimensions of this tensor."""
		return self.components.shape

	@property
	def is_zero(self: Self) -> bool:
		"""Whether this vector is the zero vector."""
		from numpy import allclose
		return allclose(self.components, 0.0)

	@property
	def array(self: Self) -> list[float]:
		"""The components of this vector represented as a Python `list`."""
		return self.components.tolist()

	def __str__(self: Self) -> str:
		"""The string representation of this vector."""
		return str(self.components)

	def __repr__(self: Self) -> str:
		"""The code representation of this vector."""
		return f"{Self}({self.array})"

	def __getitem__(self: Self, index: tuple[int, ...]) -> float:
		"""
		Get the component of this vector at the given index.
		:param index: The index of the component to get.
		"""
		return self.components[index]

	def __setitem__(self: Self, index: tuple[int, ...], value: float):
		"""
		Set the component of this vector at the given index.
		:param index: The index of the component to set.
		:param value: The value to set the component to.
		"""
		self.components[index] = value

	def __eq__(self: Self, other: Any) -> bool:
		"""
		Check if this tensor is equal to another tensor.
		:param other: The tensor to compare to.
		"""
		assert isinstance(other, Self)
		assert self.dimensions == other.dimensions
		from numpy import allclose
		return allclose(self.components, other.components)

	def __neg__(self: Self) -> Self:
		"""The negation of this tensor."""
		return -1.0 * self

	def __add__(self: Self, other: Self) -> Self:
		"""Add this tensor to another tensor."""
		return type(self)((self.components + other.components).tolist())

	def __sub__(self: Self, other: Self) -> Self:
		"""Subtract another tensor from this tensor."""
		return type(self)((self.components - other.components).tolist())

	def __mul__(self: Self, other: float) -> Self:
		"""Multiply this tensor by a scalar."""
		return type(self)((other * self.components).tolist())

	def __rmul__(self: Self, other: float) -> Self:
		"""Multiply this tensor by a scalar."""
		return self * other

	def __truediv__(self: Self, other: float) -> Self:
		"""Divide this tensor by a scalar."""
		return self * (1.0 / other)

	@staticmethod
	def new(*dimensions: int) -> "Tensor":
		"""
		Create a new tensor with the given dimensions where each entry is zero.
		:param dimensions: The dimensions of the tensor.
		"""
		from numpy import zeros
		return Tensor(zeros(dimensions).tolist())
