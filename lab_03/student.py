class Student:
    def __init__(self, name, phone, email, group):
        self.name = name
        self.phone = phone
        self.email = email
        self.group = group
    def __str__(self):
        return f"Name: {self.name}, Phone: {self.phone}, Email: {self.email}, Group: {self.group}"