class Person:
    __slots__ = ('name', 'age')

p = Person()
p.name = "Ivan"
p.age = 25

print(p.name, p.age)
