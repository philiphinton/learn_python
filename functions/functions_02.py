
# Second version: two functions — one for addition, one for subtraction

def add(x, y):
    sum = x + y
    return sum


def subtract(x, y):
    diff = x - y
    return diff


result = add(10, 20)
print(f"The sum of 10 and 20 is {result}.")

second_result = subtract(10, 5)
print(f"10 minus 5 is {second_result}.")

# Note that `sum` and `diff` are not accessible outside their functions
