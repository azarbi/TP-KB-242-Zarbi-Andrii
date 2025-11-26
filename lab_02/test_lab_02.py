import csv
import lab_02

def test_addNewElement():
    lst = []
    lab_02.addNewElement(lst, "Bob", "111", "b@x.com", "KB-242")

    assert len(lst) == 1
    assert lst[0]["name"] == "Bob"
    assert lst[0]["phone"] == "111"


def test_deleteElement():
    lst = [{"name": "Bob", "phone": "111", "email": "b@x.com", "group": "G"}]

    result = lab_02.deleteElement(lst, "Bob")

    assert result is True
    assert lst == []


def test_updateElement():
    lst = [{"name": "Bob", "phone": "111", "email": "b@x.com", "group": "G"}]

    result = lab_02.updateElement(lst, "Bob", "Emma", "222", "e@x.com", "G2")

    assert result is True
    assert lst[0]["name"] == "Emma"
    assert lst[0]["phone"] == "222"
    assert lst[0]["group"] == "G2"


def test_loadData(tmp_path):
    csv_path = test_lab2.csv
    csv_path.write_text(
        "Name,Phone,Email,Group\n"
        "Bob,111,b@x.com,G\n"
        "Emma,222,e@x.com,G2\n"
    )

    lst = []
    lab_02.loadData(lst, csv_path)

    assert len(lst) == 2
    assert lst[0]["name"] == "Bob"
    assert lst[1]["phone"] == "222"


def test_saveData():
    lst = [
        {"name": "Bob", "phone": "111", "email": "b@x.com", "group": "G"},
        {"name": "Emma", "phone": "222", "email": "e@x.com", "group": "G2"},
    ]

    csv_path = test_lab_02.csv
    lab_02.saveData(lst, csv_path)

    with open(csv_path) as f:
        reader = csv.DictReader(f)
        rows = list(reader)

    assert rows[0]["Name"] == "Bob"
    assert rows[1]["Phone"] == "222"