from dataclasses import dataclass
from typing import ClassVar


@dataclass
class Planet:
    name: str
    radius: float
    gravity: float = 9.8
    G: ClassVar[float] = 6.67430e-11

    def weight_on_planet(self, m, r):
        weight = (self.gravity * (self.radius ** 2) * m) / ((self.radius + r) ** 2)
        return weight

    def planet_mass(self):
        massa = self.gravity * (self.radius ** 2) / self.G
        return massa

    def __lt__(self, other):
        if self.radius != other.radius:
            return self.radius < other.radius
        if self.gravity != other.gravity:
            return self.gravity < other.gravity
        return self.name < other.name

    def __le__(self, other):
        if self.radius != other.radius:
            return self.radius <= other.radius
        if self.gravity != other.gravity:
            return self.gravity <= other.gravity
        return self.name <= other.name

    def __str__(self):
        return f'Planet(name=\'{self.name}\', radius={self.radius}, gravity={self.gravity})'


earth = Planet("Earth", 6371000, 9.8)
mars = Planet("Mars", 3389500, 3.71)
venus = Planet("Venus", 6051800, 8.87)
print(earth > mars)
print(earth > venus)
print(venus <= mars)
print(mars < venus)
print(earth == earth)
print(earth != mars)
