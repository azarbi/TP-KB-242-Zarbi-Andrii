from functions import add, subtract, multiply, divide

class GetOperation:
    def __init__(self, choice):
        self.choice = int(choice)
    
    @property
    def choice(self):
        return self._choice
    
    @choice.setter
    def choice(self, choice):
        if not 1 <= choice <= 4:
            raise ValueError("Operation must be 1-4.")
        self._choice = choice
    
    def calculate(self, a, b):
        if self.choice == 1:
            return add(a, b)
        if self.choice == 2:
            return subtract(a, b)      
        if self.choice == 3:
            return multiply(a, b)      
        if self.choice == 4:
            return divide(a, b)

    def __str__(self):
        return f"Choice of operation: {self.choice}"
    
def getOperation():
    print("Choose an operation (1/2/3/4):")
    print("1) Addition (+): 1")
    print("2) Subtract (-): 2")
    print("3) Multiply (*): 3")
    print("4) Divide (/): 4")
    choice = input("Enter number of operation: ")
    return GetOperation(choice)
