
# You can provide what are called "type hints" within function definitions.
# These dictate what the function will accept, and what it will return.
# So far we haven't specified any of this, and it was possible to
# pass non-integers as input!

def add(x: int, y: int = 0) -> int:
    """Takes two numbers and returns their sum.

    Second number optional; defaults to `0`.
    """

    return x + y


# Docstrings that define functions are often laid out like this, with a block in
# which parameter types, optionality, and defaults (if any), are explained.


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
<<<<<<< Updated upstream:functions/functions_07.py
print("Enter a number:")
first = int(input())

print("Enter another number:")
second = int(input())
=======
# first = int(input("Enter a number: "))
# second = int(input("Enter another number: "))

first = 20
# second = 10
second = "the default value"

>>>>>>> Stashed changes:04-functions/f7.py

# Print the results of the two calculations
result = add(first)
print(f"The sum of {first} and {second} is {result}.")

result = subtract(first)
print(f"{first} minus {second} is {result}.")
