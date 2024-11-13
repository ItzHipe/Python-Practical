for num in range(1,1001):
    length = len(str(num))
    sum_of_powers = sum([int(num) ** length for num in str(num)])
    if sum_of_powers == num:
        print(num)