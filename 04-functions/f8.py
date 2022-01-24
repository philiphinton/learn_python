
# Wrap the operations into one function, now named `calculate`,
# with a mandatory "operation" parameter.

def calculate(x: int, y: int = 1, operation: str = None) -> int:
    """Calculates the sum (or difference) of two numbers.

    Parameters:
    `x` : int
        The first number
    `y` : int, optional
        The second number (default is `1`)
    `operation`: str, optional
        Pass "subtract" to perform subtraction (default is `None`)

    Returns:
        int
    """

    if operation == "subtract":
        return x - y
    else:
        return x + y


# Get two inputs from the user and cast them to integers
first = int(input("Enter a number: "))
second = int(input("Enter another number: "))

# Print the results of the two calculations
result = calculate(first, second)
print(f"The sum of {first} and {second} is {result}.")

result = calculate(first, second, operation="subtract")
print(f"{first} minus {second} is {result}.")

# If you don't pass a second variable, the default value is used.
# There are now three parameters, so you have to name the 'operation' one:
result = calculate(first, operation="subtract")
print(f"{first} minus the default value is {result}.")

# In other words, this would not have worked:
# result = calculate(first, "subtract")
# because the function would have treated "subtract" as the second number (y)
