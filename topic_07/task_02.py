class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author
    def __str__(self):
        return f"Book title: {self.title}; Author: {self.author}"
    
class Car:
    def __init__(self, brand, mark):
        self.brand = brand
        self.mark = mark
    def __str__(self):
        return f"Car brand: {self.brand}; Mark: {self.mark}"
def get_car():
    brand = input("Enter car brand: ")
    mark = input("Enter car mark: ")
    return Car(brand, mark)

def main():
    car = get_car()
    print(car)
    title = input("Enter book title: ")
    author = input("Enter book's author: ")
    book = Book(title, author)
    print(book)
    return book

main()