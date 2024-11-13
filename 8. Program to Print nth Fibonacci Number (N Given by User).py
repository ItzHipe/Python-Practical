def fibonacci(n):
    if n <= 1:
        return n
    else:
        return fibonacci(n-1) + fibonacci(n-2)

n = int(input("Enter the position of the Fibonacci number to find: "))
print("Fibonacci number at position", n, "is", fibonacci(n))
