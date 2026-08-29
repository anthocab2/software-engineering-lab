"""
Practice: Reusing multiple functions together.

This exercise demonstrates how different functions can have different
responsibilities and work together on the same data.

calculate_product_value() is responsible for calculating inventory value.
check_stock() is responsible for determining stock status.

The main loop sends each product to both functions, stores their returned
values, and combines the results for display.

Separating responsibilities like this helps make backend code easier
to read, test, maintain, and reuse.
"""

products = [
    {"name": "Laptop", "price": 800, "quantity": 2},
    {"name": "Mouse", "price": 25, "quantity": 0},
    {"name": "Monitor", "price": 200, "quantity": 5},
]


def calculate_product_value(product):
    """Return the inventory value of one product."""
    return product["price"] * product["quantity"]


def check_stock(product):
    """Return the stock status of one product."""
    if product["quantity"] == 0:
        return "Out of stock"

    if product["quantity"] <= 3:
        return "Low stock"

    return "Available"


for product in products:
    # Each function receives the same product but performs a different job.
    value = calculate_product_value(product)
    status = check_stock(product)

    print(
        f'{product["name"]} - '
        f"Value: {value} - "
        f"Status: {status}"
    )
