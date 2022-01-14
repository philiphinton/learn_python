
<<<<<<< Updated upstream:functions/functions_03.py
# You can simplify the syntax within a function definition to
# straight away return the result.
# Note that on line 15 we re-use `result`.
=======
# You can simplify the syntax within a function definition to return the
# result straight away. Note that on line 16 we re-use the `result` variable.
# Compare this code with f2.py
# def add(x, y):
#     sum = x + y
#     return sum
>>>>>>> Stashed changes:04-functions/f3.py

def add(x, y):
    return x + y


def subtract(x, y):
    return x - y


result = add(10, 20)
print(f"The sum of 10 and 20 is {result}.")

# We can reuse variables but it is best not to - call it "result2" or somesuch.
result = subtract(10, 5)
print(f"10 minus 5 is {result}.")
