my_dict = {
    "name": "Andrii",
    "age": 19,
    "city": "Chernihiv",
    "country": "Ukraine"
}
print("Initial my_dict: ", my_dict)
    
my_dict.update({"city": "Kyiv", "age": 25, "surname": "Zarbi"})
print("Updated dictionary: ", my_dict)

del my_dict['city']
print("After del(): ", my_dict)

print("Keys: ", my_dict.keys())

print("Values: ", my_dict.values())

print("Items: ", my_dict.items())

my_dict.clear() 
print("Clear: ", my_dict)