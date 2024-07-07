# Author: Jesalva Kriston Jomari Ballesteros
# Admin No / Grp: 231165R / AA2402

# ┌───────────────────────────────────────────────────┐
# │                                                   │
# │  ____                        _                    │
# │ |  _ \ _   ___   _____ _ __ | |_ ___  _ __ _   _  │
# │ | |_) | | | \ \ / / _ \ '_ \| __/ _ \| '__| | | | │
# │ |  __/| |_| |\ V /  __/ | | | || (_) | |  | |_| | │
# │ |_|    \__, | \_/ \___|_| |_|\__\___/|_|   \__, | │
# │        |___/                               |___/  │
# │                                                   │
# └───────────────────────────────────────────────────┘

# ANSI escape code for colors, extra marks for user experience pls
YELLOW = "\033[93m"
MAROON_HIGHLIGHT = "\033[48;5;1m\033[97m"

# ANSI escape code to RESET color
RESET = "\033[0m"

def search_inv(products):
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
    search_term = input("\nEnter search term: ").lower()
    results = [
                # Search for the search term in the product name and description
                p for p in products if search_term in p['Product Name'].lower()
                or search_term in p['Description'].lower()
            ]

    if results:
        print(YELLOW + "\n==== Search Results ====" + RESET)
        for product in results:
            
            print(f"\nProduct ID: {product['Product ID']}") # ID
            print(f"Product Name: {product['Product Name']}") # Name
            print("-" * 10)
            print(f"Category: {product['Category']}") # Category
            print(f"Description: {product['Description']}") # Description
            print("-" * 10)
            print(f"Price: ${product['Price']:.2f}") # Price
            print(f"Quantity Available: {product['Quantity Available']}") # Quantity
            print(YELLOW + "\n========================" + RESET)

    else:
        print(MAROON_HIGHLIGHT + "No products found matching the search term." + RESET)
