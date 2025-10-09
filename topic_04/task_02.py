def getValues():
  while True:
    try:
      a = int(input("Enter A: "))
      b = int(input("Enter B: "))

      print("Choose an operation (1/2/3/4):")
      print("1) Addition (+): ")
      print("2) Subtract (-): ")
      print("3) Multiply (*): ")
      print("4) Divide (/): ")
      choice_of_operation = int(input("Enter number of operation: "))
      if choice_of_operation not in [1, 2, 3, 4]:
          print("Incorrect operation.")
          continue
      
      return a, b, choice_of_operation
    except ValueError:
      print("Error. Enter only numbers and try again.")  
    
def add (a, b):
  return a + b

def subtract (a, b):
  return a - b

def multiply (a, b):
  return a * b

def divide (a, b):
   try:
    a / b
   except ZeroDivisionError: 
     print("Error: division on zero.")
     return None

key = input("Enter 'Continue' to continue, or 'Stop' to stop: ")

while key == "Continue": 
   a, b, choice_of_operation = getValues()

   match choice_of_operation:
     case 1:
        print("Result: ", add(a, b))
     case 2:
        print("Result: ", subtract(a, b))
     case 3:
        print("Result: ", multiply(a, b))
     case 4:
        print("Result: ", divide(a, b))
     case _:
        print("Incorrect operation")

   key = input("Enter 'Continue' to continue, or 'Stop' to stop: ")
print("Calculator stopped.")