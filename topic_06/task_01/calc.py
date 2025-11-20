from operations import getNumbers, choiceOperation, operationResult

def saveData(a, b, choice, result):
    with open("log.txt", "a") as file:
        file.write(f"First number: {a} \nSecond number: {b} \nOperation (1 (+); 2  (-); 3 (*); 4 (/)): {choice} \nResult: {result} \n====================================\n")

a, b = getNumbers()

choice = choiceOperation()
result = operationResult(a, b, choice)

print(f"Result: {result}")

saveData(a, b, choice, result)