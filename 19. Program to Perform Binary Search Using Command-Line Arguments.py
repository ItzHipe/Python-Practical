import sys

def binary_search(arr, target):
    arr.sort()
    low, high = 0, len(arr) - 1
    while low <= high:
        mid = (low + high) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            low = mid + 1
        else:
            high = mid - 1
    return -1

if len(sys.argv) > 2:
    arr = list(map(int, sys.argv[1:-1]))
    target = int(sys.argv[-1])
    index = binary_search(arr, target)
    print(f"Element found at index {index}" if index != -1 else "Element not found")
else:
    print("Usage: python script.py <list of numbers> <target>")
