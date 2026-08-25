#!/usr/bin/env python3
"""
Product Summary Program

This program collects product information and calculates
the total inventory value for that product.
"""

product_name = input("Enter product name: ")
category = input("Enter product category: ")
price = float(input("Enter product price: "))
quantity = int(input("Enter product quantity: "))

total_value = price * quantity

print("\nProduct Summary")
print("---------------")
print(f"Product Name: {product_name}")
print(f"Category: {category}")
print(f"Price: ${price:.2f}")
print(f"Quantity: {quantity}")
print(f"Total Inventory Value: ${total_value:.2f}")
