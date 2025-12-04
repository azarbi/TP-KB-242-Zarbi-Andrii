from operations import getOperation
from operations import GetOperation

class GetNumbers:
    def __init__(self, a, b):
        self.a = float(a)
        self.b = float(b)

    def __str__(self):
        return f"A: {self.a}, B: {self.b}"
    
def getNumbers():
    a = input("Enter A: ")
    b = input("Enter B: ")
    return GetNumbers(a, b)

def main():
    numbers = getNumbers()
    operation = getOperation()
    result = operation.calculate(numbers.a, numbers.b)
    print(f"Result: {result}")

main()