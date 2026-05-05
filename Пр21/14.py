class Vector:
    __slots__ = ('x', 'y')

    def add(self, other):
        return Vector.from_values(self.x + other.x, self.y + other.y)

    @classmethod
    def from_values(cls, x, y):
        v = cls()
        v.x = x
        v.y = y
        return v

v1 = Vector.from_values(1, 2)
v2 = Vector.from_values(3, 4)

v3 = v1.add(v2)
print(v3.x, v3.y)
