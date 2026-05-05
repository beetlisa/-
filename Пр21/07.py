class Point:
    __slots__ = ('x', 'y')

    def coords(self):
        return f"({self.x}, {self.y})"

p = Point()
p.x = 3
p.y = 7

print(p.coords())
