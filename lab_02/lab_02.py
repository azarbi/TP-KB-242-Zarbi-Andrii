import csv

list = []

def loadData(list):
    with open (r"C:\Folder\TP-KB-242-Zarbi-Andrii\lab_02\lab2.csv") as file: 
        reader = csv.DictReader(file)
        for row in reader:
            list.append({"name": row["Name"], "phone": row["Phone"], "email": row["Email"], "group": row["Group"]})

def saveData(list):
    with open(r"C:\Folder\TP-KB-242-Zarbi-Andrii\lab_02\lab2.csv", "w") as file:
        fieldnames = ["Name", "Phone", "Email", "Group"]
        writer = csv.DictWriter(file, fieldnames=fieldnames)
        writer.writeheader()
        for row in list:
            writer.writerow({"Name": row["name"], "Phone": row["phone"], "Email": row["email"], "Group": row["group"]})

def printAllList():
    for elem in list:
        strForPrint = (f"Student name is {elem['name']}, Phone is {elem['phone']}, Email is {elem['email']}, Group is {elem['group']}")
        print(strForPrint)
    return

def addNewElement():
    name = input("Please enter student name: ")
    phone = input("Please enter student phone: ")
    email = input("Please enter student email: ")
    group = input("Please enter student group: ")
    newItem = {"name": name, "phone": phone, "email": email, "group": group}
    # find insert position
    insertPosition = 0
    for item in list:
        if name > item["name"]:
            insertPosition += 1
        else:
            break
    list.insert(insertPosition, newItem)
    print("New element has been added")
    return

def deleteElement():
    name = input("Please enter name to be deleted: ")
    deletePosition = -1
    for item in list:
        if name == item["name"]:
            deletePosition = list.index(item)
            break
    if deletePosition == -1:
        print("Element was not found")
    else:
        print("Deleted position " + str(deletePosition))
        # list.pop(deletePosition)
        del list[deletePosition]
    return


def updateElement():
    # implementation required
    name = input("Please enter name to be updated: ")
    deletePosition = -1
    for item in list:
        if name == item["name"]:
           deletePosition = list.index(item)
           print("\nFound element:")
           print(f"Name: {item['name']}, Phone: {item['phone']}, Email: {item['email']}, Group: {item['group']}\n")
           break

    if deletePosition == -1:
        print("Element was not found")
        return

    del list[deletePosition]

    new_name = input("Please enter new name: ")
    new_phone= input("Please enter new phone: ")
    new_email = input("Please enter new email: ")
    new_group = input("Please enter new group: ")
    updatedItem = {"name": new_name, "phone": new_phone, "email": new_email, "group": new_group}
            
    insertPosition = 0
    for item in list:
        if updatedItem["name"] > item["name"]:
           insertPosition += 1
        else:
           break
    list.insert(insertPosition, updatedItem)
    print("Element was updated")

def main():
    loadData(list)

    while True:
        chouse = input("Please specify the action [ C create, U update, D delete, P print,  X exit ] ")
        match chouse:
            case "C" | "c":
                print("New element will be created:")
                addNewElement()
                printAllList()
            case "U" | "u":
                print("Existing element will be updated")
                updateElement()
            case "D" | "d":
                print("Element will be deleted")
                deleteElement()
            case "P" | "p":
                print("List will be printed")
                printAllList()
            case "X" | "x":
                print("Data saved and exit()")
                saveData(list)
                break
            case _:
                print("Wrong chouse")


main()