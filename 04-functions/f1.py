
# Let's make a calculator

# Function definitions start with the 'def' keyword,
# and are followed by two blank lines

# First example: addition-only
def add(x, y):
    sum = x + y
    return sum


result = add(10, 20)
print(f"The sum of 10 and 20 is {result}.")

# Generally speaking, because the interpreter reads files from top to bottom,
# calls to functions must come after their definitions.
# Which is to say, you wouldn't have been able to call add() on line 1.
