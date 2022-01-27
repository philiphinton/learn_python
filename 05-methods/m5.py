
# Import our module and rename it (within this script)
import calculator as calc

# Print program title and author name
print(f"\nCalculator, By {calc.author}.")
print(calc.__doc__)
print("*" * 10)

# Everything from here down is identical to previous exercises in the
# `functions` folder, except the names of the function calls themselves

# Get two inputs from the user and cast them to integers
first = int(input("Enter a number: "))
second = int(input("Enter another number: "))

result = calc.calculate(first, second)
print(f"The sum of {first} and {second} is {result}.")

result = calc.calculate(first, second, subtract=True)
print(f"{first} minus {second} is {result}.")

result = calc.calculate(first, subtract=True)
print(f"{first} minus the default value is {result}.")
