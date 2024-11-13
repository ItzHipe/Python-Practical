# Creating a dictionary
my_dict = {'a': 1, 'b': 2, 'c': 3}

# Adding and updating elements
my_dict['d'] = 4
my_dict.update({'e': 5})

# Removing elements
del my_dict['a']
popped_value = my_dict.pop('b', None)

# Accessing elements
value_c = my_dict.get('c', 'Not Found')

# Iterating over dictionary
for key, value in my_dict.items():
    print(key, value)

print("Final dictionary:", my_dict)
print("Value of 'c':", value_c)
