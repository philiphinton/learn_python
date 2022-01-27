
'''
So now we have a fully functioning calculator.
It has three parameters, only one of which (the first number) is required.
The second number defaults to 1, and the calculator performs addition by
default.
'''

# You can condense return statements into one line with the ternary operator;
# see https://syntaxdb.com/ref/python/ternary for more


def calculate(x: int, y: int = 1, *, subtract: bool = False) -> int:
    """Calculates the sum (or difference) of two numbers.

    Parameters:
    `x` : int, required
        The first number
    `y` : int, optional
        The second number (default is 1)
    `subtraction`: bool, optional
        Whether to perform subtraction. Default is False.
    """

    # if subtraction:
    #     return x - y
    # return x + y

    return x - y if subtraction else x + y

    # You could also do this:
    # if not subtraction:
    #     return x + y
    # return x - y


# Get two inputs from the user and cast them to integers
print("Enter a number:")
first = int(input())

print("Enter another number:")
second = int(input())

# Print the results of the two calculations
result = calculate(first, second)
print(f"The sum of {first} and {second} is {result}.")

result = calculate(first, second, subtract=True)
print(f"{first} minus {second} is {result}.")

# If you don't pass a second variable, the default value is used:
result = calculate(first, subtract=True)
print(f"{first} minus the default value is {result}.")
