
# Sorting the list before we loop through it

shopping_list = ["Tomatoes", "Bananas", "Crackers",
                 "Sugar", "Icecream", "Bread", "Bananas", "Chocolate"]

shopping_list.sort()

print("Shopping list in alphabetical order:")

for item in shopping_list:
    print(item)
