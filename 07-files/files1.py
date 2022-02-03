
# To read and write a file, you have to open a file handler using the built-in
# `open()` function. Its only required argument is the path to the file.

# We've used "f"-strings before to incorporate variable values, but now we
# need to use an "r"-string: https://www.journaldev.com/23598/python-raw-string
# They take backslashes literally — very important in Windows file/dir paths.

# This may need to be altered for use on Windows
filepath = r'07-files/shopping_list.csv'

file = open(filepath)

# File objects (such as those returned by `open()`) are effectively a list:
for line in file:
    print(line, end='')

file.close()
