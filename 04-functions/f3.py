
# You can simplify the syntax within a function definition to return the
# result straight away. Note that before the second print call,
# we re-use the `result` variable.

def add(x, y):
    return x + y


def subtract(x, y):
    return x - y


result = add(10, 20)
print(f"The sum of 10 and 20 is {result}.")

result = subtract(10, 5)
print(f"10 minus 5 is {result}.")
