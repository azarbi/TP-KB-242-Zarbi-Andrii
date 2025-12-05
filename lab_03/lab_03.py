from student import Student
from student_list import StudentList
from file_work import File_work

def main():
    lst = StudentList()
    fw = File_work(r"C:\Folder\TP-KB-242-Zarbi-Andrii\lab_03\lab3.csv")

    fw.loadData(lst)

    while True:
        chouse = input("Please specify the action [ C create, U update, D delete, P print,  X exit ] ")

        match chouse:
            case "C" | "c":
                name = input("New name: ")
                phone = input("New phone: ")
                email = input("New email: ")
                group = input("New group: ")
                result_add = lst.add_student(Student(name, phone, email, group))
                if result_add:
                    print("Student added.")
                else:
                    print("Student already exists.")
                
            case "U" | "u":
                old_name = input("Old name: ")

                new_name = input("New name: ")
                new_phone = input("New phone: ")
                new_email = input("New email: ")
                new_group = input("New group: ")
                result_update = lst.update_student(old_name, Student(new_name, new_phone, new_email, new_group))
                if result_update:
                    print("Student updated!")
                else:
                    print("Student not found!")

            case "D" | "d":
                name = input("Name to delete: ")
                result_delete = lst.delete_student(name)
                if result_delete:
                    print("Student deleted!")
                else:
                    print("Student not found!")

            case "P" | "p":
                lst.print_all()

            case "X" | "x":
                fw.saveData(lst)
                print("Saved. Exiting.")
                break

            case _:
                print("Wrong choice!")


if __name__ == "__main__":
    main()
