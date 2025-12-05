import csv
from student import Student
from student_list import StudentList

class File_work:
    def __init__(self, path):
        self.path = path

    def loadData(self, student_list: StudentList):
        with open(self.path, "r") as file:
            reader = csv.DictReader(file)
            for row in reader:
                student_list.add_student(Student(row["Name"], row["Phone"], row["Email"], row["Group"]))

    def saveData(self, student_list: StudentList):
        with open(self.path, "w", newline="") as file:
            fieldnames = ["Name", "Phone", "Email", "Group"]
            writer = csv.DictWriter(file, fieldnames=fieldnames)
            writer.writeheader()

            for student in student_list.students:
                writer.writerow({"Name": student.name, "Phone": student.phone, "Email": student.email, "Group": student.group})