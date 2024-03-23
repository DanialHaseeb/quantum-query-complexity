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

	def __repr__(self: Self) -> str:
		"""The string representation of this vector."""
		return str(self.components)

	def __getitem__(self: Self, index: tuple[int, ...]) -> float:
		"""
		Get the component of this tensor at the given index.
		:param index: The index of the component to get.
		"""
		return self.components[index]

	def __setitem__(self: Self, index: tuple[int, ...], value: float):
		"""
		Set the component of this tensor at the given index.
		:param index: The index of the component to set.
		:param value: The value to set the component to.
		"""
		self.components[index] = value

	def __eq__(self: Self, other: Any) -> bool:
		"""
		Check if this tensor is equal to another tensor.
		:param other: The tensor to compare to.
		"""
		assert self.dimensions == other.dimensions
		from numpy import allclose
		return allclose(self.components, other.components)

	def __neg__(self: Self) -> Self:
		"""The negation of this tensor."""
		return -1.0 * self

	def __add__(self: Self, other: Self) -> Self:
		"""Add this tensor to another tensor."""
		return type(self)(*(self.components + other.components))

	def __sub__(self: Self, other: Self) -> Self:
		"""Subtract another tensor from this tensor."""
		return type(self)(*(self.components - other.components))

	def __mul__(self: Self, scalar: float) -> Self:
		"""Multiply this tensor by a scalar."""
		return type(self)(*(scalar * self.components))

	def __rmul__(self: Self, scalar: float) -> Self:
		"""Multiply this tensor by a scalar."""
		return self * scalar

	def __truediv__(self: Self, scalar: float) -> Self:
		"""Divide this tensor by a scalar."""
		return self * (1.0 / scalar)
