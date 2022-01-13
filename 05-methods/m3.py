
# Finally, you can call a module anything you like within your program
from datetime import date as get_date

today = get_date.today()

long_format_date = today.strftime("%B %d, %Y")
print(f"Today is {long_format_date}.")
