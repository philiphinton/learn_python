
# There is another kind of object we haven't looked at yet: the "set"
# Sets contain only unique values, so you can loop through a list that
# contains duplicates (like two "Bananas" here) and arrive at unique values

shopping_list = ["Tomatoes", "Bananas", "Crackers",
                 "Sugar", "Icecream", "Bread", "Bananas", "Chocolate"]

unique_shopping_list = set()

for item in shopping_list:
    unique_shopping_list.add(item)

print(unique_shopping_list)
