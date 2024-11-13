# Creating sets
set_a = {1, 2, 3}
set_b = {3, 4, 5}

# Adding and removing elements
set_a.add(6)
set_a.discard(2)

# Union, intersection, and difference
union_set = set_a | set_b
intersection_set = set_a & set_b
difference_set = set_a - set_b

print("Union:", union_set)
print("Intersection:", intersection_set)
print("Difference:", difference_set)
