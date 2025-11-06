from functions import add, subtract, multiply, divide

def getNumbers():
    a = int(input("Enter A: "))
    b = int(input("Enter B: "))
    return a, b

def choiceOperation(): 
    print("Choose an operation (1/2/3/4):")
    print("1) Addition (+): 1")
    print("2) Subtract (-): 2")
    print("3) Multiply (*): 3")
    print("4) Divide (/): 4")
    choice = int(input("Enter number of operation: "))
    return choice

def operationResult(a, b, choice):
    if(choice == 1):
        return add(a, b)
    
    elif(choice == 2):
        return subtract(a, b)
    
    elif(choice == 3):
        return multiply(a, b)
    
    elif(choice == 4):
        return divide(a, b)
    
    else:
        print("Incorrect operation.")