students = []

with open("topic_06/list.csv") as file:
    for line in file:
        name, mark = line.rstrip().split(",")
        student = {"name": name, "mark": mark}
        students.append(student)

for elem in sorted(students, key=lambda student: student["name"]):
    print(f"Name = {elem['name']}  mark = {elem['mark']}")