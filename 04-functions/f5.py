
# Comments are good, but docstrings are better.
# Hover over the function calls on lines 18 and 21 to see them in action.

def add(x, y):
    """Takes two numbers and returns their sum."""

    return x + y


# Docstrings should be followed by a blank line.
def subtract(x, y):
    """Takes two numbers and returns their difference."""

    return x - y


result = add(10, 20)
print(f"The sum of 10 and 20 is {result}.")

result = subtract(10, 5)
print(f"10 minus 5 is {result}.")
