
shopping_list = ["Tomatoes", "Bananas", "Crackers",
                 "Sugar", "Icecream", "Bread", "Bananas", "Chocolate"]
print(shopping_list)

# This time let's have our function return the value of matching elements
mapped = map(lambda item: item if item[0] == "B" else None, shopping_list)

print(list(mapped))
