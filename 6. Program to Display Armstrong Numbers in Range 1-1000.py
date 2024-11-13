for num in range(1, 1001):
    order = len(str(num))
    sum = sum(int(digit) ** order for digit in str(num))
    if sum == num:
        print(num, "is an Armstrong number.")
