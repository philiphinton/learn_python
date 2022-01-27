
from supermarket import shopping_list

list_by_aisle = sorted(shopping_list, key=lambda item: item.aisle)

print("To go through the supermaket efficiently, you should buy things in this order: ", end="")

# Create a boolean to check if we're at the last item in the (zero-indexed) list
list_length = len(list_by_aisle) - 1

for position, item in enumerate(list_by_aisle):

    # Print out the item name (in lowercase) with no new line
    print(item.name.lower(), end="")

    # If we're not at the end, print a semicolon and a space, also with no new line
    if not position == list_length:
        print("; ", end="")

print(".")

# ### Things to play with to replace lines 11 to 20
# # for pos, item in enumerate(list_by_aisle, start=1):
# #     print(f"{pos}. {item.name}")

# counter = 1
# for item in list_by_aisle:
#     print(f"{counter}. {item.name}")
#     counter += 1  # same as counter = counter + 1
