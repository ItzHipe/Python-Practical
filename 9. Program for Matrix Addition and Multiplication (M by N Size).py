import numpy as np
import random

M = int(input("Enter number of rows: "))
N = int(input("Enter number of columns: "))

# Generating two random matrices
matrix1 = np.random.randint(1, 10, size=(M, N))
matrix2 = np.random.randint(1, 10, size=(M, N))

# Matrix addition
addition_result = matrix1 + matrix2

# Matrix multiplication
multiplication_result = np.dot(matrix1, matrix2.T)

print("Matrix 1:\n", matrix1)
print("Matrix 2:\n", matrix2)
print("Addition:\n", addition_result)
print("Multiplication:\n", multiplication_result)