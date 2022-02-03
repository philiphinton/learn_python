
# To read and write a file, you have to open a file handler, with the built-in
# `open()` function. Its only required argument is the path to the file.

# We've used "f"-strings before to incorporate variable values, but now we
# need to use an "r"-string: https://www.journaldev.com/23598/python-raw-string
# They take backslashes literally — very important in Windows file/dir paths.

filepath = r'07-files/shopping_list.csv'

file = open(filepath)

for line in file:
    print(line, end="")

file.close()
