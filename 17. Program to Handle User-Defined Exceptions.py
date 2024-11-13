class NegativeValueError(Exception):
    """Custom exception for negative values."""
    pass

def check_positive(number):
    if number < 0:
        raise NegativeValueError("Negative values are not allowed.")
    else:
        print("The number is positive.")

try:
    check_positive(-5)
except NegativeValueError as e:
    print(e)
