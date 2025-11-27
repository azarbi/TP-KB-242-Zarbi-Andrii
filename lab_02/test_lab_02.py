import lab_02
def test_add_student():
    #1 Test
    list = []
    lab_02.add_student(list, "Artem", "0631234567", "artem@example.com", "KB-243")

    assert list[0] ["name"] == "Artem" 
    assert list[0] ["phone"] == "0631234567" 
    assert list[0] ["email"] == "artem@example.com" 
    assert list[0] ["group"] == "KB-243" 

    #2 Test
    result = lab_02.add_student(list, "Artem", "0631234567", "artem@example.com", "KB-243")
    assert result is False
    assert list[0] ["name"] == "Artem"

    #3 Test
    lst = [{"name": "Dima", "phone": "0631234567", "email": "dima@example.com", "group": "KB-243"}, 
        {"name": "Sasha", "phone": "0631234567", "email": "sasha@example.com", "group": "KB-243"}]
    
    lab_02.add_student(lst, "Eddie", "0631234567", "eddie@example.com", "KB-243")

    assert lst[1] ["name"] == "Eddie" 
    assert lst[1] ["phone"] == "0631234567" 
    assert lst[1] ["email"] == "eddie@example.com" 
    assert lst[1] ["group"] == "KB-243" 

    #4 Test
    result_2 = lab_02.add_student(lst, "Dima", "0631234567", "dima@example.com", "KB-243")
    assert result_2 is False

def test_delete_student():
    #1 Test
    lst = [{"name": "Dima", "phone": "0631234567", "email": "dima@example.com", "group": "KB-243"}, 
           {"name": "Eddie", "phone": "0631234567", "email": "eddie@example.com", "group": "KB-243"},
           {"name": "Sasha", "phone": "0631234567", "email": "sasha@example.com", "group": "KB-243"}]
    
    result_1 = lab_02.delete_student(lst, "Dima")

    assert result_1 is True
    assert len(lst) == 2
    assert lst[0] ["name"] == "Eddie" 
    assert lst[1] ["name"] == "Sasha" 

    #2 Test
    result_2 = lab_02.delete_student(lst, "Andrii")
    assert result_2 is False
    assert len(lst) == 2
    assert lst[0] ["name"] == "Eddie" 
    assert lst[1] ["name"] == "Sasha" 

    #3 Test
    result_3 = lab_02.delete_student(lst, "Eddie")
    assert result_3 is True
    assert len(lst) == 1
    assert lst[0] ["name"] == "Sasha" 

def test_update_student():
    #1 Test
    lst = [{"name": "Dima", "phone": "0631234567", "email": "dima@example.com", "group": "KB-243"}, 
           {"name": "Eddie", "phone": "0631234567", "email": "eddie@example.com", "group": "KB-243"},
           {"name": "Sasha", "phone": "0631234567", "email": "sasha@example.com", "group": "KB-243"}]
    
    result_1 = lab_02.update_student(lst, "Dima", "Andrii", "0631234567", "andrii@example.com", "KB-242")

    assert result_1 is True
    assert lst[0] ["name"] == "Andrii" 
    assert lst[0] ["phone"] == "0631234567" 
    assert lst[0] ["email"] == "andrii@example.com" 
    assert lst[0] ["group"] == "KB-242" 

    #2 Test
    result_2 = lab_02.update_student(lst, "Artem", "Bob", "0631234567", "artem@example.com", "KB-243")
    assert result_2 is False
    assert len(lst) == 3
    assert lst[0] ["name"] == "Andrii" 
    assert lst[1] ["name"] == "Eddie" 
    assert lst[2] ["name"] == "Sasha" 

    #3 Test
    result_3 = lab_02.update_student(lst, "Eddie", "Zarzour", "0631234567", "zarzour@example.com", "KB-242")
    assert result_3 is True
    assert lst[0] ["name"] == "Andrii" 
    assert lst[1] ["name"] == "Sasha"
    assert lst[2] ["name"] == "Zarzour"

    assert lst[2]["phone"] == "0631234567"
    assert lst[2]["email"] == "zarzour@example.com"
    assert lst[2]["group"] == "KB-242" 

def test_loadData():
    from lab_02 import loadData
    csv_file = r"C:\Folder\TP-KB-242-Zarbi-Andrii\lab_02\lab2.csv"

    # 1 Test
    with open(csv_file, "w") as file:
        file.write("Name,Phone,Email,Group\n")
        file.write("Dima,0631234567,dima@example.com,KB-243\n")

    lst = []
    loadData(lst)
    assert len(lst) == 1
    assert lst[0]["name"] == "Dima"

    # 2 Test
    with open(csv_file, "w") as file:
        file.write("Name,Phone,Email,Group\n")
    lst = []
    loadData(lst)
    assert lst == []

    # 3 Test
    with open(csv_file, "w") as f:
        f.write("Name,Phone,Group\n")
        f.write("Eddie,0631234567,KB-243\n")
    lst = []
    try:
        loadData(lst)
        assert False, "loadData should give KeyError"
    except KeyError:
        assert True

def test_saveData():
    from lab_02 import saveData
    csv_file = r"C:\Folder\TP-KB-242-Zarbi-Andrii\lab_02\lab2.csv"

    # 1 Test
    data = [
        {"name": "Sasha", "phone": "0631234567", "email": "sasha@example.com", "group": "KB-243"}]

    saveData(data)
    with open(csv_file, "r") as file:
        lines = file.readlines()

    assert len(lines) == 2
    assert lines[1].strip() == "Sasha,0631234567,sasha@example.com,KB-243"

    # 2 Test
    saveData([])
    with open(csv_file, "r") as file:
        header = file.readline().strip()
    assert header == "Name,Phone,Email,Group"