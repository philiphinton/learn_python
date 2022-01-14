
<<<<<<< Updated upstream:functions/functions_10.py
# There are two differences between this version and version 9.
# Line 18 is only be executed when `subtraction` is False.
=======
# The only difference between this version and version 9 is on line 18 where 'else:' has been removed.
>>>>>>> Stashed changes:04-functions/f10.py

def calculate(x: int, y: int, *, subtraction: bool = False):
    """Calculates the sum (or difference) of two numbers.

    Parameters:
    `x` : int
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

result = calculate(first, second, subtraction=True)
print(f"{first} minus {second} is {result}.")
