class A:
    __slots__ = ('x',)

class B:
    pass

a = A()
a.x = 10

b = B()
b.x = 10

try:
    a.y = 20
except AttributeError as e:
    print("A error:", e)

b.y = 20
print("B y:", b.y)
