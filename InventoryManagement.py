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

# List of predefined categories
CATEGORIES = ["Electronics", "Mobile Devices", "Accessories", "Home Appliance"]

def add_product(products):
    """
    Add a new product to the inventory.

    Args:
        products (list): List of dictionaries containing product information.
    """
    print("\nAdding a new product:")

    # Input product details with validation
    while True:
        product_id = input("Enter Product ID: ")
        if any(p['Product ID'] == product_id for p in products):
            print("Product ID already exists. Please enter a unique ID.")
        else:
            break

    name = input("Enter Product Name: ")

    while True:
        category = input(f"Enter Category {CATEGORIES}: ")
        if category in CATEGORIES:
            break
        print("Invalid category. Please choose from the list.")

    description = input("Enter Description: ")

    while True:
        try:
            price = float(input("Enter Price: "))
            break
        except ValueError:
            print("Invalid price. Please enter a number.")

    while True:
        try:
            quantity = int(input("Enter Quantity Available: "))
            break
        except ValueError:
            print("Invalid quantity. Please enter a whole number.")

    # Create new product dictionary and add to list
    new_product = {
        'Product ID': product_id,
        'Product Name': name,
        'Category': category,
        'Description': description,
        'Price': price,
        'Quantity Available': quantity
    }
    products.append(new_product)
    print("Product added successfully!")

def update_product(products):
    """
    Update an existing product.

    Args:
        products (list): List of dictionaries containing product information.
    """
    if not products:
        print("No products in inventory.")
        return

    product_id = input("Enter Product ID to update: ")
    product = next((p for p in products if p['Product ID'] == product_id), None)

    if product:
        print("\nCurrent product details:")
        print(product)
        print("\nEnter new details (press Enter to keep current value):")
        
        name = input(f"Product Name [{product['Product Name']}]: ") or product['Product Name']
    
        while True:
            category = input(f"Category {CATEGORIES} [{product['Category']}]: ") or product['Category']
            if category in CATEGORIES:
                break
            print("Invalid category. Please choose from the list.")

        description = input(f"Description [{product['Description']}]: ") or product['Description']
    
        while True:
            price_input = input(f"Price [{product['Price']}]: ") or str(product['Price'])
            try:
                price = float(price_input)
                break
            except ValueError:
                print("Invalid price. Please enter a number.")

        while True:
            quantity_input = input(f"Quantity Available [{product['Quantity Available']}]: ") or str(product['Quantity Available'])
            try:
                quantity = int(quantity_input)
                break
            except ValueError:
                print("Invalid quantity. Please enter a whole number.")

        # Update product
        product.update({
            'Product Name': name,
            'Category': category,
            'Description': description,
            'Price': price,
            'Quantity Available': quantity
        })
        print("Product updated successfully!")
    else:
        print("Product not found.")

def remove_product(products):
    """
    Remove a product from the inventory.

    Args:
        products (list): List of dictionaries containing product information.
    """
    if not products:
        print("No products in inventory.")
        return

    product_id = input("Enter Product ID to remove: ")
    product = next((p for p in products if p['Product ID'] == product_id), None)
 
    if product:
        products.remove(product)
        print("Product removed successfully!")
    else:
        print("Product not found.")

def view_inventory(products):
    """
    Display all products in the inventory.

    Args:
        products (list): List of dictionaries containing product information.

    This function prints the product details in a formatted manner.
        + the total no. of prod and the respective total value of the whole thing (Since assignment brief says so)
    """
    if not products:
        print("No products in inventory.")
        return

    print("\n==== Current Inventory ====")
    for product in products:
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

    # Calculate total value and no. of prod
    print("\n==== Inventory Summary ====")
    print(f"Total number of products: {len(products)}")

    total_value = sum(p['Price'] * p['Quantity Available'] for p in products)
    
    print(f"Total inventory value: ${total_value:.2f}")
    print("===========================")
