
# Using == for comparison, part two

x = 12
y = 8

statement = ((x + y) == 20)
print(f"It is {statement} that {x} plus {y} is 20.")

# Note that, again, the parentheses on line 7 don't need to be there;
# this works just as well (even though it may not so be clear to read)
statement = x + y == 20
print(f"It is {statement} that {x} plus {y} is 20.")
