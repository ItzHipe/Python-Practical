n = int(input("Enter the position of the Fibonacci number to find: "))

if n <= 0:
    print("Please enter a positive integer")
elif n == 1:
    print("Fibonacci number at position 1 is 0")
else:
    a, b = 0, 1
    for _ in range(2, n):
        a, b = b, a + b
    print("Fibonacci number at position", n, "is", b)