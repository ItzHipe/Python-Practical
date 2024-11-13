# Creating a list
my_list = [1, 2, 3, 4, 5]

# Adding elements
my_list.append(6)
my_list.insert(2, 7)  # insert at position 2

# Removing elements
my_list.remove(7)
popped_element = my_list.pop()  # removes the last item

# Sorting and reversing
my_list.sort()
my_list.reverse()

# Accessing elements
first_element = my_list[0]
last_element = my_list[-1]

# Slicing
sub_list = my_list[1:4]

print("Final list:", my_list)
print("First element:", first_element)
print("Last element:", last_element)
print("Sliced list:", sub_list)