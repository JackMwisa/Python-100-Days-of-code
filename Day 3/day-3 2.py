def generate_catalog():
    items = {
        "Item 1": 200.0,
        "Item 2": 400.0,
        "Item 3": 600.0
    }

    catalog = []

    # Add individual items to the catalog
    catalog.extend(map(lambda x: (x[0], x[1]), items.items()))

    # Add combo packs with a 10% discount
    combos = [("Combo 1(Item 1 + 2)", ["Item 1", "Item 2"]),
              ("Combo 2(Item 2 + 3)", ["Item 2", "Item 3"]),
              ("Combo 3(Item 1 + 3)", ["Item 1", "Item 3"])]

    catalog.extend(map(lambda x: (x[0], sum(items[item] for item in x[1]) * 0.9), combos))

    # Add gift pack with a 25% discount
    gift_pack_items = ["Item 1", "Item 2", "Item 3"]
    gift_pack_price = sum(items[item] for item in gift_pack_items)
    catalog.append(("Gift Pack(Item 1 + 2 + 3)", gift_pack_price * 0.75))  # 25% discount

    # Generate the catalog output
    output = "Online store\n" + "-" * 27 + "\n"
    output += "{:<40} {:<10}\n".format("Product(s)", "Price")

    output += "\n".join(map(lambda x: "{:<40} {:<10.1f}".format(x[0], x[1]), catalog))

    output += "\n" + "_" * 27 + "\nFor delivery Contact:98764678899"
    
    print(output)

# Call the function to generate and print the catalog
generate_catalog()
