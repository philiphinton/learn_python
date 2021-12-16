
# Finally, you can call a module anything you like within your program
from datetime import date as d8

today = d8.today()

long_format_date = today.strftime("%B %d, %Y")
print(f"Today is {long_format_date}.")
