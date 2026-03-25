from collections.abc import Iterable, Iterator

class Matter1Iterator(Iterator):
    def __init__(self, students):
        self.sorted_students = sorted(students, key=lambda x: x.subject1, reverse=True)
        self.index = 0

    def __next__(self):
        if self.index >= len(self.sorted_students):
            raise StopIteration
        student = self.sorted_students[self.index]
        self.index += 1
        return student

class Student:
    def __init__(self, name, subject1, subject2, subject3):
        self.name = name
        self.subject1 = subject1
        self.subject2 = subject2
        self.subject3 = subject3

    @property
    def average(self):
        return (self.subject1 + self.subject2 + self.subject3) / 3

class SchoolClass(Iterable):
    def __init__(self):
        self.students = []

    def add_student(self, student: Student):
        self.students.append(student)

    def __iter__(self):
        return Matter1Iterator(self.students)

if __name__ == '__main__':
    school_class = SchoolClass()
    school_class.add_student(Student('J', 10, 12, 13))
    school_class.add_student(Student('A', 8, 2, 17))
    school_class.add_student(Student('V', 9, 14, 14))
    
    print("--- Parcours avec l'Itérateur (Matière 1) ---")
    for student in school_class:
        print(f"{student.name} : {student.subject1}")
