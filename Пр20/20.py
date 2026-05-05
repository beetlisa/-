class Student:
    __slots__ = ('name', 'age', 'grades')

    def add_grade(self, value):
        self.grades.append(value)

    def average(self):
        return sum(self.grades) / len(self.grades)

s1 = Student()
s1.name = "A"
s1.age = 20
s1.grades = [4, 5]

s1.add_grade(3)

s2 = Student()
s2.name = "B"
s2.age = 21
s2.grades = [5, 5, 4]

print(s1.average())
print(s2.average())
