from typing import Self
from . import Tensor

class Vector(Tensor):
	"""A vector is a mathematical object that has a magnitude and a direction."""
	def __init__(self: Self, *components: float):
		"""
		Create a new vector with the given components.
		:param components: The entries of the vector.
		"""
		super().__init__(list(components))

	@property
	def magnitude(self) -> float:
		"""The magnitude of this vector."""
		from numpy.linalg import norm
		return float(norm(self.components))

	@property
	def direction(self: Self) -> Self:
		"""The direction of the vector."""
		return self / self.magnitude

	@property
	def is_unit(self: Self) -> bool:
		"""Whether this vector is a unit vector."""
		from math import isclose
		return isclose(self.magnitude, 1.0)

	def dot(self: Self, other: Self) -> float:
		"""
		Compute the dot product of two vectors.
		:param other: The vector to dot with this one.
		"""
		assert self.dimensions == other.dimensions
		from numpy import dot
		return dot(self.components, other.components)

	def cross(self: Self, other: Self) -> Self:
		"""
		Compute the cross product of two vectors.
		:param other: The vector to cross with this one.
		"""
		assert self.dimensions == other.dimensions == (3,)
		from numpy import cross
		return type(self)((cross(self.components, other.components)).tolist())

	def projection(self: Self, other: Self) -> Self:
		"""
		Compute the projection of this vector onto another.
		:param other: The vector to project onto.
		"""
		assert self.dimensions == other.dimensions
		return (self.dot(other) / other.magnitude) * other.direction

	def rejection(self: Self, other: Self) -> Self:
		"""
		Compute the rejection of this vector from another.
		:param other: The vector to reject from.
		"""
		return self - self.projection(other)

	def angle(self: Self, other: Self) -> float:
		"""
		Compute the angle between two vectors.
		:param other: The vector to compute the angle with.
		"""
		assert self.dimensions == other.dimensions
		from math import acos
		return acos(self.dot(other) / (self.magnitude * other.magnitude))

	def is_parallel(self: Self, other: Self) -> bool:
		"""
		Whether this vector is parallel to another.
		:param other: The vector to compare to this one.
		"""
		from math import pi
		return self.is_zero or other.is_zero or self.angle(other) in (0.0, pi)

	def is_orthogonal(self: Self, other: Self) -> bool:
		"""
		Whether this vector is orthogonal to another.
		:param other: The vector to compare to this one.
		"""
		from math import isclose
		return isclose(self.dot(other), 0.0)

	@staticmethod
	def new(*dimensions: int) -> "Vector":
		"""
		Create a new vector with the given dimensions where each entry is zero.
		:param dimensions: The dimensions of the vector.
		"""
		assert len(dimensions) == 1
		from numpy import zeros
		return Vector(zeros(dimensions).tolist())
