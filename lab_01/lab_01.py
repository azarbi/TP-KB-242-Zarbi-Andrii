
## List [Item1, Item2, Item3]
## Item {"name":"Jon", "phone":"0631234567"}

# already sorted list
list = [
    {"name":"Bob", "phone":"0631234567", "email":"bob@example.com", "group":"KB-243"},
    {"name":"Emma", "phone":"0631234567", "email":"emma@example.com", "group":"KB-243"},
    {"name":"Jon",  "phone":"0631234567", "email":"jon@example.com", "group":"KB-243"},
    {"name":"Zak",  "phone":"0631234567", "email":"zak@example.com", "group":"KB-243"}
]

def printAllList():
    for elem in list:
        strForPrint = "Student name is " + elem["name"] + ",  Phone is " + elem["phone"] + ", Email is " + elem["email"] + ", Group is " + elem["group"]
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
    for item in list:
     if name == item["name"]:
        deletePosition = list.index(item)
        break
    if deletePosition == -1:
        print("Element was not found")
    else:
         del list[deletePosition]

    name = input("Please enter new name: ")
    phone= input("Please enter new phone: ")
    email = input("Please enter new email: ")
    group = input("Please enter new group: ")    
    newItem = {"name": name, "phone": phone, "email": email, "group": group}

    insertPosition = 0
    for item in list:
     if name > item["name"]:
         insertPosition += 1
     else:
         break
    list.insert(insertPosition, newItem)
    print("Element was updated")
    return

def main():
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
                print("Exit()")
                break
            case _:
                print("Wrong chouse")


main()