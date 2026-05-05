class Animal:
    __slots__ = ('type', 'weight')

a = Animal()
a.type = "cat"
a.weight = 4

try:
    a.color = "black"
except AttributeError as e:
    print(e)
