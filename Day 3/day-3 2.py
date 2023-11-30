def calculate_price(items, item_prices, combo_discount=0.1, gift_pack_discount=0.25):
    """Calculates the total price for a customer's purchase, taking into account any discounts for combo packs or gift packs.

    Args:
        items (list): A list of the items the customer is purchasing.
        item_prices (dict): A dictionary of item names to prices.
        combo_discount (float): The discount rate for combo packs (default: 0.1).
        gift_pack_discount (float): The discount rate for gift packs (default: 0.25).

    Returns:
        float: The total price for the customer's purchase.
    """

    total_price = 0
    for item in items:
        total_price += item_prices[item]

    # Check if the customer is purchasing a combo pack.
    if len(items) == 2 and items != ["Item 1", "Item 3"]:
        total_price *= (1 - combo_discount)

    # Check if the customer is purchasing a gift pack.
    if len(items) == 3:
        total_price *= (1 - gift_pack_discount)

    return total_price


item_prices = {
    "Item 1": 200.0,
    "Item 2": 150.0,
    "Item 3": 300.0,
    "Combo 1(Item 1 + 2)": 320.0,
    "Gift Pack": 825.0
}

# Calculate the total price for a customer who purchases Item 1 and Item 2.
items = ["Item 1", "Item 2"]
total_price = calculate_price(items, item_prices)
print(f"Total price for Item 1 and Item 2: {total_price}")

# Calculate the total price for a customer who purchases the gift pack of all three items.
items = ["Item 1", "Item 2", "Item 3"]
total_price = calculate_price(items, item_prices)
print(f"Total price for the gift pack of all three items: {total_price}")
