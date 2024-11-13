def greet(name, message="Hello"):
    """Function with default argument."""
    print(f"{message}, {name}!")

def add(*args):
    """Function with variable-length arguments."""
    return sum(args)

def person_info(name, **kwargs):
    """Function with keyword arguments."""
    print(f"Name: {name}")
    for key, value in kwargs.items():
        print(f"{key}: {value}")

# Function calls
greet("Alice")
greet("Bob", "Welcome")
print("Sum:", add(1, 2, 3, 4, 5))
person_info("Charlie", age=30, location="New York")
