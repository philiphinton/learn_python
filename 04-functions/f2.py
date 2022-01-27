
# Two functions — one for addition, one for subtraction
author = "Phil"

def add(x, y):
    sum = x + y
    return sum


def subtract(x, y):
    diff = x - y
    return diff


num = 10
second_num = 20

result = add(10, 20)
print(f"The sum of 10 and 20 is {result}.")

result = add(num, second_num)
print(f"The sum of {num} and {second_num} is {result}.")

second_result = subtract(num, 5)
print(f"10 minus 5 is {second_result}.")

# Note that `sum` and `diff` are not accessible outside their functions
# Un-commenting the next line will raise a NameError
# print(diff)
print(author)
