
# In the previous exercise, we imported the whole datetime module, but only
# used the "date" part of it. You can be more specific in the import statement:
from datetime import date

# Then you don't need the longer syntax of the module name before the class
today = date.today()

long_format_date = today.strftime("%B %d, %Y")
print(f"Today is {long_format_date}.")
