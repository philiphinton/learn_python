
# The oly difference between this version and version 9 is on line 18.

def calculate(x: int, y: int, *, subtraction: bool = False) -> int:
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
    return x + y

    # You could also do this:
    # if not subtraction:
    #     return x + y
    # return x - y


# Get two inputs from the user and cast them to integers
first = int(input("Enter a number: "))
second = int(input("Enter another number: "))

# Print the results of the two calculations
result = calculate(first, second)
print(f"The sum of {first} and {second} is {result}.")

result = calculate(first, second, subtraction=True)
print(f"{first} minus {second} is {result}.")
