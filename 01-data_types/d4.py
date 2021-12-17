
# Accessing slices in strings
# See http://opensask.ca/Python/Strings/StringIntro.html#the-slice-operator

name = "Phil J Hinton"

# First four characters — exclusive of the fourth character
print(name[0:4])

# From character 5 to the end
print(name[5:])

# Start 6 characters back from the end, then go to the end
print(name[-6:])

# Start 6 characters back from the end, then stop two characters from the end
print(name[-6:-2])
