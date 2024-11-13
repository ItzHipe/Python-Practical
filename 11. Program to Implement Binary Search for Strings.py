def binary_search(arr, x):
    low, high = 0, len(arr) - 1
    while low <= high:
        mid = (low + high) // 2
        if arr[mid] == x:
            return mid
        elif arr[mid] < x:
            low = mid + 1
        else:
            high = mid - 1
    return -1

# Sorted list of strings
arr = sorted(["apple", "banana", "cherry", "date", "fig", "grape"])
x = input("Enter the string to search: ")
index = binary_search(arr, x)

print("Found" if index != -1 else "Not found")
