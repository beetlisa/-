class Student:
    __slots__ = ('name', 'grade')

    def change_grade(self, value):
        self.grade = value

s = Student()
s.name = "Anna"
s.grade = 4

s.change_grade(5)
print(s.name, s.grade)
