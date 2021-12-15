
# Let's get input from the user instead of hardcoding numbers into the
# function call. and add some comments explaining what we're doing.

# Define two functions; one to perform additon, and another, subtraction
def add(x, y):
    return x + y


def subtract(x, y):
    return x - y


# Single-line comments, like this one, start with a `#` (hashmark/'pound' sign)
# Multi-line ones are wrapped in three `'` (straight apostrophes), like so:

'''
Get two inputs from the user and cast them to integers.
This is because the built-in input() method returns a string by default.

You could also do the casting within the functions themselves,
but doing it just once, at the time of capture, is probably more efficient.
'''
first = int(input("Enter a number: "))
second = int(input("Enter another number: "))

# Print the results of the two calculations
result = add(first, second)
print(f"The sum of {first} and {second} is {result}.")

result = subtract(first, second)
print(f"{first} minus {second} is {result}.")
