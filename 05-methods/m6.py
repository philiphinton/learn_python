
# This time, let's make it easier to call our function and author name:
from calculator import calculate as calc
from calculator import author

# Print program title and author name
print(f"Calculator, by {author}.")
print("*" * 10)

# Everything from here down is identical to previous exercises in the
# `functions` folder, except the names of the function calls themselves

# Get two inputs from the user and cast them to integers
first = int(input("Enter a number: "))
second = int(input("Enter another number: "))

result = calc(first, second)
print(f"The sum of {first} and {second} is {result}.")

result = calc(first, second, subtract=True)
print(f"{first} minus {second} is {result}.")

result = calc(first, subtract=True)
print(f"{first} minus the default value is {result}.")
