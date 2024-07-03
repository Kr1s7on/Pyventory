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

# Import libraries
import csv
import os
import getpass

# List of predefined categories
CATEGORIES = ["Electronics", "Mobile Devices", "Accessories", "Home Appliance"]

# File to store product data
PRODUCTS_FILE = "products.csv"
PASSWORDS_FILE = "passwords.txt"

def load_products():
    """
    Load products from CSV file.

    Returns:
        list: List of dictionaries containing product information.
    """
    products = []
    if os.path.exists(PRODUCTS_FILE):
        with open(PRODUCTS_FILE, 'r', newline='', encoding='utf-8') as file:
            reader = csv.DictReader(file)
            for row in reader:
                # Convert price and quantity to appropriate types
                row['Price'] = float(row['Price'])
                row['Quantity Available'] = int(row['Quantity Available'])
                products.append(row)
    return products

def save_products(products):
    """
    Save products to CSV file.

    Args:
        products (list): List of dictionaries containing product information.
    """
    with open(PRODUCTS_FILE, 'w', newline='', encoding='utf-8') as file:
        fieldnames = ['Product ID', 'Name', 'Price', 'Quantity Available']
        writer = csv.DictWriter(file, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(products)

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
    """
    if not products:
        print("No products in inventory.")
        return

    print("\n==== Current Inventory ====")
    for product in products:
        print(f"\nProduct ID: {product['Product ID']}")
        print(f"Product Name: {product['Product Name']}")
        print(f"Category: {product['Category']}")
        print(f"Description: {product['Description']}")
        print(f"Price: ${product['Price']:.2f}")
        print(f"Quantity Available: {product['Quantity Available']}")
        print("========================")
    
    print("\n==== Inventory Summary ====")
    print(f"Total number of products: {len(products)}")
    total_value = sum(p['Price'] * p['Quantity Available'] for p in products)
    print(f"Total inventory value: ${total_value:.2f}")
    print("========================")

def search_product(products):
    """
    Search for a product in the inventory.

    Args:
        products (list): List of dictionaries containing product information.
    """
    if not products:
        print("No products in inventory.")
        return

    search_term = input("Enter search term: ").lower()
    results = [p for p in products if search_term in p['Product Name'].lower() or search_term in p['Description'].lower()]
    
    if results:
        print("\n==== Search Results ====")
        for product in results:
            print(f"\nProduct ID: {product['Product ID']}")
            print(f"Product Name: {product['Product Name']}")
            print(f"Category: {product['Category']}")
            print(f"Description: {product['Description']}")
            print(f"Price: ${product['Price']:.2f}")
            print(f"Quantity Available: {product['Quantity Available']}")
            print("========================")
    else:
        print("No products found matching the search term.")

def login():
    """
    Perform user login.

    Returns:
        bool: True if login is successful, False otherwise.
    """
    username = input("Enter username: ")
    password = getpass.getpass("Enter password: ")

    with open(PASSWORDS_FILE, 'r', encoding='utf-8') as file:
        for line in file:
            stored_username, stored_password = line.strip().split(':')
            if username == stored_username and password == stored_password:
                print("Login successful!")
                return True
    
    print("Invalid username or password.")
    return False

def main():
    """
    Main function to run the Pyventory system.
    """
    if not login():
        return

    products = load_products()

    while True:
        print("\n===== Pyventory =====")
        print("1. Add new product")
        print("2. Update existing product")
        print("3. Remove product")
        print("4. View inventory")
        print("5. Search product")
        print("6. Exit")

        choice = input("Enter your choice (1-6): ")

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
            save_products(products)
            print("Thank you for using Pyventory. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

        save_products(products)

if __name__ == "__main__":
    main()