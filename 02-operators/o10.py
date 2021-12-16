
values = [1, 2, 3, 4, 5]

number = 0
statement = number not in values

# You can add "=" after a variable name inside curly braces to print out the
# variable name and its contents; see https://bugs.python.org/issue36817

print(f"It is {statement} that {number} is not in {values=}.")
# print(f"It is {statement} that {number=} is not in {values=}.")
# print(f"It is {statement=} that {number=} is not in {values=}.")
