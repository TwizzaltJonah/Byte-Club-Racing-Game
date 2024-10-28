from __future__ import annotations
import math

class Vec2:
    """Multi purpose vector class"""

    def __init__(self, x: float = 0.0, y: float = 0.0):
        self.x: float = float(x)
        self.y: float = float(y)

    @staticmethod
    def fromTuple(xy: tuple[float | int]):
        return Vec2(xy[0], xy[1])

    def __repr__(self):
        return f"Vec2({self.x}, {self.y})"

    """
    some examples of how to use these magic math methods:
    (in the form of 'expression -> result')
    
    Vec2(2.0, 3.0) + Vec2(10.0, 2.0) -> Vec2(12.0, )
    Vec2(12.0, 2.0) - 10.0 -> Vec2(2.0, -8.0)
    Vec2(-1.0, 4.0) * 5.0 -> Vec2(-5.0, 20.0)
    Vec2(10.0, 15.0) / 10.0 -> Vec2(1.0, 1.5)
    
    Vec2(10.0, 2.0) == Vec2(10.0, 3.0) -> False
    Vec2(13.0, 1.0) == Vec2(13.0, 1.0) -> True
    """

    def __add__(self, other: Vec2 | float | int):
        if isinstance(other, Vec2):
            return Vec2(self.x + other.x, self.y + other.y)
        else:
            return Vec2(self.x + other, self.y + other)

    def __sub__(self, other: Vec2 | float | int):
        if isinstance(other, Vec2):
            return Vec2(self.x - other.x, self.y - other.y)
        else:
            return Vec2(self.x - other, self.y - other)

    def __mul__(self, other: Vec2 | float | int):
        if isinstance(other, Vec2):
            return Vec2(self.x * other.x, self.y * other.y)
        else:
            return Vec2(self.x * other, self.y * other)

    def __truediv__(self, other: Vec2 | float | int):
        if isinstance(other, Vec2):
            return Vec2(self.x / other.x, self.y / other.y)
        else:
            return Vec2(self.x / other, self.y / other)

    def __eq__(self, other: Vec2):
        return self.x == other.x and self.y == other.y

    def rotateRadians(self, angle: float):
        """return a vector rotated around the origin by 'angle' radians"""
        return Vec2(self.x * math.cos(angle) - self.y * math.sin(angle),
                    self.x * math.sin(angle) + self.y * math.cos(angle))

    def rotate(self, angle: float):
        """return a vector rotated around the origin by 'angle' degrees"""
        return self.rotateRadians(math.radians(angle))

    def rotateAroundRadians(self, point: Vec2, angle: float):
        """return a vector rotated around 'point' by 'angle' radians"""
        return (self - point).rotateRadians(angle) + point

    def rotateAround(self, point: Vec2, angle: float):
        """return a vector rotated around 'point' by 'angle' radians"""
        return (self - point).rotate(angle) + point

    def asTuple(self):
        return self.x, self.y

    def length(self):
        """return the length of this vector from the origin (its magnitude)"""
        return math.sqrt(self.x ** 2 + self.y ** 2)

    def lengthSquared(self):
        """return the length of this vector from the origin squared (its magnitude squared)

        this is useful because taking the square root (which is needed for regular length) can be somewhat computationally expensive
        """
        return self.x ** 2 + self.y ** 2

    def normalized(self):
        """return a new Vector with the same X:Y ratio but a length of 1 (or normalized)"""
        return self / self.length()
