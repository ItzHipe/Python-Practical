try:
    num = int(input("Enter a number: "))
    result = 10 / num
    print("Result:", result)
    
    my_list = [1, 2, 3]
    print(my_list[5])

except ValueError:
    print("Invalid input! Please enter a number.")
except ZeroDivisionError:
    print("Cannot divide by zero!")
except IndexError:
    print("Index out of range!")
