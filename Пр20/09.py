class Circle:
    __slots__ = ('radius',)

    def area(self):
        return 3.14 * self.radius ** 2

c = Circle()
c.radius = 3

print(c.area())
