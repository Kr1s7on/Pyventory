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

# List of predefined categories
CATEGORIES = ["Electronics", "Mobile Devices", "Accessories", "Home Appliance"]

# ANSI escape code for colors
RED = "\033[91m"
GREEN = "\033[92m"
BLUE = "\033[34m"
YELLOW = "\033[93m"
MAGNETA = "\033[95m"
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

        if not product_id.strip():
            print(RED + "\nProduct ID cannot be blank." + RESET)

        elif not product_id.isdigit():
            print(RED + "\nProduct ID must be numeric." + RESET)

        elif any(p['Product ID'] == product_id for p in products):
            print(RED + "\nProduct ID already exists. Please enter a unique ID." + RESET)

        else:
            break

    # Input name with validation
    while True:
        name = input("\nEnter Product Name: ")
        # When name is empty
        if name == "":
            print(RED + "\nProduct Name cannot be empty. Please enter a name." + RESET)

        else:
            break

    # Input category with validation
    while True:
        category = input(f"\nEnter Category {CATEGORIES}: ")
        if category in CATEGORIES:
            break
        print(RED + "\nInvalid category. Please choose from the list." + RESET)

    # Input description with validation
    while True:
        description = input("\nEnter Description: ")
        # When desc is empty
        if description == "":
            print(RED + "\nDescription cannot be empty. Please enter a description." + RESET)

        else:
            break

    # Input price with validation
    while True:
        try:
            price = float(input("\nEnter Price: "))
            break

        except ValueError:
            print(RED + "\nInvalid price. Please enter a number." + RESET)

    # Input quantity with validation
    while True:
        try:
            quantity = int(input("\nEnter Quantity Available: "))
            break

        except ValueError:
            print(RED + "\nInvalid quantity. Please enter a whole number." + RESET)

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
        print(RED + "No products in inventory." + RESET)
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
            print("\n")

        # Input description
        description = input(f"\nDescription [{product['Description']}]: ") or product['Description']

        # Input price with validation
        while True:
            price_input = input(f"\nPrice [{product['Price']}]: ") or str(product['Price'])
            try:
                price = float(price_input)
                break

            except ValueError:
                print(MAROON_HIGHLIGHT + "Invalid price. Please enter a number." + RESET)
                print("\n")

        # Input quantity with validation
        while True:
            quantity_input = input(f"\nQuantity Available [{product['Quantity Available']}]: ") or str(product['Quantity Available'])
            try:
                quantity = int(quantity_input)
                break

            except ValueError:
                print(MAROON_HIGHLIGHT + "Invalid quantity. Please enter a whole number." + RESET)
                print("\n")

        # Update product
        product.update({
            'Product Name': name,
            'Category': category,
            'Description': description,
            'Price': price,
            'Quantity Available': quantity
        })
        print("\n")
        print(GREEN_HIGHLIGHT + "Product updated successfully!" + RESET)

    else:
        print(MAROON_HIGHLIGHT + "Product not found." + RESET)

def remove_product(products):
    """
    Remove a product from the inventory.

    Args:
        products (list): List of dictionaries containing product information.
    """

    # Validation for when thers no products in the csv
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

    print(BLUE + "\n=============== Current Inventory ===============" + RESET)
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
        print(BLUE + "\n================================================" + RESET)

    # Calculate total value and no. of prod
    print(MAGNETA + "\n======= Inventory Summary =======\n" + RESET)
    print(f"Total number of products: {len(products)}")

    total_value = sum(p['Price'] * p['Quantity Available'] for p in products)

    print(f"Total inventory value: ${total_value:.2f}")
    print(MAGNETA + "\n=================================" + RESET)
