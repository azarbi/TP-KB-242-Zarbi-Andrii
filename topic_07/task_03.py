class Student:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    def __str__(self):
        return f"{self.name}, {self.age}"

student_list = [
    Student("Artem", 19),
    Student("Dima", 18),
    Student("Sasha", 20),
    Student("Andrii", 19)
    ]

for student in sorted(student_list, key=lambda student: student.age):
    print(student)