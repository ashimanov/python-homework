from functools import total_ordering

@total_ordering
class SomeClass:
    def __init__(self, name, value):
        self.name = name
        self.value = value

    def __eq__(self, other):
        # print(f'{self.name} is equal to {other.name}:')
        return self.value == other.value

    def __gt__(self, other):
        print(f'{self.name} is greater than {other.name}:')
        return self.value > other.value


a = SomeClass('"a"', 1)
b = SomeClass('"b"', 2)


print(a < b)
print(a > b)

import math
from functools import total_ordering

@total_ordering
class Point:
    def __init__(self, x, y) -> None:
        self._x = x
        self._y = y

    def __repr__(self) -> str:
        return f'Point(x={self._x}, y={self._y})'
    
    def __hash__(self) -> int:
        return hash(abs(self))
    
    def __eq__(self, other) -> bool:
        return hash(self) == hash(other)
    
    def __lt__(self, other) -> bool:
        return abs(self) < abs(other)

    def __abs__(self):
        return math.sqrt(self._x ** 2 + self._y ** 2)
    
    def __add__(self, other):
        return Point(
            self._x + other._x,
            self._y + other._y
            )
    
    def __sub__(self, other):
        return Point(
            self._x - other._x,
            self._y - other._y
        )
    
    def __mul__(self, other):
        return Point(
            self._x * other._x,
            self._y * other._y
        )

    def __pos__(self):
        return Point(+self._x, +self._y)
    
    def __neg__(self):
        return Point(-self._x, -self._y)

    def __invert__(self):
        return Point(self._y, self._x)

    def __int__(self):
        return int(abs(self))

    def __float__(self):
        return float(abs(self))
    
    def __round__(self, ndigits=None):
        return round(abs(self), ndigits)



p1 = Point(1, 1)
p2 = Point(1, 5)
print(abs(p1))
print(round(p1, 2))

