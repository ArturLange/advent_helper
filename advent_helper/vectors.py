from collections.abc import Iterable
from typing import Self


class Vector[T]:
    def __init__(self: Self, values: Iterable[T]) -> None:
        self.values = tuple(values)

    @property
    def dimension(self: Self) -> int:
        return len(self.values)
    
    def __add__(self: Self, other: Self):
        return Vector(self.values[index] + other[index] for index in range(self.dimension))
    
    def __sub__(self: Self, other: Self):
        return Vector(self.values[index] - other[index] for index in range(self.dimension))
    
    def __mul__(self: Self, other: int):
        return Vector(self.values[index] * other for index in range(self.dimension))

    def __repr__(self: Self):
        return str(self.values)

    def __getitem__(self: Self, index):
        return self.values[index]
    
    def __len__(self: Self):
        return self.dimension
    
    def euclidean_distance(self: Self, other: Self):
        return ((self.values[0] - other[0]) ** 2 + (self.values[1] - other[1]) ** 2) ** 0.5
    
    def __eq__(self: Self, value: Self):
        return self.values == value.values
    
