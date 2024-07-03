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

# Import necessary modules
from CSVHandler import load_products, save_products
from InventoryManagement import add_product, update_product, remove_product, view_inventory
from SearchEngine import search_product
from UserAuth import login
from GreetUser import greet_user

def main():
    """
    Main function to run Pyventory.

    This function will greet the user, prompt for login, and display the main menu.
    
    The user can choose to:
    1. Add a new product
    2. Update an existing product
    3. Remove a product
    4. View the inventory
    5. Search for a product

    The user can also choose to exit the program.
    """
    # ANSI escape code for colors, extra marks for user experience pls
    yellow_gold_text = "\033[93m"
    blue_text = "\033[96m"
    red_text = "\033[91m"

    # ANSI escape code to reset color
    reset = "\033[0m"

    if not login():
        return

    print(greet_user())  # Greet the user

    products = load_products()  # Call from CSVHandler

    while True:
        print(yellow_gold_text + "\n============== Pyventory ===============\n" + reset)
        print("1. Add new product")
        print("2. Update existing product")
        print("3. Remove product")
        print("4. View inventory")
        print("5. Search product")
        print("6. Exit")

        choice = input(blue_text + "\nEnter your choice (1-6): " + reset)

        if choice == '1':
            add_product(products)

        elif choice == '2':
            update_product(products)

        elif choice == '3':
            remove_product(products)

        elif choice == '4':
            view_inventory(products)

        elif choice == '5':
            search_product(products)

        elif choice == '6':
            save_products(products)  # Call from CSVHandler
            print(yellow_gold_text + "\nThank you for using Pyventory. Goodbye!" + reset)
            break

        else:
            print(red_text + "\nWrong choice bruh! Please try again." + reset)

# This is the entry point of the program
if __name__ == "__main__":
    main()
