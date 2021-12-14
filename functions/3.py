
# You can simplify the syntax within a function definition to
# straight away return the result.
# Note that on line 15 we re-use `result`.

def add(x, y):
    return x + y


def subtract(x, y):
    return x - y


result = add(10, 20)
print(f"The sum of 10 and 20 is {result}.")

result = subtract(10, 5)
print(f"10 minus 5 is {result}.")
