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
from SearchEngine import search_inv
from UserAuth import login
from GreetUser import greet_user

# ANSI escape code for colors
YELLOW = "\033[93m"
LIGHT_BLUE = "\033[94m"
RED = "\033[91m"

# ANSI escape code to RESET color
RESET = "\033[0m"

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

    if not login():
        return

    # print(greet_user())  # Greet the user

    products = load_products()  # Call from CSVHandler

    while True:
        print(YELLOW + "\n\n============== Pyventory ===============\n" + RESET)
        print(greet_user())
        print("\n")
        print("1. Add new product")
        print("2. Update existing product")
        print("3. Remove product")
        print("4. View inventory")
        print("5. Search product")
        print("6. Exit")

        choice = input(LIGHT_BLUE + "\nWhat would you like to do (1-6)? " + RESET)

        if choice == '1':
            add_product(products)

        elif choice == '2':
            update_product(products)

        elif choice == '3':
            remove_product(products)

        elif choice == '4':
            view_inventory(products)

        elif choice == '5':
            search_inv(products)

        elif choice == '6':
            save_products(products)  # Call from CSVHandler
            print(YELLOW + "\nThank you for using Pyventory. Goodbye!" + RESET)
            break

        else:
            print(RED + "\nWRONG choice! Please try again." + RESET)

# This is the entry point of the program
if __name__ == "__main__":
    main()
