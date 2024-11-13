import random

numbers = random.sample(range(1, 100), 20)
target = int(input("Enter a number to search for: "))

found = target in numbers
print("List:", numbers)
print(f"{'Found' if found else 'Not found'} the target {target}")
