def discr(a, b, c):
    return b * b - 4 * a * c
a = int(input("Enter a: "))
b = int(input("Enter b: "))
c = int(input("Enter c: "))
def findx(a, b, c):
    d = discr(a, b, c)
    if d > 0:
     x1 = (-b + d**(0.5))/(2*a)
     x2 = (-b - d**(0.5))/(2*a)
     return f"First x: {x1}" \
     f" Second x: {x2}"
    elif d == 0:
     x = -b/(2*a)
     return f"Equation has one x: {x}"
    elif d < 0:
     return "Equation has no solution"
print("Discriminant: ", discr(a, b, c))
print("Solution for equation: ", findx(a, b, c))