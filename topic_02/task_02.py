def add (a, b):
    return a + b

def subtract (a, b):
    return a - b

def multiply (a, b):
    return a * b

def divide (a, b):
    if(b == 0):
        print("Error")
    else:
        return a / b
    
a = int(input("Enter A: "))
b = int(input("Enter B: "))
print("Choose an operation (1/2/3/4):")
print("1) Addition (+): 1")
print("2) Subtract (-): 2")
print("3) Multiply (*): 3")
print("4) Divide (/): 4")
choice_of_operation = int(input("Enter number of operation: "))

if (choice_of_operation == 1):
    print("Result of addition: ", add(a, b))
elif (choice_of_operation == 2):
    print("Result of subtract: ", subtract(a, b))
elif (choice_of_operation == 3):
    print("Result of multiply:", multiply(a, b))
elif (choice_of_operation == 4):
    print("Result of divide: ", divide(a, b))
else:
    print("Incorrect operation.")