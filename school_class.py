class Student:
    def __init__(self, name, subject1, subject2, subject3):
        self.name = name
        self.subject1 = subject1
        self.subject2 = subject2
        self.subject3 = subject3

    @property
    def average(self):
        return (self.subject1 + self.subject2 + self.subject3) / 3

class SchoolClass:
    def __init__(self):
        self.students = []

    def add_student(self, student: Student):
        self.students.append(student)
