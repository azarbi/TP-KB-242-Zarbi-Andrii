my_list = ['a', 14, 15, 16, 'cat', 88]
print("Initial my_list: ", my_list)

my_list.extend([7, 8, 9]) 
print("Extended my_list: ", my_list)

my_list.append(10) 
print("Appended my_list: ", my_list)

my_list.insert(0, 'who')
print("Inserted my_list: ", my_list)

my_list.remove('a')
print("Removed my_list: ", my_list)

my_list.sort(key=str)
print("Sorted my_list: ", my_list)

my_list.reverse()
print("Reversed my_list: ", my_list)

my_copied_list = my_list.copy()
print("Copied my_list: ", my_copied_list)

my_list.clear() 
print("Cleared my_list: ", my_list)