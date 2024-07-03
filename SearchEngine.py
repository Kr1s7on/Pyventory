# Author: Jesalva Kriston Jomari Ballesteros
# Admin No / Grp: 231165R / AA2402

"""
┌───────────────────────────────────────────────────┐
│                                                   │
│  ____                        _                    │
│ |  _ \ _   ___   _____ _ __ | |_ ___  _ __ _   _  │
│ | |_) | | | \ \ / / _ \ '_ \| __/ _ \| '__| | | | │
│ |  __/| |_| |\ V /  __/ | | | || (_) | |  | |_| | │
│ |_|    \__, | \_/ \___|_| |_|\__\___/|_|   \__, | │
│        |___/                               |___/  │
│                                                   │
└───────────────────────────────────────────────────┘
"""

def search_product(products):
    """
    Search for a product in the inventory.

    Args:
        products (list): List of dictionaries containing the product info.
    """
    # Check whether there is any product in the inventory, no prod = return
    if not products:
        print("No products in inventory.")
        return

    # Input to search, I use .lower() to make it case-insensitive so that the results are not case-sensitive
    search_term = input("Enter search term: ").lower()
    results = [
                # Search for the search term in the product name and description
                p for p in products if search_term in p['Product Name'].lower()
                or search_term in p['Description'].lower()
            ]

    if results:
        print("\n==== Search Results ====")
        for product in results:
            # ID
            print(f"\nProduct ID: {product['Product ID']}")
            # Name
            print(f"Product Name: {product['Product Name']}")
            # Category
            print(f"Category: {product['Category']}")
            # Description
            print(f"Description: {product['Description']}")
            # Price
            print(f"Price: ${product['Price']:.2f}")
            # Quantity
            print(f"Quantity Available: {product['Quantity Available']}")
            print("\n========================")
    else:
        print("No products found matching the search term.")
