my_list = [14, 15, 16, 88]
ins_el = int(input("Enter element to insert in list: "))

def find_position_to_insert(my_list, ins_el):
    for i in range(len(my_list)):
        if (ins_el <= my_list[i]):
            return i
    return len(my_list)

pos = find_position_to_insert(my_list, ins_el)

print("Position to insert: ", pos)