import random

numbers = random.sample(range(1, 100), 20)
print("List:", numbers)
target = int(input("Enter a number to search for: "))

found = target in numbers
if found:
    print("Number found at position", numbers.index(target))
else:
    print("Number not found")