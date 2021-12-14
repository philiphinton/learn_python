
# Comments are good, but docstrings (https://www.programiz.com/python-programming/docstrings)
# are better. Hover over the function calls on lines 22 and 25 to see them in action.

def add(x, y):
    """Takes two numbers and returns their sum."""

    return x + y


# Docstrings should be followed by a blank line.
def subtract(x, y):
    """Takes two numbers and returns their difference."""

    return x - y


# Get two inputs from the user and cast them to integers
print("Enter a number:")
first = int(input())

print("Enter another number:")
second = int(input())

# Print the results of the two calculations
result = add(first, second)
print(f"The sum of {first} and {second} is {result}.")

result = subtract(first, second)
print(f"{first} minus {second} is {result}.")
