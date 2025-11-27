import csv

def loadData(lst):
    with open (r"C:\Folder\TP-KB-242-Zarbi-Andrii\lab_02\lab2.csv") as file: 
        reader = csv.DictReader(file)
        for row in reader:
            lst.append({"name": row["Name"], "phone": row["Phone"], "email": row["Email"], "group": row["Group"]})

def saveData(lst):
    with open(r"C:\Folder\TP-KB-242-Zarbi-Andrii\lab_02\lab2.csv", "w") as file:
        fieldnames = ["Name", "Phone", "Email", "Group"]
        writer = csv.DictWriter(file, fieldnames=fieldnames)
        writer.writeheader()
        for row in lst:
            writer.writerow({"Name": row["name"], "Phone": row["phone"], "Email": row["email"], "Group": row["group"]})

#==========================================================================

def add_student(lst, name, phone, email, group):
    for item in lst:
        if item["name"] == name:
            return False
    
    newItem = {"name": name, "phone": phone, "email": email, "group": group}

    insertPosition = 0
    for item in lst:
        if name > item["name"]:
            insertPosition += 1
        else:
            break

    lst.insert(insertPosition, newItem)
    return True

def delete_student(lst, name):
    for i, item in enumerate(lst):
        if item["name"] == name:
            del lst[i]
            return True
    return False

def update_student(lst, old_name, new_name, new_phone, new_email, new_group):
    for i, item in enumerate(lst):
        if item["name"] == old_name:
            del lst[i]
            break
    else: 
        return False

    updated = {"name": new_name, "phone": new_phone, "email": new_email, "group": new_group}
    insertPosition = 0
    for el in lst:
        if updated["name"] > el["name"]:
            insertPosition += 1
        else:
            break
    lst.insert(insertPosition, updated)
    return True

#==========================================================================

def printAllList(lst):
    for elem in lst:
        strForPrint = "Student name is " + elem["name"] + ",  Phone is " + elem["phone"] + ", Email is " + elem["email"] + ", Group is " + elem["group"]
        print(strForPrint)
    return

def addNewElement(lst):
    name = input("Please enter student name: ")
    phone = input("Please enter student phone: ")
    email = input("Please enter student email: ")
    group = input("Please enter student group: ")
    newItem = {"name": name, "phone": phone, "email": email, "group": group}
    # find insert position
    insertPosition = 0
    for item in lst:
        if name > item["name"]:
            insertPosition += 1
        else:
            break
    lst.insert(insertPosition, newItem)
    print("New element has been added")
    return

def deleteElementlst(lst):
    name = input("Please enter name to be deleted: ")
    deletePosition = -1
    for item in lst:
        if name == item["name"]:
            deletePosition = lst.index(item)
            break
    if deletePosition == -1:
        print("Element was not found")
    else:
        print("Deleted position " + str(deletePosition))
        # list.pop(deletePosition)
        del lst[deletePosition]
    return


def updateElement(lst):
    # implementation required
    name = input("Please enter name to be updated: ")
    deletePosition = -1
    for item in lst:
        if name == item["name"]:
           deletePosition = lst.index(item)
           print("\nFound element:")
           print(f"Name: {item['name']}, Phone: {item['phone']}, Email: {item['email']}, Group: {item['group']}\n")
           break

    if deletePosition == -1:
        print("Element was not found")
        return

    del lst[deletePosition]

    new_name = input("Please enter new name: ")
    new_phone= input("Please enter new phone: ")
    new_email = input("Please enter new email: ")
    new_group = input("Please enter new group: ")
    updatedItem = {"name": new_name, "phone": new_phone, "email": new_email, "group": new_group}
            
    insertPosition = 0
    for item in lst:
        if updatedItem["name"] > item["name"]:
           insertPosition += 1
        else:
           break
    lst.insert(insertPosition, updatedItem)
    print("Element was updated")


def main():
    students = []
    loadData(students)

    while True:
        chouse = input("Please specify the action [ C create, U update, D delete, P print,  X exit ] ")
        match chouse:
            case "C" | "c":
                print("New element will be created:")
                addNewElement(students)
                printAllList(students)
            case "U" | "u":
                print("Existing element will be updated")
                updateElement(students)
            case "D" | "d":
                print("Element will be deleted")
                deleteElementlst(students)
            case "P" | "p":
                print("List will be printed")
                printAllList(students)
            case "X" | "x":
                print("Data saved and exit()")
                saveData(students)
                break
            case _:
                print("Wrong chouse")


if __name__ == "__main__":
    main()