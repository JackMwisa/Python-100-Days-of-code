def calculate_price(items, item_prices, combo_discounts=None, gift_pack_discount=0.25):
    if not items:
        return 0

    head, *tail = items
    price = item_prices[head]

    if not tail:
        return price

    combo_pack_discount = combo_discounts.get(
        f"Combo 1(Item 1 + 2)" if head == "Item 2" and tail[0] == "Item 1" else None
    )
    if combo_pack_discount is not None:
        price *= (1 - combo_pack_discount)

    return price + calculate_price(tail, item_prices, combo_discounts, gift_pack_discount)


# Example usage
item_prices = {
    "Item 1": 200.0,
    "Item 2": 150.0,
    "Item 3": 300.0,
    "Combo 1(Item 1 + 2)": 320.0,
    "Gift Pack": 825.0,
}

combo_discounts = {
    "Combo 1(Item 1 + 2)": 0.15,
    "Combo 2(Item 1 + 3)": 0.20,
}

# Calculate total price for Item 1 and Item 2 with default combo discount
items = ["Item 1", "Item 2"]
total_price = calculate_price(items, item_prices, combo_discounts)
print(f"Total price for Item 1 and Item 2 with default combo discount: {total_price}")

# Calculate total price for Item 1 and Item 2 with custom combo discount
items = ["Item 1", "Item 2"]
total_price = calculate_price(items, item_prices, combo_discounts={"Combo 1(Item 1 + 2)": 0.25})
print(f"Total price for Item 1 and Item 2 with custom combo discount: {total_price}")
