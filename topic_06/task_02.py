students = []

with open("topic_06/list.csv") as file:
    for line in file:
        name, score = line.rstrip().split(",")
        student = {"name": name, "score": score}
        students.append(student)

for elem in sorted(students, key=lambda student: student["name"]):
    print(f"Name = {elem['name']}  Score = {elem['score']}")