
"""
The arguments we've used so far are positional. Whatever is passed into
the function is used in that order. You can set default values if none
is passed. Positional arguments must precede default arguments.

Docstrings can be single-line, or multi-line. The former can be wrapped in
three single-quote marks, but the latter must be wrapped in three
double-quote marks.

The first line of a docstring is a summary, and should be followed by
a blank line - this roughly equates to a carriage-return [PH].
"""


def add(x, y=5):
    """Takes two numbers and returns their sum.
    
    Second number optional; defaults to `0`.
    This is a third line.
    """

    return x + y


def subtract(x, y=1):
    """Takes two numbers and returns their difference.

    Second number optional; defaults to `1`.
    """

    return x - y


# Get two inputs from the user and cast them to integers
print("Enter a number:")
first = int(input())

print("Enter another number:")
second = int(input())

# Print the results of the two calculations
result = add(first, second)
print(f"The sum of {first} and {second} is {result}.")

#If you don't pass a second variable, the default value is used:
result = subtract(first)
print(f"{first} minus the default value (1) is {result}.")

result = add(first)
print(f"The sum of {first} and the default is {result}.")
