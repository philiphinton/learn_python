
# Comments are good, but docstrings are better.
# Hover over the function calls on lines 23 and 26 to see them in action.

def add(x, y):
    """Takes two numbers and returns their sum."""

    return x + y


# Docstrings should be followed by a blank line.
def subtract(x, y):
    """Takes two numbers and returns their difference."""

    return x - y


# Get two inputs from the user and cast them to integers
first = int(input("Enter a number: "))
second = int(input("Enter another number: "))

# Print the results of the two calculations
result = add(first, second)
print(f"The sum of {first} and {second} is {result}.")

result = subtract(first, second)
print(f"{first} minus {second} is {result}.")
