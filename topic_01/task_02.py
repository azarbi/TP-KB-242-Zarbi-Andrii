s = "  Hello world" 
s1 = "python is the best"
def test():
    print("Strip: ", s.strip())
    print("Capitalize: ", s1.capitalize())
    print("Title: ", s1.title())
    print("Upper: ", s.upper())
    print("Lower: ", s.lower())
print("Original 'Hello world': ", s)
print("Original 'Python is the best': ", s1)
test()