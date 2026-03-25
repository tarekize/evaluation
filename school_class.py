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

class Matter2Iterator(Iterator):
    def __init__(self, students):
        self.sorted_students = sorted(students, key=lambda x: x.subject2, reverse=True)
        self.index = 0

    def __next__(self):
        if self.index >= len(self.sorted_students):
            raise StopIteration
        student = self.sorted_students[self.index]
        self.index += 1
        return student

class Matter3Iterator(Iterator):
    def __init__(self, students):
        self.sorted_students = sorted(students, key=lambda x: x.subject3, reverse=True)
        self.index = 0

    def __next__(self):
        if self.index >= len(self.sorted_students):
            raise StopIteration
        student = self.sorted_students[self.index]
        self.index += 1
        return student

class Matter4Iterator(Iterator):
    def __init__(self, students):
        self.sorted_students = sorted(students, key=lambda x: x.subject4, reverse=True)
        self.index = 0

    def __next__(self):
        if self.index >= len(self.sorted_students):
            raise StopIteration
        student = self.sorted_students[self.index]
        self.index += 1
        return student

def add_subject_4(cls):
    """Décorateur de classe qui ajoute une propriété subject4 avec une note par défaut"""
    cls.subject4 = 10  # Note par défaut pour la matière 4
    
    @property
    def new_average(self):
        return (self.subject1 + self.subject2 + self.subject3 + self.subject4) / 4
        
    cls.average = new_average
    return cls

@add_subject_4
class Student:
    def __init__(self, name, subject1, subject2, subject3):
        self.name = name
        self.subject1 = subject1
        self.subject2 = subject2
        self.subject3 = subject3

    @property
    def average(self):
        return (self.subject1 + self.subject2 + self.subject3) / 3

def add_matter_4_iterator(cls):
    """Décorateur de classe qui ajoute la méthode iter_matter_4 à SchoolClass"""
    def iter_matter_4(self):
        return Matter4Iterator(self.students)
    
    cls.iter_matter_4 = iter_matter_4
    return cls

@add_matter_4_iterator
class SchoolClass(Iterable):
    _instance = None

    def __new__(cls, *args, **kwargs):
        if cls._instance is None:
            cls._instance = super(SchoolClass, cls).__new__(cls, *args, **kwargs)
            cls._instance.students = []
        return cls._instance

    def __init__(self):
        # L'initialisation est désormais gérée dans __new__ pour garantir le Singleton
        pass

    def add_student(self, student: Student):
        if student not in self.students:
            self.students.append(student)

    def __iter__(self):
        return Matter1Iterator(self.students)

    def iter_matter_2(self):
        return Matter2Iterator(self.students)

    def iter_matter_3(self):
        return Matter3Iterator(self.students)

if __name__ == '__main__':
    school_class = SchoolClass()
    school_class.add_student(Student('J', 10, 12, 13))
    school_class.add_student(Student('A', 8, 2, 17))
    school_class.add_student(Student('V', 9, 14, 14))
    
    print("--- Parcours avec l'Itérateur (Matière 1) ---")
    for student in school_class:
        print(f"{student.name} : {student.subject1}")

    print("\n--- Parcours avec l'Itérateur (Matière 2) ---")
    for student in school_class.iter_matter_2():
        print(f"{student.name} : {student.subject2}")

    print("\n--- Parcours avec l'Itérateur (Matière 3) ---")
    for student in school_class.iter_matter_3():
        print(f"{student.name} : {student.subject3}")

    print("\n--- Parcours avec l'Itérateur Décoré (Matière 4) ---")
    for student in school_class.iter_matter_4():
        print(f"{student.name} : {student.subject4}")

    print("\n--- Vérification de la Matière 4 et de la nouvelle moyenne ---")
    for student in school_class.students:
        print(f"{student.name} - Mat4: {student.subject4} - Moyenne (sur 4): {student.average:.2f}")

    print("\n--- Vérification du Singleton ---")
    another_school_class = SchoolClass()
    print(f"school_class et another_school_class sont la même instance : {school_class is another_school_class}")
    print(f"Nombre d'élèves dans another_school_class: {len(another_school_class.students)}")
