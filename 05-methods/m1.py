
# Modules in Python are basically .py files — we've been making them all along.

# To import a module, use the "import" keyword at the top of your file:
import datetime

today = datetime.date.today()

long_format_date = today.strftime("%B %d, %Y")
print(f"Today is {long_format_date}.")
