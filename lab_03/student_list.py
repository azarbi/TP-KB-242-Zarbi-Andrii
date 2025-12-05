from student import Student

class StudentList:
    def __init__(self):
        self.students = []
    
    def add_student(self, student: Student):
        for s in self.students:
            if s.name == student.name:
                return False

        insertPosition = 0
        for s in self.students:
            if student.name > s.name:
               insertPosition += 1
            else:
                break

        self.students.insert(insertPosition, student)
        return True
    
    def delete_student(self, name):
        for i, s in enumerate(self.students):
            if s.name == name:
                del self.students[i]
                return True
        return False
    
    def update_student(self, old_name, new_student: Student):
        for s in self.students:
            if s.name == new_student.name and s.name != old_name:
                return False
        for i, s in enumerate(self.students):
            if s.name == old_name:
                del self.students[i]
                break
        else:
            return False
            
        insertPosition = 0
        for s in self.students:
            if new_student.name > s.name:
               insertPosition += 1
            else:
                break

        self.students.insert(insertPosition, new_student)
        return True

    def print_all(self):
        for s in self.students:
            print(s)