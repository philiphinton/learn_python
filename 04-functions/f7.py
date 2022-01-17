
# You can provide what are called "type hints" within function definitions.
# These dictate what the function will accept, and what it will return.
# So far we haven't specified any of this, and it was possible to
# pass non-integers as input! 😱

from re import S


def add(x: int, y: int = 0) -> int:
    """Takes two numbers and returns their sum.

    Second number optional; defaults to `0`.
    """

    return x + y


# Docstrings that define functions are often laid out with a block
# in which parameter types, optionality, and defaults are explained.


def subtract(x: int, y: int = 1) -> int:
    """Takes two numbers and returns their difference.

    Parameters:
    `x` : int
        The first number
    `y` : int, optional
        The second number (default is `1`)
    """

    return x - y


# Get two inputs from the user and cast them to integers
first = int(input("Enter a number: "))
second = int(input("Enter another number: "))

# Print the results of the two calculations
result = add(first, second)
print(f"The sum of {first} and {second} is {result}.")

result = subtract(first, second)
print(f"{first} minus {second} is {result}.")

# If you don't pass a second variable, the default value is used:
result = subtract(first)
print(f"{first} minus the default value is {result}.")
