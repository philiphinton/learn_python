
# This time let's not use a string for the operation parameter.
# Since it's an either-or choice, a Boolean will do nicely.

# For an explanation of the use of the "*" in the definition block, see
# https://ivergara.github.io/boolean-arguments-to-functions-in-python.html

<<<<<<< Updated upstream:functions/functions_09.py
def calculate(x: int, y: int, *, subtraction: bool = False):
=======
def calculate(x: int, y: int = 1, *, subtraction: bool = False) -> int:
>>>>>>> Stashed changes:04-functions/f9.py
    """Calculates the sum (or difference) of two numbers.

    Parameters:
    `x` : int
        The first number
    `y` : int, optional
        The second number (default is 1)
    `subtraction`: bool, optional
        Whether to perform subtraction. Default is False.
    """

    if subtraction:
        return x - y
    else:
    return x + y

<<<<<<< Updated upstream:functions/functions_09.py
=======
    # You could also do this (note that you do not actually need 'else':'):
    # if not subtraction:
    #     return x + y
    # return x - y

>>>>>>> Stashed changes:04-functions/f9.py

# Get two inputs from the user and cast them to integers
print("Enter a number:")
first = int(input())

print("Enter another number:")
second = int(input())

# Print the results of the two calculations
result = calculate(first, second)
print(f"The sum of {first} and {second} is {result}.")

result = calculate(first, second, subtraction=True)
print(f"{first} minus {second} is {result}.")
