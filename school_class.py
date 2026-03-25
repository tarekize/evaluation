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

    def rank_matter_1(self):
        print("--- Classement Matière 1 ---")
        for s in sorted(self.students, key=lambda x: x.subject1, reverse=True):
            print(f"{s.name} : {s.subject1}")

if __name__ == '__main__':
    school_class = SchoolClass()
    school_class.add_student(Student('J', 10, 12, 13))
    school_class.add_student(Student('A', 8, 2, 17))
    school_class.add_student(Student('V', 9, 14, 14))
    school_class.rank_matter_1()
