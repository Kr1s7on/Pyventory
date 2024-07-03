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

This file contains functions to handle CSV file operations.
"""

# Import libraries
import csv
import os

# File to store product data
PRODUCTS_FILE = "products.csv"

def load_products():
    """
    Load products from CSV file.

    Returns:
        list: List of dictionaries containing product information.

    It reads the products from the CSV then returns a list of dictionaries.
    """
    # Initialise empty list to store the products
    products = []
    if os.path.exists(PRODUCTS_FILE):

        with open(PRODUCTS_FILE, 'r', encoding='utf-8') as file:

            reader = csv.DictReader(file)

            for row in reader:
                # Converts the price and quantity to appropriate types so that they can be used in calculations (the total stats basically)
                row['Price'] = float(row['Price'])
                row['Quantity Available'] = int(row['Quantity Available'])
                products.append(row)

    return products

def save_products(products):
    """
    Save products to CSV file.

    Args:
        products (list): List of dictionaries containing product information.

    This function writes the products into the CSV file.
    """
    with open(PRODUCTS_FILE, 'w', newline='', encoding='utf-8') as file:
        # Write the header first with the fieldnames
        writer = csv.DictWriter(file, fieldnames=['Product ID', 'Product Name', 'Category', 'Description', 'Price', 'Quantity Available'])

        # add the header
        writer.writeheader()

        # then write the rows
        writer.writerows(products)
