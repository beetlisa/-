class Employee:
    __slots__ = ('name', 'salary')

    def increase(self, percent):
        self.salary += self.salary * percent / 100

e = Employee()
e.name = "John"
e.salary = 1000

e.increase(10)
print(e.salary)
