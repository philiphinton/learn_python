
# In the previous exercise, we imported the entire datetime module, but used
# only one function from it ("datetime.date").

# You can specfiy module classes in import statements:
from datetime import date

# This way, you don't need the longer syntax of the module name in the call:
today = date.today()

long_format_date = today.strftime("%B %d, %Y")
print(f"Today is {long_format_date}.")
