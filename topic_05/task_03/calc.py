from operations import getNumbers, choiceOperation, operationResult
from functions import add, subtract, multiply, divide

a, b = getNumbers()
choice = choiceOperation()
result = operationResult(a, b, choice)

print(f"Result: {result}")