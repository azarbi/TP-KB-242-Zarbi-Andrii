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
     return f"Перший корінь: {x1}" \
     f" Другий корінь: {x2}"
    elif d == 0:
     x = -b/(2*a)
     return f"Рівняння має один корінь: {x}"
    elif d < 0:
     return "Рівняння не має розв'язку"
print(discr(a, b, c))
print(findx(a, b, c))