
# Import our module and rename it within this script
import calculator as calc

# Give its author some credit
print(f"Calculator, by {calc.author}.")
print("*" * 10)

# Everything from here down is identical to before, except the function calls

# Get two inputs from the user and cast them to integers
first = int(input("Enter a number: "))
second = int(input("Enter another number: "))

# Print the results of the two calculations
# The difference is we now have to say where the "calculate" function lives
result = calc.calculate(first, second)
print(f"The sum of {first} and {second} is {result}.")

result = calc.calculate(first, second, subtraction=True)
print(f"{first} minus {second} is {result}.")
