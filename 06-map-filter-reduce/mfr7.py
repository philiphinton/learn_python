
from supermarket import shopping_list

items_on_special = list(
    filter(
        lambda item: item.on_special,
        shopping_list)
)

print("On special this week:")
for item in items_on_special:
    print(f"{item.brand} {item.name.lower()} (${item.price:.2f} / {item.price_measure})")
