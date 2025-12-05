import lab_03
import unittest
from student import Student
from student_list import StudentList
class testLab(unittest.TestCase):
    def test_add_student(self):
        #1 Test
        lst = StudentList()
        student = Student("Artem", "0631234567", "artem@example.com", "KB-243")
        result1 = lst.add_student(student)
        self.assertTrue(result1)
        self.assertEqual(lst.students[0].name, "Artem")

        #2 Test
        lst.add_student(Student("Sasha", "0631234567", "sasha@example.com", "KB-243"))
        lst.add_student(Student("Dima", "0631234567", "dima@example.com", "KB-243"))
        self.assertEqual(lst.students[1].name, "Dima")

        #3 Test
        lst.add_student(Student("Zahar", "0631234567", "zahar@example.com", "KB-243"))
        self.assertEqual(lst.students[-1].name, "Zahar")

        #4 Test
        result2 = lst.add_student(Student("Artem", "0631234567", "artem@example.com", "KB-243"))
        self.assertFalse(result2)

    def test_delete_student(self):
        lst = StudentList()

        #1 Test
        result1 = lst.delete_student("Ivan")
        self.assertFalse(result1)

        #2 Test
        lst.add_student(Student("Sasha", "0631234567", "sasha@example.com", "KB-243"))
        lst.add_student(Student("Dima", "0631234567", "dima@example.com", "KB-243"))
        lst.add_student(Student("Alice", "0631234567", "alice@example.com", "KB-243"))

        result2 = lst.delete_student("Dima")
        self.assertTrue(result2)
        self.assertEqual(len(lst.students), 2)
        self.assertNotIn("Dima", [s.name for s in lst.students])

        #3 Test
        result3 = lst.delete_student("Andrii")
        self.assertFalse(result3)

    def test_update_student(self):
        lst = StudentList()
        lst.add_student(Student("Sasha", "0631234567", "sasha@example.com", "KB-243"))
        lst.add_student(Student("Dima", "0631234567", "dima@example.com", "KB-243"))
        lst.add_student(Student("Alice", "0631234567", "alice@example.com", "KB-243"))
        lst.add_student(Student("Zahar", "0631234567", "zahar@example.com", "KB-243"))

        #1 Test
        result = lst.update_student("Sasha", Student("Andrii", "0631234567", "andrii@example.com", "KB-243"))
        self.assertTrue(result)
        self.assertEqual(lst.students[1].name, "Andrii")

        #2 Test
        result2 = lst.update_student("Dima", Student("Ivan", "0631234567", "ivan@example.com", "KB-243"))
        self.assertTrue(result2)
        self.assertEqual(lst.students[2].name, "Ivan")

        #3 Test
        result3 = lst.update_student("Zahar", Student("Alice", "0631234567", "alice@example.com", "KB-243"))
        self.assertFalse(result3)
        self.assertIn("Zahar", [s.name for s in lst.students])

        #4 Test
        result4 = lst.update_student("Victor", Student("Stas", "0631234567", "stas@example.com", "KB-243"))
        self.assertFalse(result4)

    def test_loadData(self):
        from file_work import File_work
        from student_list import StudentList
        from student import Student

        with open("lab_03/test.csv", "w") as file:
            file.write("Name,Phone,Email,Group\n")
            file.write("John,0631112233,john@gmail.com,KB-243\n")

        lst = StudentList()
        fw = File_work("lab_03/test.csv")
        fw.loadData(lst)

        s = lst.students[0]

        self.assertEqual(s.name, "John")
        self.assertEqual(s.phone, "0631112233")
        self.assertEqual(s.email, "john@gmail.com")
        self.assertEqual(s.group, "KB-243")

    def test_saveData(self):
        from file_work import File_work
        from student_list import StudentList
        from student import Student

        lst = StudentList()
        lst.students = [
            Student("Alice", "0631234567", "alice@example.com", "KB-243"),
            Student("John", "0631234567", "john@example.com", "KB-243")
        ]

        fw = File_work("lab_03/test2.csv")
        fw.saveData(lst)

        with open("lab_03/test2.csv", "r") as file:
            lines = file.readlines()
        self.assertEqual(lines[1].strip(), "Alice,0631234567,alice@example.com,KB-243")

if __name__ == "__main__":
    unittest.main()