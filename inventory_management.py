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

"""
InventoryManagement.py contains functions to manage the inventory.

Operations include:
- Adding a new product
- Updating an existing product
- Removing a product
- Viewing the inventory

The add_product() function:
    1. prompts the user to enter product details,
    2. validates the input,
    3. adds the new product to the inventory.
    
The update_product() function:
    1. prompts the user to enter the product ID to update,
    2. finds the product with the given ID,
    3. updates the product details.

The remove_product() function:
    1. prompts the user to enter the product ID to remove,
    2. finds the product with the given ID,
    3. removes the product from the inventory.

The view_inventory() function:
    1. displays all products in the inventory.
    2. calculates the total value of the inventory.
    3. displays the total number of products in the inventory.
"""

from csv_handler import save_products

# List of predefined categories
CATEGORIES = ["Electronics", "Mobile Devices", "Accessories", "Home Appliance"]

# ANSI escape code for colors
RED = "\033[91m"
GREEN = "\033[92m"
BLUE = "\033[34m"
YELLOW = "\033[93m"
MAGNETA = "\033[95m"
PALE_ORANGE = "\033[38;5;208m"
GREEN_HIGHLIGHT = "\033[48;5;22m\033[37m"
MAROON_HIGHLIGHT = "\033[48;5;1m\033[97m"
YELLOW_HIGHLIGHT = "\033[30;43m"

# ANSI escape code to RESET color
RESET = "\033[0m"

def add_product(products):
    """
    Add a new product to the inventory.

    Args:
        products (list): List of dictionaries containing product information.
    """
    print("\nAdding a new product")
    print("========================")

    # Input ID with validation
    while True:
        product_id = input("\nEnter Product ID: ")
        # When ID is empty
        if not product_id.strip():
            print(MAROON_HIGHLIGHT + "Product ID cannot be blank." + RESET)

        # When ID is not numeric
        elif not product_id.isdigit():
            print(MAROON_HIGHLIGHT + "Product ID must be numeric." + RESET)

        # When ID already exists
        elif any(p['Product ID'] == product_id for p in products):
            print(MAROON_HIGHLIGHT + "Product ID already exists. Please enter a unique ID." + RESET)

        else:
            break

    # Input name with validation
    while True:
        name = input("\nEnter Product Name: ")
        # When name is empty
        if name == "":
            print(MAROON_HIGHLIGHT + "Product Name cannot be empty. Please enter a name." + RESET)

        else:
            break

    # Input category with validation
    while True:
        category = input(f"\nEnter Category {CATEGORIES}: ")
        if category in CATEGORIES:
            break
        print(MAROON_HIGHLIGHT + "Invalid category. Please choose from the list." + RESET)

    # Input description with validation
    while True:
        description = input("\nEnter Description: ")
        # When desc is empty
        if description == "":
            print(MAROON_HIGHLIGHT + "Description cannot be empty. Please enter a description." + RESET)

        else:
            break

    # Input price with validation
    while True:
        try:
            price = float(input("\nEnter Price: "))
            if price < 0:
                print(MAROON_HIGHLIGHT + "What world do you live in? How can price be -ve? Enter a +ve number." + RESET)
                continue
            break

        except ValueError:
            print(MAROON_HIGHLIGHT + "Invalid price. Please enter a number." + RESET)

    # Input quantity with validation
    while True:
        try:
            quantity = int(input("\nEnter Quantity Available: "))
            if quantity < 0:
                print(MAROON_HIGHLIGHT + "What world do you live in? How can price be -ve? Enter a +ve number." + RESET)
                continue
            break

        except ValueError:
            print(MAROON_HIGHLIGHT + "Invalid quantity. Please enter a whole number." + RESET)

    # Create new product dictionary and add to list
    new_product = {
        'Product ID': product_id,
        'Product Name': name,
        'Category': category,
        'Description': description,
        'Price': price,
        'Quantity Available': quantity
    }

    # Append the new product to the list
    products.append(new_product)
    save_products(products)
    print("\n========================")
    print(GREEN_HIGHLIGHT + "Product added successfully!" + RESET)

def update_product(products):
    """
    Update an existing product.

    Args:
        products (list): List of dictionaries containing product information.
    """

    # Validation for when thers no products in the csv
    if not products:
        print(MAROON_HIGHLIGHT + "No products in inventory." + RESET)
        return

    # Input product ID to update
    print("\n")
    product_id = input("Enter Product ID to update: ")

    # Find the product with the given ID
    product = next((p for p in products if p['Product ID'] == product_id), None)

    # If product is found, update the details
    if product:
        print("\n")
        print(YELLOW + "============ Current product details ============" + RESET)
        print(product)
        print("\n")
        print(YELLOW + "Entering new details..." + RESET)
        print(YELLOW_HIGHLIGHT + "(press ENTER to keep the original)" + RESET)

        # Input name
        name = input(f"\nProduct Name [{product['Product Name']}]: ") or product['Product Name']

        # Input categories with validation
        while True:
            category = input(f"\nCategory {CATEGORIES} [{product['Category']}]: ") or product['Category']
            if category in CATEGORIES:
                break

            print(MAROON_HIGHLIGHT + "Invalid category. Please choose from the list." + RESET)

        # Input description
        description = input(f"\nDescription [{product['Description']}]: ") or product['Description']

        # Input price with validation
        while True:
            price_input = input(f"\nPrice [{product['Price']}]: ") or str(product['Price'])
            try:
                price = float(price_input)
                if price < 0:
                    print(MAROON_HIGHLIGHT + "What world do you live in? How can price be -ve? Enter a +ve number." + RESET)
                    continue
                break

            except ValueError:
                print(MAROON_HIGHLIGHT + "Invalid price. Enter a number." + RESET)

        # Input quantity with validation
        while True:
            quantity_input = input(f"\nQuantity Available [{product['Quantity Available']}]: ") or str(product['Quantity Available'])
            try:
                quantity = int(quantity_input)
                if quantity < 0:
                    print(MAROON_HIGHLIGHT + "How do you have -ve quantity? Enter a +ve number." + RESET)
                    continue
                break

            except ValueError:
                print(MAROON_HIGHLIGHT + "Invalid quantity. Enter a whole number." + RESET)

        # Update product
        product.update({
            'Product Name': name,
            'Category': category,
            'Description': description,
            'Price': price,
            'Quantity Available': quantity
        })
        print("\n")

        save_products(products)
        print(YELLOW + "==============================================" + RESET)
        print(GREEN_HIGHLIGHT + "Product updated successfully!" + RESET)

    else:
        print(MAROON_HIGHLIGHT + "Are you sure you typed the ID correctly? I might be blind but I don't see it in the CSV file." + RESET)

def remove_product(products):
    """
    Remove a product from the inventory.

    Args:
        products (list): List of dictionaries containing product information.
    """

    # Validation for when there's no products in the csv
    if not products:
        print("No products in inventory.")
        return

    # Input product ID to remove
    product_id = input(RED + "\nEnter Product ID to remove: " + RESET)
    # Find the product with the given ID
    product = next((p for p in products if p['Product ID'] == product_id), None)

    if product:
        # Remove the product from the csv
        products.remove(product)
        print(GREEN_HIGHLIGHT + "Product removed successfully!" + RESET)
        save_products(products)

    else:
        print(MAROON_HIGHLIGHT + "Product not found." + RESET)

def view_inventory(products):
    """
    Display all products in the inventory.

    Args:
        products (list): List of dictionaries containing product information.

    This function prints the product details in a formatted manner.
    + total no. of prod and respective total value of the whole thing
    """

    # Validation for when thers no products in the csv
    if not products:
        print("No products in inventory.")
        return

    print(PALE_ORANGE + "\n=============== Current Inventory ===============" + RESET)
    for product in products:
        # ID
        print(f"\nProduct ID: {product['Product ID']}")
        # Name
        print(f"Product Name: {product['Product Name']}")
        # Category
        print(f"\nCategory: {product['Category']}")
        # Description
        print(f"Description: {product['Description']}")
        # Price
        print(f"\nPrice: ${product['Price']:.2f}")
        # Quantity
        print(f"Quantity Available: {product['Quantity Available']}")
        print(PALE_ORANGE + "\n================================================" + RESET)

    # Calculate total value and no. of prod
    print(MAGNETA + "\n=============== Inventory Summary ==============\n" + RESET)
    print(f"Total number of products: {len(products)}")

    total_value = sum(p['Price'] * p['Quantity Available'] for p in products)

    print(f"Total inventory value: ${total_value:.2f}")
    print(MAGNETA + "\n================================================" + RESET)
