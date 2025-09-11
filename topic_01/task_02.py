s = "  Hello world" 
s1 = "python is the best"
s2 = "PYTHON"
def test():
    print("Strip: ", s.strip())
    print("Capitalize: ", s1.capitalize())
    print("Title: ", s1.title())
    print("Upper: ", s.upper())
    print("Lower: ", s2.lower())
print("Original 'Hello world': ", s)
print("Original 'Python is the best': ", s1)
print("Original 'Python': ", s2)
test()