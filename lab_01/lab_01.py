
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
            new_name = input("Please enter new name (leave empty to keep current): ")
            new_phone= input("Please enter new phone (leave empty to keep current): ")
            new_email = input("Please enter new email (leave empty to keep current): ")
            new_group = input("Please enter new group (leave empty to keep current): ")
            
            if new_name:
                item["name"] = new_name
            if new_phone:
                item["phone"] = new_phone
            if new_email:
                item["email"] = new_email  
            if new_group:
                item["group"] = new_group
            list.sort(key=lambda x: x["name"])    
            print("Element was updated")          
            return
    print("Item wasnot found in list")

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